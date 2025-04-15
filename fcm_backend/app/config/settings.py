from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # ... existing code ...
    
    # Billing Configuration
    API_DAILY_LIMIT: int = 1000
    API_MONTHLY_LIMIT: int = 30000
    API_PRICE_PER_REQUEST: float = 0.01
    API_FREE_TIER_DAILY_LIMIT: int = 100
    API_FREE_TIER_MONTHLY_LIMIT: int = 3000
    
    class Config:
        env_file = ".env"

settings = Settings() 