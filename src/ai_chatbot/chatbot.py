import logging
import logging.config
from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from src.common.logging import setup_logging
from src.common.security import require_api_key
from src.common.config import Settings
from src.common.middleware import error_handler, request_logger
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from flask_caching import Cache
import time
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from flask_compress import Compress
from celery import Celery

def create_app():
    app = Flask(__name__)

    settings = Settings()

    setup_logging()
    logger = logging.getLogger('ai_chatbot.chatbot')

    limiter = Limiter(app, key_func=get_remote_address)
    cache = Cache(config={'CACHE_TYPE': 'simple'})
    cache.init_app(app)
    db = SQLAlchemy(app)
    Compress(app)
    celery = Celery(
        app.name,
        broker=f"redis://{settings.get('CACHE_REDIS_HOST', 'localhost')}:{settings.get('CACHE_REDIS_PORT', 6379)}/0",
        backend=f"redis://{settings.get('CACHE_REDIS_HOST', 'localhost')}:{settings.get('CACHE_REDIS_PORT', 6379)}/0"
    )

    app.before_request(request_logger)
    app.after_request(lambda response: after_request(response, logger))
    app.register_error_handler(Exception, error_handler)

    @app.route('/chat', methods=['POST'])
    def chat():
        try:
            data = request.get_json()
            if not data:
                return jsonify({"error": "No data provided"}), 400
                
            user_input = data.get('message', '')
            if not user_input:
                return jsonify({"error": "No message provided"}), 400
                
            logger.info("Received message: %s", user_input)
        
            response_text = generate_response(user_input)
            response = {"reply": response_text}
            
            logger.info("Sending reply: %s", response['reply'])
            return jsonify(response)
            
        except Exception as e:
            logger.error("Error processing request: %s", str(e))
            return jsonify({"error": "Internal server error"}), 500

    @app.route('/healthz', methods=['GET'])
    def healthz():
        return jsonify({"status": "OK"}), 200

    @app.route('/readyz', methods=['GET'])
    def readyz():
        try:
            db.session.execute(text('SELECT 1'))
            return jsonify({"status": "Ready"}), 200
        except Exception as e:
            logger.error(f"Readiness check failed: {e}")
            return jsonify({"status": "Not Ready"}), 500
    
    def generate_response(message):
        return f"Echo: {message}"

    @celery.task
    def process_message(message):
        time.sleep(5)  
        return f"Processed: {message}"

    @app.route('/process', methods=['POST'])
    @require_api_key
    @limiter.limit("5 per minute")
    def process():
        data = request.get_json()
        message = data.get('message', '')
        task = process_message.delay(message)
        logger.info("Started background task %s for message: %s", task.id, message)
        return jsonify({"task_id": task.id, "status": "Processing"}), 202

    @app.route('/metrics', methods=['GET'])
    def metrics():
        return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

    @app.route('/db', methods=['GET'])
    @cache.cached(timeout=120)
    def db_operation():
        try:
            result = db.session.execute(text('SELECT 1')).fetchall()
            return jsonify(result=str(result)), 200
        except Exception as e:
            logger.error("Database operation failed: %s", e)
            return jsonify({"error": "Database operation failed"}), 500

    if __name__ == '__main__':
        app = create_app()
        app.run(host='0.0.0.0', port=5000)

    return app

def after_request(response, logger):
    if hasattr(request, 'start_time'):
        elapsed = time.time() - request.start_time
        logger.info("Request completed in %.2f seconds", elapsed)
    return response

app = create_app()