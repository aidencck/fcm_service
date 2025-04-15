import logging
from .redis_client import RedisClient
from ..config.redis_config import REDIS_CONFIG

def init_redis():
    """
    初始化Redis连接
    """
    try:
        # 获取Redis客户端实例
        redis_client = RedisClient(**REDIS_CONFIG)
        
        # 测试连接
        if redis_client.get('test_connection'):
            logging.info("Redis connection test successful")
        else:
            # 设置测试键
            redis_client.set('test_connection', 'ok', expire=60)
            logging.info("Redis connection established and tested")
            
        return redis_client
    except Exception as e:
        logging.error(f"Failed to initialize Redis: {e}")
        raise 