from pydantic import BaseSettings
from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    # Firebase Configuration
    FIREBASE_CREDENTIALS_PATH: str = os.getenv("FIREBASE_CREDENTIALS_PATH", "")
    FIREBASE_PROJECT_ID: str = os.getenv("FIREBASE_PROJECT_ID", "")
    
    # API Configuration
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "FCM Backend"
    
    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days
    
    # Alexa Configuration
    ALEXA_CLIENT_ID: Optional[str] = os.getenv("ALEXA_CLIENT_ID")
    ALEXA_CLIENT_SECRET: Optional[str] = os.getenv("ALEXA_CLIENT_SECRET")
    
    # Google Assistant Configuration
    GOOGLE_ASSISTANT_CREDENTIALS_PATH: Optional[str] = os.getenv("GOOGLE_ASSISTANT_CREDENTIALS_PATH")
     # Billing Configuration
    API_DAILY_LIMIT: int = 1000
    API_MONTHLY_LIMIT: int = 30000
    API_PRICE_PER_REQUEST: float = 0.01
    API_FREE_TIER_DAILY_LIMIT: int = 100
    API_FREE_TIER_MONTHLY_LIMIT: int = 3000
    
    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings() 