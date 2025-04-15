# FCM Backend API

一个基于 FastAPI 构建的 Firebase Cloud Messaging (FCM) 后端服务，提供消息推送、用户管理和计费功能。

## 功能特点

- 🔥 Firebase Cloud Messaging 集成
- 👤 用户认证和授权
- 💰 灵活的计费系统
- 📊 API 使用统计和限制
- 🔒 安全的 API 访问控制
- 🚀 高性能的消息推送
- 📱 多平台支持

## 技术栈

- Python 3.8+
- FastAPI
- Firebase Admin SDK
- Redis
- Pydantic
- Uvicorn

## 项目结构

```
fcm_backend/
├── app/
│   ├── api/
│   │   └── v1/
│   │       └── endpoints/
│   │           ├── auth.py
│   │           ├── billing.py
│   │           ├── fcm.py
│   │           └── users.py
│   ├── core/
│   │   ├── config/
│   │   │   └── settings.py
│   │   └── security.py
│   ├── models/
│   │   └── user.py
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── billing_service.py
│   │   ├── fcm_service.py
│   │   └── user_service.py
│   └── utils/
│       └── redis/
│           └── client.py
├── tests/
│   ├── api/
│   ├── services/
│   └── utils/
├── .env.example
├── requirements.txt
└── README.md
```

## 快速开始

### 1. 环境要求

- Python 3.8+
- Redis 服务器
- Firebase 项目

### 2. 安装

```bash
# 克隆项目
git clone https://github.com/yourusername/fcm_backend.git
cd fcm_backend

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
.\venv\Scripts\activate  # Windows

# 安装依赖
pip install -r requirements.txt
```

### 3. 配置

1. 复制 `.env.example` 为 `.env`：
```bash
cp .env.example .env
```

2. 配置环境变量：
```env
# 项目设置
PROJECT_NAME=FCM Backend
API_V1_STR=/api/v1
DEBUG=True

# 安全设置
SECRET_KEY=your-secret-key
ACCESS_TOKEN_EXPIRE_MINUTES=11520  # 8 days

# Firebase 设置
FIREBASE_PROJECT_ID=your-project-id
FIREBASE_PRIVATE_KEY=your-private-key
FIREBASE_CLIENT_EMAIL=your-client-email
FIREBASE_PRIVATE_KEY_ID=your-private-key-id
FIREBASE_CLIENT_ID=your-client-id
FIREBASE_AUTH_URI=https://accounts.google.com/o/oauth2/auth
FIREBASE_TOKEN_URI=https://oauth2.googleapis.com/token
FIREBASE_AUTH_PROVIDER_X509_CERT_URL=https://www.googleapis.com/oauth2/v1/certs
FIREBASE_CLIENT_X509_CERT_URL=your-client-x509-cert-url

# Redis 设置
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0
REDIS_PASSWORD=your-redis-password
```

### 4. 运行

```bash
# 启动开发服务器
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

访问 http://localhost:8000/docs 查看 API 文档。

## API 文档

### 认证

- `POST /api/v1/auth/login` - 用户登录
- `POST /api/v1/auth/register` - 用户注册
- `POST /api/v1/auth/refresh` - 刷新访问令牌

### FCM 消息

- `POST /api/v1/fcm/send` - 发送单设备消息
- `POST /api/v1/fcm/send-multicast` - 发送多设备消息

### 用户管理

- `GET /api/v1/users/me` - 获取当前用户信息
- `PUT /api/v1/users/me` - 更新用户信息
- `GET /api/v1/users/{user_id}` - 获取指定用户信息

### 计费

- `GET /api/v1/billing/usage` - 获取 API 使用情况
- `GET /api/v1/billing/usage-history` - 获取使用历史
- `GET /api/v1/billing/subscription` - 获取订阅信息
- `POST /api/v1/billing/upgrade` - 升级订阅
- `POST /api/v1/billing/cancel` - 取消订阅

## 计费系统

系统提供三种订阅等级：

1. **免费版**
   - 每日限制：100 次 API 调用
   - 每月限制：3000 次 API 调用
   - 价格：免费

2. **基础版**
   - 每日限制：1000 次 API 调用
   - 每月限制：30000 次 API 调用
   - 价格：$9.99/月

3. **高级版**
   - 每日限制：10000 次 API 调用
   - 每月限制：300000 次 API 调用
   - 价格：$29.99/月

## 开发指南

### 添加新功能

1. 在 `app/api/v1/endpoints/` 创建新的路由文件
2. 在 `app/services/` 创建对应的服务类
3. 在 `app/models/` 添加必要的数据模型
4. 编写单元测试

### 测试

```bash
# 运行所有测试
pytest

# 运行特定测试
pytest tests/api/test_fcm.py
```

## 贡献指南

1. Fork 项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 联系方式

- 项目维护者：[Your Name]
- 邮箱：[your.email@example.com]
- 项目链接：[https://github.com/yourusername/fcm_backend](https://github.com/yourusername/fcm_backend)

## 致谢

- [FastAPI](https://fastapi.tiangolo.com/)
- [Firebase Admin SDK](https://firebase.google.com/docs/admin/setup)
- [Redis](https://redis.io/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
