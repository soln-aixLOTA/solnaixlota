import logging
import logging.config
import yaml
from typing import Optional, Dict, Any

def setup_logging(name: str, logging_config: Dict[str, Any], default_level: int = logging.INFO) -> None:
    """Setup logging configuration"""
    try:
        logging.config.dictConfig(logging_config)
    except Exception as e:
        logging.basicConfig(level=default_level)
        logging.error(f"Error loading logging configuration: {e}")

    logger = logging.getLogger(name)
    logger.info("Logging is set up.") 