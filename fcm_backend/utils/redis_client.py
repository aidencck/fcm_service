import redis
from typing import Any, Optional, Union, List, Dict
import json
import logging

class RedisClient:
    _instance = None
    _redis_client = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(RedisClient, cls).__new__(cls)
        return cls._instance

    def __init__(self, host: str = 'localhost', port: int = 6379, db: int = 0, 
                 password: Optional[str] = None, decode_responses: bool = True):
        if self._redis_client is None:
            try:
                self._redis_client = redis.Redis(
                    host=host,
                    port=port,
                    db=db,
                    password=password,
                    decode_responses=decode_responses,
                    socket_timeout=5,
                    socket_connect_timeout=5,
                    retry_on_timeout=True
                )
                # 测试连接
                self._redis_client.ping()
                logging.info("Redis connection established successfully")
            except redis.ConnectionError as e:
                logging.error(f"Redis connection failed: {e}")
                raise

    @classmethod
    def get_instance(cls) -> 'RedisClient':
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def set(self, key: str, value: Any, expire: Optional[int] = None) -> bool:
        """设置键值对，支持设置过期时间"""
        try:
            if isinstance(value, (dict, list)):
                value = json.dumps(value)
            if expire:
                return self._redis_client.setex(key, expire, value)
            return self._redis_client.set(key, value)
        except Exception as e:
            logging.error(f"Redis set error: {e}")
            return False

    def get(self, key: str) -> Optional[Any]:
        """获取键值"""
        try:
            value = self._redis_client.get(key)
            if value is None:
                return None
            try:
                return json.loads(value)
            except json.JSONDecodeError:
                return value
        except Exception as e:
            logging.error(f"Redis get error: {e}")
            return None

    def delete(self, key: str) -> bool:
        """删除键"""
        try:
            return bool(self._redis_client.delete(key))
        except Exception as e:
            logging.error(f"Redis delete error: {e}")
            return False

    def exists(self, key: str) -> bool:
        """检查键是否存在"""
        try:
            return bool(self._redis_client.exists(key))
        except Exception as e:
            logging.error(f"Redis exists error: {e}")
            return False

    def expire(self, key: str, seconds: int) -> bool:
        """设置键的过期时间"""
        try:
            return bool(self._redis_client.expire(key, seconds))
        except Exception as e:
            logging.error(f"Redis expire error: {e}")
            return False

    def ttl(self, key: str) -> int:
        """获取键的剩余过期时间"""
        try:
            return self._redis_client.ttl(key)
        except Exception as e:
            logging.error(f"Redis ttl error: {e}")
            return -2

    def hset(self, key: str, field: str, value: Any) -> bool:
        """设置哈希字段"""
        try:
            if isinstance(value, (dict, list)):
                value = json.dumps(value)
            return bool(self._redis_client.hset(key, field, value))
        except Exception as e:
            logging.error(f"Redis hset error: {e}")
            return False

    def hget(self, key: str, field: str) -> Optional[Any]:
        """获取哈希字段值"""
        try:
            value = self._redis_client.hget(key, field)
            if value is None:
                return None
            try:
                return json.loads(value)
            except json.JSONDecodeError:
                return value
        except Exception as e:
            logging.error(f"Redis hget error: {e}")
            return None

    def hgetall(self, key: str) -> Dict[str, Any]:
        """获取所有哈希字段"""
        try:
            result = self._redis_client.hgetall(key)
            return {k: json.loads(v) if isinstance(v, str) and v.startswith('{') else v 
                   for k, v in result.items()}
        except Exception as e:
            logging.error(f"Redis hgetall error: {e}")
            return {}

    def sadd(self, key: str, *members: Any) -> int:
        """添加集合成员"""
        try:
            return self._redis_client.sadd(key, *members)
        except Exception as e:
            logging.error(f"Redis sadd error: {e}")
            return 0

    def smembers(self, key: str) -> set:
        """获取集合所有成员"""
        try:
            return self._redis_client.smembers(key)
        except Exception as e:
            logging.error(f"Redis smembers error: {e}")
            return set()

    def pipeline(self):
        """获取管道对象"""
        return self._redis_client.pipeline()

    def close(self):
        """关闭Redis连接"""
        if self._redis_client:
            self._redis_client.close()
            self._redis_client = None
            self._instance = None 