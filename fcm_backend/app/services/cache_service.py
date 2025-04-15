import logging
from typing import Any, Optional, Dict
from ..utils.redis_client import RedisClient
from ..config.redis_config import REDIS_CONFIG

class CacheService:
    def __init__(self):
        self.redis_client = RedisClient(**REDIS_CONFIG)
        self.prefix = "cache:"  # 缓存键前缀

    def set_cache(self, key: str, value: Any, expire: Optional[int] = None) -> bool:
        """
        设置缓存
        :param key: 缓存键
        :param value: 缓存值
        :param expire: 过期时间（秒）
        :return: 是否设置成功
        """
        try:
            cache_key = f"{self.prefix}{key}"
            return self.redis_client.set(cache_key, value, expire)
        except Exception as e:
            logging.error(f"Failed to set cache: {e}")
            return False

    def get_cache(self, key: str) -> Optional[Any]:
        """
        获取缓存
        :param key: 缓存键
        :return: 缓存值
        """
        try:
            cache_key = f"{self.prefix}{key}"
            return self.redis_client.get(cache_key)
        except Exception as e:
            logging.error(f"Failed to get cache: {e}")
            return None

    def delete_cache(self, key: str) -> bool:
        """
        删除缓存
        :param key: 缓存键
        :return: 是否删除成功
        """
        try:
            cache_key = f"{self.prefix}{key}"
            return self.redis_client.delete(cache_key)
        except Exception as e:
            logging.error(f"Failed to delete cache: {e}")
            return False

    def set_user_session(self, user_id: str, session_data: Dict[str, Any], expire: int = 3600) -> bool:
        """
        设置用户会话
        :param user_id: 用户ID
        :param session_data: 会话数据
        :param expire: 过期时间（秒）
        :return: 是否设置成功
        """
        try:
            session_key = f"session:{user_id}"
            return self.redis_client.set(session_key, session_data, expire)
        except Exception as e:
            logging.error(f"Failed to set user session: {e}")
            return False

    def get_user_session(self, user_id: str) -> Optional[Dict[str, Any]]:
        """
        获取用户会话
        :param user_id: 用户ID
        :return: 会话数据
        """
        try:
            session_key = f"session:{user_id}"
            return self.redis_client.get(session_key)
        except Exception as e:
            logging.error(f"Failed to get user session: {e}")
            return None

    def clear_user_session(self, user_id: str) -> bool:
        """
        清除用户会话
        :param user_id: 用户ID
        :return: 是否清除成功
        """
        try:
            session_key = f"session:{user_id}"
            return self.redis_client.delete(session_key)
        except Exception as e:
            logging.error(f"Failed to clear user session: {e}")
            return False

    def increment_counter(self, key: str, amount: int = 1) -> Optional[int]:
        """
        增加计数器
        :param key: 计数器键
        :param amount: 增加数量
        :return: 增加后的值
        """
        try:
            counter_key = f"counter:{key}"
            with self.redis_client.pipeline() as pipe:
                pipe.incrby(counter_key, amount)
                result = pipe.execute()
            return result[0]
        except Exception as e:
            logging.error(f"Failed to increment counter: {e}")
            return None

    def get_counter(self, key: str) -> Optional[int]:
        """
        获取计数器值
        :param key: 计数器键
        :return: 计数器值
        """
        try:
            counter_key = f"counter:{key}"
            value = self.redis_client.get(counter_key)
            return int(value) if value else 0
        except Exception as e:
            logging.error(f"Failed to get counter: {e}")
            return None 