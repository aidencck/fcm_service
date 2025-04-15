from pydantic_settings import BaseSettings
from typing import List, Optional, Dict
import os
from dotenv import load_dotenv
from pathlib import Path
import json

# Load environment variables from .env file
load_dotenv()

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent.parent

class Settings(BaseSettings):
    # Project settings
    PROJECT_NAME: str = "FCM Backend"
    API_V1_STR: str = "/api/v1"
    DEBUG: bool = True

    # Security settings
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-here")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days
    BACKEND_CORS_ORIGINS: List[str] = ["*"]  # In production, set specific origins

    # Firebase settings
    FIREBASE_PROJECT_ID: str = os.getenv("FIREBASE_PROJECT_ID", "")
    FIREBASE_PRIVATE_KEY: str = os.getenv("FIREBASE_PRIVATE_KEY", "")
    FIREBASE_CLIENT_EMAIL: str = os.getenv("FIREBASE_CLIENT_EMAIL", "")
    FIREBASE_PRIVATE_KEY_ID: str = os.getenv("FIREBASE_PRIVATE_KEY_ID", "")
    FIREBASE_CLIENT_ID: str = os.getenv("FIREBASE_CLIENT_ID", "")
    FIREBASE_AUTH_URI: str = os.getenv("FIREBASE_AUTH_URI", "https://accounts.google.com/o/oauth2/auth")
    FIREBASE_TOKEN_URI: str = os.getenv("FIREBASE_TOKEN_URI", "https://oauth2.googleapis.com/token")
    FIREBASE_AUTH_PROVIDER_X509_CERT_URL: str = os.getenv("FIREBASE_AUTH_PROVIDER_X509_CERT_URL", "https://www.googleapis.com/oauth2/v1/certs")
    FIREBASE_CLIENT_X509_CERT_URL: str = os.getenv("FIREBASE_CLIENT_X509_CERT_URL", "")

    @property
    def firebase_credentials(self) -> Dict:
        """Get Firebase credentials as a dictionary."""
        return {
            "type": "service_account",
            "project_id": self.FIREBASE_PROJECT_ID,
            "private_key_id": self.FIREBASE_PRIVATE_KEY_ID,
            "private_key": self.FIREBASE_PRIVATE_KEY.replace("\\n", "\n"),
            "client_email": self.FIREBASE_CLIENT_EMAIL,
            "client_id": self.FIREBASE_CLIENT_ID,
            "auth_uri": self.FIREBASE_AUTH_URI,
            "token_uri": self.FIREBASE_TOKEN_URI,
            "auth_provider_x509_cert_url": self.FIREBASE_AUTH_PROVIDER_X509_CERT_URL,
            "client_x509_cert_url": self.FIREBASE_CLIENT_X509_CERT_URL
        }

    # Redis settings
    REDIS_HOST: str = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT: int = int(os.getenv("REDIS_PORT", "6379"))
    REDIS_DB: int = int(os.getenv("REDIS_DB", "0"))
    REDIS_PASSWORD: Optional[str] = os.getenv("REDIS_PASSWORD")
    REDIS_DECODE_RESPONSES: bool = True
    REDIS_SOCKET_TIMEOUT: int = 5
    REDIS_SOCKET_CONNECT_TIMEOUT: int = 5
    REDIS_RETRY_ON_TIMEOUT: bool = True

    # Billing settings
    BILLING_CONFIG: Dict = {
        'daily_api_limit': 1000,
        'monthly_api_limit': 30000,
        'api_price_per_call': 0.001,
        'free_tier_limit': 100,
        'subscription_tiers': {
            'free': {
                'daily_limit': 100,
                'monthly_limit': 3000,
                'price': 0
            },
            'basic': {
                'daily_limit': 1000,
                'monthly_limit': 30000,
                'price': 9.99
            },
            'premium': {
                'daily_limit': 10000,
                'monthly_limit': 300000,
                'price': 29.99
            }
        }
    }

    # API Usage Limits
    API_FREE_TIER_DAILY_LIMIT: int = 100
    API_FREE_TIER_MONTHLY_LIMIT: int = 3000
    API_DAILY_LIMIT: int = 1000
    API_MONTHLY_LIMIT: int = 30000

    class Config:
        env_file = ".env"
        case_sensitive = True

    @property
    def redis_config(self) -> Dict:
        """Get Redis configuration as a dictionary."""
        return {
            'host': self.REDIS_HOST,
            'port': self.REDIS_PORT,
            'db': self.REDIS_DB,
            'password': self.REDIS_PASSWORD,
            'decode_responses': self.REDIS_DECODE_RESPONSES,
            'socket_timeout': self.REDIS_SOCKET_TIMEOUT,
            'socket_connect_timeout': self.REDIS_SOCKET_CONNECT_TIMEOUT,
            'retry_on_timeout': self.REDIS_RETRY_ON_TIMEOUT
        }

# Create settings instance
settings = Settings() 