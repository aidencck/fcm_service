from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .middleware.rate_limiter import RateLimiter
from .api.v1.endpoints import fcm, users
from .config.settings import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add rate limiting middleware
app.add_middleware(
    RateLimiter,
    window_size=60,  # 1 minute window
    max_requests=100  # Max requests per minute
)

# Include routers
app.include_router(fcm.router, prefix=f"{settings.API_V1_STR}/fcm", tags=["fcm"])
app.include_router(users.router, prefix=f"{settings.API_V1_STR}/users", tags=["users"])

@app.get("/")
async def root():
    return {"message": "Welcome to FCM Backend API"} 