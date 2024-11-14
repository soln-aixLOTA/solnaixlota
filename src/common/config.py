import os
from pathlib import Path
import yaml
from typing import Dict, Any

class Settings:
    """Configuration management class"""
    def __init__(self):
        self.env = os.getenv("APP_ENV", "development")
        self.config = self._load_config()
        self.secrets = self._load_secrets()

    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from YAML file"""
        config_path = Path(f"configs/environments/{self.env}.yaml")
        if not config_path.exists():
            raise FileNotFoundError(f"Configuration file {config_path} not found.")
        with open(config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)

    def _load_secrets(self) -> Dict[str, str]:
        """Load secrets from environment variables"""
        secrets = {
            "API_KEY": os.getenv("API_KEY"),
            "DB_PASSWORD": os.getenv("DB_PASSWORD"),
            "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY"),
            "JWT_SECRET_KEY": os.getenv("JWT_SECRET_KEY"),
            "SQLALCHEMY_DATABASE_URI": os.getenv("SQLALCHEMY_DATABASE_URI"),
        }
        missing = [key for key, value in secrets.items() if not value]
        if missing:
            raise EnvironmentError(f"Missing environment variables: {', '.join(missing)}")
        return secrets

    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value"""
        return self.config.get(key, default) 