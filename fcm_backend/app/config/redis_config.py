REDIS_CONFIG = {
    'host': 'localhost',            # Redis服务器地址
    'port': 6379,                   # Redis服务器端口
    'db': 0,                        # 使用的Redis数据库序号，默认从0开始
    'password': None,               # 如果有密码，请设置
    'decode_responses': True,       # 是否自动解码返回结果（将字节转换为字符串）
    'socket_timeout': 5,            # 连接建立后，操作的读写超时时间（秒）
    'socket_connect_timeout': 5,    # 建立连接的超时时间（秒）
    'retry_on_timeout': True        # 在超时错误时，是否重试连接操作
}