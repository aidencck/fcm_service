from .redis_client import RedisClient
from ..config.settings import settings
import logging

logger = logging.getLogger(__name__)

def init_redis():
    """
    初始化Redis连接
    """
    try:
        # 获取Redis客户端实例
        redis_client = RedisClient(**settings.redis_config)
        logger.info("Redis client initialized successfully")
        
        # 测试连接
        if redis_client.get('test_connection'):
            logging.info("Redis connection test successful")
        else:
            # 设置测试键
            redis_client.set('test_connection', 'ok', expire=60)
            logging.info("Redis connection established and tested")
            
        return redis_client
    except Exception as e:
        logger.error(f"Failed to initialize Redis client: {str(e)}")
        raise 