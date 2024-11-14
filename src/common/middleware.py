"""Middleware functions for Flask application."""

from flask import request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import logging

# Initialize Limiter
limiter = Limiter(
    get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

def rate_limit_exceeded(e):
    """Handle rate limit exceeded errors."""
    logging.warning("Rate limit exceeded: %s", e)
    return jsonify(error="Rate limit exceeded"), 429

def generic_error_handler(error):
    """Handle generic errors."""
    logging.error("An error occurred: %s", error)
    return jsonify(error="Internal server error"), 500 