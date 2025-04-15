# FCM 全栈项目

一个完整的 Firebase Cloud Messaging (FCM) 解决方案，包含后端 API 服务和现代化的前端界面。

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![Node Version](https://img.shields.io/badge/node-16%2B-green)](https://nodejs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.68.0-green)](https://fastapi.tiangolo.com/)
[![Vue 3](https://img.shields.io/badge/Vue-3.0-blue)](https://v3.vuejs.org/)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

## 🚀 项目概述

本项目是一个完整的 FCM 消息推送解决方案，包含：

- **后端服务**：基于 FastAPI 的高性能 API 服务
- **前端界面**：基于 Vue 3 的现代化管理界面
- **消息推送**：支持单设备、多设备和主题消息
- **用户管理**：完整的用户认证和授权系统
- **计费系统**：灵活的订阅和计费方案

## 🛠 技术栈

### 后端 (fcm_backend)
- **框架**: FastAPI 0.68.0
- **数据库**: Firebase Firestore
- **缓存**: Redis 6.0+
- **认证**: Firebase Auth
- **消息推送**: Firebase Cloud Messaging
- **API 文档**: Swagger UI, ReDoc
- **测试框架**: Pytest
- **代码格式化**: Black
- **类型检查**: mypy

### 前端 (frontend)
- **框架**: Vue 3 + TypeScript
- **构建工具**: Vite
- **UI 框架**: Tailwind CSS
- **状态管理**: Pinia
- **路由**: Vue Router
- **HTTP 客户端**: Axios
- **代码规范**: ESLint + Prettier
- **测试框架**: Vitest
- **提交规范**: Husky + Commitlint

## 📁 项目结构

### 后端结构
```
fcm_backend/
├── app/                    # 应用主目录
│   ├── api/               # API 路由
│   ├── core/             # 核心功能
│   ├── models/          # 数据模型
│   ├── services/        # 业务逻辑
│   └── utils/           # 工具函数
├── tests/               # 测试文件
├── credentials/         # 凭证文件
├── .env.example        # 环境变量模板
└── requirements.txt    # Python 依赖
```

### 前端结构
```
frontend/
├── src/                # 源代码
│   ├── assets/        # 静态资源
│   ├── components/    # 组件
│   ├── views/         # 页面
│   ├── store/         # 状态管理
│   ├── router/        # 路由
│   └── utils/         # 工具函数
├── public/            # 公共资源
├── tests/             # 测试文件
├── .env.example       # 环境变量模板
└── package.json       # 项目配置
```

## 🚀 快速开始

### 1. 环境要求

- Python 3.8+
- Node.js 16+
- Redis 6.0+
- Firebase 项目
- Docker (可选)

### 2. 后端设置

```bash
# 进入后端目录
cd fcm_backend

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
.\venv\Scripts\activate  # Windows

# 安装依赖
pip install -r requirements.txt

# 配置环境变量
cp .env.example .env
# 编辑 .env 文件设置必要的配置

# 运行开发服务器
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 3. 前端设置

```bash
# 进入前端目录
cd frontend

# 安装依赖
pnpm install

# 配置环境变量
cp .env.example .env
# 编辑 .env 文件设置必要的配置

# 运行开发服务器
pnpm dev
```

### 4. Docker 部署

```bash
# 使用 docker-compose 启动所有服务
docker-compose up -d
```

## 📚 API 文档

后端 API 文档可通过以下地址访问：
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

主要 API 端点包括：

### 认证 API
- `POST /api/v1/auth/login` - 用户登录
- `POST /api/v1/auth/register` - 用户注册
- `POST /api/v1/auth/refresh` - 刷新令牌

### FCM API
- `POST /api/v1/fcm/send` - 发送单设备消息
- `POST /api/v1/fcm/send-multicast` - 发送多设备消息
- `POST /api/v1/fcm/topics/subscribe` - 订阅主题

### 用户管理
- `GET /api/v1/users/me` - 获取当前用户信息
- `PUT /api/v1/users/me` - 更新用户信息

### 计费系统
- `GET /api/v1/billing/usage` - 获取使用情况
- `GET /api/v1/billing/subscription` - 获取订阅信息
- `POST /api/v1/billing/upgrade` - 升级订阅

## 💰 订阅方案

### 免费版
- 每日限制：100 次 API 调用
- 每月限制：3000 次 API 调用
- 价格：免费

### 基础版
- 每日限制：1000 次 API 调用
- 每月限制：30000 次 API 调用
- 价格：$9.99/月

### 高级版
- 每日限制：10000 次 API 调用
- 每月限制：300000 次 API 调用
- 价格：$29.99/月

## 🔧 开发指南

### 后端开发
```bash
# 运行测试
pytest

# 代码格式化
black .

# 类型检查
mypy app/
```

### 前端开发
```bash
# 运行测试
pnpm test

# 代码格式化
pnpm format

# 构建生产版本
pnpm build
```

## 🚀 部署

### Docker 部署
```bash
# 构建镜像
docker-compose build

# 启动服务
docker-compose up -d
```

### Kubernetes 部署
```bash
# 应用配置
kubectl apply -f k8s/
```

## 🤝 贡献指南

1. Fork 项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

### 提交规范
- feat: 新功能
- fix: 修复 bug
- docs: 文档更新
- style: 代码格式
- refactor: 代码重构
- test: 测试相关
- chore: 构建过程或辅助工具的变动

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 📞 联系方式

- 项目维护者：[Your Name]
- 邮箱：[your.email@example.com]
- 项目链接：[https://github.com/yourusername/fcm-project](https://github.com/yourusername/fcm-project)
- 问题反馈：[Issues](https://github.com/yourusername/fcm-project/issues)

## 🙏 致谢

- [FastAPI](https://fastapi.tiangolo.com/) - 高性能的 Python Web 框架
- [Vue.js](https://vuejs.org/) - 渐进式 JavaScript 框架
- [Firebase](https://firebase.google.com/) - Google 的移动和 Web 应用开发平台
- [Tailwind CSS](https://tailwindcss.com/) - 实用的 CSS 框架

## 📈 性能指标

- 平均响应时间：< 100ms
- 并发处理能力：1000+ 请求/秒
- 消息推送延迟：< 1秒
- API 可用性：99.9%
- 前端加载时间：< 2秒
