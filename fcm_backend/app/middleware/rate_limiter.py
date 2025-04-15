from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from ..utils.redis_client import RedisClient
from ..config.settings import settings
import logging
from typing import Optional

class RateLimiter(BaseHTTPMiddleware):
    def __init__(self, app, window_size: int = 60, max_requests: int = 100):
        super().__init__(app)
        self.redis_client = RedisClient(**settings.redis_config)
        self.rate_limit_prefix = "api_rate_limit:"
        self.window_size = window_size
        self.max_requests = max_requests

    async def dispatch(self, request: Request, call_next):
        try:
            # 获取客户端IP
            client_ip = request.client.host if request.client else "unknown"
            
            # 检查速率限制
            if not await self._check_rate_limit(client_ip):
                raise HTTPException(
                    status_code=429,
                    detail="Too many requests. Please try again later."
                )
            
            # 更新请求计数
            await self._update_rate_limit(client_ip)
            
            # 继续处理请求
            response = await call_next(request)
            return response
            
        except HTTPException as e:
            raise e
        except Exception as e:
            logging.error(f"Rate limiter error: {e}")
            # 在发生错误时仍然允许请求通过
            return await call_next(request)

    async def _check_rate_limit(self, client_ip: str) -> bool:
        """
        检查是否超过速率限制
        """
        try:
            cache_key = f"{self.rate_limit_prefix}{client_ip}"
            request_count = self.redis_client.get_counter(cache_key) or 0
            return request_count < self.max_requests
        except Exception as e:
            logging.error(f"Error checking rate limit: {e}")
            return True  # 发生错误时允许请求通过

    async def _update_rate_limit(self, client_ip: str):
        """
        更新请求计数
        """
        try:
            cache_key = f"{self.rate_limit_prefix}{client_ip}"
            self.redis_client.increment_counter(cache_key)
        except Exception as e:
            logging.error(f"Error updating rate limit: {e}") 