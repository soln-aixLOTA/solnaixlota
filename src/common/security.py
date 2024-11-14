from functools import wraps
from flask import request, abort
import jwt
from datetime import datetime, timedelta

class Security:
    def __init__(self, secret_key: str):
        self.secret_key = secret_key

    def generate_token(self, user_id: str) -> str:
        """Generate JWT token"""
        payload = {
            'user_id': user_id,
            'exp': datetime.utcnow() + timedelta(days=1)
        }
        return jwt.encode(payload, self.secret_key, algorithm='HS256')

    def validate_token(self, token: str) -> bool:
        """Validate JWT token"""
        try:
            jwt.decode(token, self.secret_key, algorithms=['HS256'])
            return True
        except jwt.InvalidTokenError:
            return False

def require_api_key(f):
    """Decorator to require API key"""
    @wraps(f)
    def decorated(*args, **kwargs):
        api_key = request.headers.get('X-API-Key')
        if not api_key or not validate_api_key(api_key):
            abort(401)
        return f(*args, **kwargs)
    return decorated

def validate_api_key(api_key: str) -> bool:
    """Validate API key"""
    # Implement your API key validation logic (e.g., check against a database or secure store)
    return True 