"""Flask application for processing data."""

import logging
from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy
from celery import Celery
from src.common.security import require_api_key

def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)

    # Configure Logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Initialize Extensions
    limiter = Limiter(app, key_func=get_remote_address)
    cache = Cache(config={'CACHE_TYPE': 'simple'})
    cache.init_app(app)
    db = SQLAlchemy(app)
    celery = Celery(app.name, broker='redis://localhost:6379/0')

    @app.route('/process', methods=['POST'])
    @require_api_key
    @limiter.limit("5 per minute")
    def process_data():
        """Endpoint to process incoming data."""
        data = request.get_json()
        logger.info("Processing data...")
        try:
            # Add processing logic here
            processed_data = data  # Placeholder for actual processing
            return jsonify({"status": "success", "data": processed_data}), 200
        except ValueError as ve:
            logger.error("Value error occurred: %s", ve)
            return jsonify({"status": "error", "message": str(ve)}), 400
        except Exception as e:
            logger.error("An unexpected error occurred: %s", e)
            return jsonify({"status": "error", "message": "Internal server error"}), 500

    @app.route('/healthz', methods=['GET'])
    def healthz():
        """Health check endpoint."""
        return jsonify({"status": "OK"}), 200

    @app.route('/readyz', methods=['GET'])
    def readyz():
        """Readiness check endpoint."""
        # Implement readiness logic here
        return jsonify({"status": "Ready"}), 200

    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)

    return app

app = create_app() 