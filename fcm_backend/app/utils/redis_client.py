import redis
import json
import logging
from typing import Optional, Any

class RedisClient:
    def __init__(self, **kwargs):
        self.client = redis.Redis(**kwargs)
        
    def get_counter(self, key: str) -> Optional[int]:
        """获取计数器值"""
        try:
            value = self.client.get(key)
            return int(value) if value else 0
        except Exception as e:
            logging.error(f"Error getting counter: {e}")
            return None
            
    def increment_counter(self, key: str, amount: int = 1) -> bool:
        """增加计数器值"""
        try:
            self.client.incrby(key, amount)
            return True
        except Exception as e:
            logging.error(f"Error incrementing counter: {e}")
            return False
            
    def set_expire(self, key: str, seconds: int) -> bool:
        """设置过期时间"""
        try:
            return self.client.expire(key, seconds)
        except Exception as e:
            logging.error(f"Error setting expire: {e}")
            return False
            
    def get(self, key: str) -> Optional[Any]:
        """获取值"""
        try:
            value = self.client.get(key)
            return json.loads(value) if value else None
        except Exception as e:
            logging.error(f"Error getting value: {e}")
            return None
            
    def set(self, key: str, value: Any, expire: Optional[int] = None) -> bool:
        """设置值"""
        try:
            serialized = json.dumps(value)
            if expire:
                return self.client.setex(key, expire, serialized)
            return self.client.set(key, serialized)
        except Exception as e:
            logging.error(f"Error setting value: {e}")
            return False 