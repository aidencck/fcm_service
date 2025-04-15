import unittest
import sys
import os

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.cache_service import CacheService
from utils.redis_init import init_redis

class TestRedis(unittest.TestCase):
    def setUp(self):
        """测试前的准备工作"""
        self.cache_service = CacheService()
        self.test_key = "test_key"
        self.test_value = {"name": "test", "value": 123}
        self.test_user_id = "user123"
        self.test_session = {"token": "abc123", "role": "admin"}

    def test_basic_cache(self):
        """测试基本的缓存功能"""
        # 测试设置缓存
        self.assertTrue(self.cache_service.set_cache(self.test_key, self.test_value))
        
        # 测试获取缓存
        result = self.cache_service.get_cache(self.test_key)
        self.assertEqual(result, self.test_value)
        
        # 测试删除缓存
        self.assertTrue(self.cache_service.delete_cache(self.test_key))
        self.assertIsNone(self.cache_service.get_cache(self.test_key))

    def test_user_session(self):
        """测试用户会话功能"""
        # 测试设置会话
        self.assertTrue(self.cache_service.set_user_session(
            self.test_user_id, 
            self.test_session
        ))
        
        # 测试获取会话
        session = self.cache_service.get_user_session(self.test_user_id)
        self.assertEqual(session, self.test_session)
        
        # 测试清除会话
        self.assertTrue(self.cache_service.clear_user_session(self.test_user_id))
        self.assertIsNone(self.cache_service.get_user_session(self.test_user_id))

    def test_counter(self):
        """测试计数器功能"""
        counter_key = "test_counter"
        
        # 测试增加计数器
        initial_value = self.cache_service.increment_counter(counter_key)
        self.assertEqual(initial_value, 1)
        
        # 测试再次增加
        new_value = self.cache_service.increment_counter(counter_key, 2)
        self.assertEqual(new_value, 3)
        
        # 测试获取计数器值
        current_value = self.cache_service.get_counter(counter_key)
        self.assertEqual(current_value, 3)

    def test_cache_expiration(self):
        """测试缓存过期功能"""
        # 设置一个1秒后过期的缓存
        self.assertTrue(self.cache_service.set_cache(
            self.test_key, 
            self.test_value, 
            expire=1
        ))
        
        # 立即获取应该存在
        self.assertIsNotNone(self.cache_service.get_cache(self.test_key))
        
        # 等待1秒后应该过期
        import time
        time.sleep(1.1)
        self.assertIsNone(self.cache_service.get_cache(self.test_key))

if __name__ == '__main__':
    unittest.main() 