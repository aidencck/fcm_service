from utils.redis_client import RedisClient
from config.redis_config import REDIS_CONFIG

def main():
    # 获取Redis客户端实例
    redis_client = RedisClient(**REDIS_CONFIG)
    
    # 基本键值操作
    redis_client.set('test_key', 'test_value')
    value = redis_client.get('test_key')
    print(f"Get value: {value}")
    
    # 设置带过期时间的键
    redis_client.set('temp_key', 'temp_value', expire=60)
    
    # 哈希操作
    user_data = {
        'name': 'John',
        'age': 30,
        'email': 'john@example.com'
    }
    redis_client.hset('user:1', 'profile', user_data)
    profile = redis_client.hget('user:1', 'profile')
    print(f"User profile: {profile}")
    
    # 集合操作
    redis_client.sadd('online_users', 'user1', 'user2', 'user3')
    online_users = redis_client.smembers('online_users')
    print(f"Online users: {online_users}")
    
    # 使用管道进行批量操作
    with redis_client.pipeline() as pipe:
        pipe.set('key1', 'value1')
        pipe.set('key2', 'value2')
        pipe.set('key3', 'value3')
        pipe.execute()
    
    # 检查键是否存在
    exists = redis_client.exists('key1')
    print(f"Key1 exists: {exists}")
    
    # 获取键的剩余过期时间
    ttl = redis_client.ttl('temp_key')
    print(f"Temp key TTL: {ttl}")

if __name__ == '__main__':
    main() 