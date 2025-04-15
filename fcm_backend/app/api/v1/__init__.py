from fastapi import APIRouter

from app.api.v1.endpoints import users, billing

api_router = APIRouter()

# 注册用户路由
api_router.include_router(users.router, prefix="/users", tags=["users"])

# 注册计费路由
api_router.include_router(billing.router, prefix="/billing", tags=["billing"]) 