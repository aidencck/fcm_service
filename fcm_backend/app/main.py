from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from .routes import auth, notifications, users, billing
from .utils.redis_client import RedisClient
from .services.billing_service import BillingService
from .utils.security import get_current_user
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

# Include routers
app.include_router(auth.router, prefix=f"{settings.API_V1_STR}/auth", tags=["auth"])
app.include_router(notifications.router, prefix=f"{settings.API_V1_STR}/notifications", tags=["notifications"])
app.include_router(users.router, prefix=f"{settings.API_V1_STR}/users", tags=["users"])
app.include_router(billing.router, prefix=f"{settings.API_V1_STR}/billing", tags=["billing"])

@app.middleware("http")
async def api_usage_middleware(request: Request, call_next):
    # 跳过非API路由
    if not request.url.path.startswith(f"{settings.API_V1_STR}/"):
        return await call_next(request)
        
    try:
        # 获取当前用户
        current_user = await get_current_user(request)
        if not current_user:
            return JSONResponse(
                status_code=401,
                content={"error": "Unauthorized"}
            )
            
        # 检查订阅状态
        billing_service = BillingService(RedisClient())
        subscription_info = billing_service.check_subscription(current_user)
        
        if subscription_info["is_expired"]:
            return JSONResponse(
                status_code=403,
                content={
                    "error": "Subscription expired",
                    "subscription_status": subscription_info["status"]
                }
            )
            
        # 检查API使用限制
        usage_info = billing_service.check_api_usage(current_user)
        
        if usage_info["is_daily_exceeded"]:
            return JSONResponse(
                status_code=429,
                content={
                    "error": "Daily API limit exceeded",
                    "daily_usage": usage_info["daily_usage"],
                    "daily_remaining": usage_info["daily_remaining"]
                }
            )
            
        if usage_info["is_monthly_exceeded"]:
            return JSONResponse(
                status_code=429,
                content={
                    "error": "Monthly API limit exceeded",
                    "monthly_usage": usage_info["monthly_usage"],
                    "monthly_remaining": usage_info["monthly_remaining"]
                }
            )
            
        # 增加使用计数
        if not billing_service.increment_api_usage(current_user):
            return JSONResponse(
                status_code=500,
                content={"error": "Failed to update usage count"}
            )
            
        # 处理请求
        response = await call_next(request)
        
        # 添加使用信息到响应头
        response.headers["X-Daily-Usage"] = str(usage_info["daily_usage"])
        response.headers["X-Monthly-Usage"] = str(usage_info["monthly_usage"])
        response.headers["X-Daily-Remaining"] = str(usage_info["daily_remaining"])
        response.headers["X-Monthly-Remaining"] = str(usage_info["monthly_remaining"])
        response.headers["X-Subscription-Status"] = subscription_info["status"]
        response.headers["X-Subscription-Tier"] = subscription_info["tier"]
        
        return response
        
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )

@app.get("/")
async def root():
    return {"message": "Welcome to FCM Backend API"} 