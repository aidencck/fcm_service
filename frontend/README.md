# Frontend Project

## 项目概述
这是一个基于现代前端技术栈构建的 Web 应用项目，使用 Docker 容器化部署方案，支持开发和生产环境。

## 技术栈
- **前端框架**: Vue 3
- **构建工具**: Vite
- **包管理器**: pnpm
- **样式处理**: Tailwind CSS
- **代码规范**: ESLint + Prettier
- **测试框架**: Vitest
- **容器化**: Docker + Docker Compose
- **Web 服务器**: Nginx (生产环境)

## 项目结构
```
frontend/
├── src/                # 源代码目录
├── public/             # 静态资源
├── node_modules/       # 依赖包
├── dist/               # 构建输出目录
├── Dockerfile          # 生产环境 Docker 配置
├── Dockerfile.dev      # 开发环境 Docker 配置
├── docker-compose.yml  # Docker Compose 配置
├── .env.example        # 环境变量示例
└── package.json        # 项目配置
```

## 环境要求
- Node.js 18+
- pnpm 8+
- Docker 20+
- Docker Compose 2+

## 快速开始

### 本地开发（不使用 Docker）
```bash
# 安装依赖
pnpm install

# 启动开发服务器
pnpm dev
```

### 使用 Docker 开发
```bash
# 启动开发环境
docker-compose up frontend-dev

# 访问开发服务器
http://localhost:5173
```

### 生产环境部署
```bash
# 构建生产镜像
docker build -t frontend-prod .

# 运行生产容器
docker-compose up frontend

# 访问生产环境
http://localhost:80
```

## 环境变量配置
复制 `.env.example` 文件为 `.env`，并根据需要修改以下变量：
```
VITE_API_URL=http://api.example.com
VITE_APP_TITLE=My App
```

## 开发指南

### 代码规范
- 使用 ESLint 进行代码检查
- 使用 Prettier 进行代码格式化
- 提交代码前运行 `pnpm lint` 和 `pnpm format`

### 测试
```bash
# 运行测试
pnpm test

# 运行测试并查看覆盖率
pnpm test:coverage
```

### 构建
```bash
# 构建生产版本
pnpm build
```

## Docker 部署说明

### 开发环境
- 使用 `Dockerfile.dev` 配置
- 支持热重载
- 源代码通过 volume 挂载
- 访问地址：http://localhost:5173

### 生产环境
- 使用 `Dockerfile` 配置
- 多阶段构建优化镜像大小
- 使用 Nginx 作为静态文件服务器
- 访问地址：http://localhost:80

## 常见问题

### 开发环境问题
1. 如果遇到端口冲突，可以在 `docker-compose.yml` 中修改端口映射
2. 如果依赖安装失败，尝试清理缓存后重新安装：
   ```bash
   pnpm store prune
   pnpm install
   ```

### 生产环境问题
1. 确保环境变量正确配置
2. 检查 Nginx 配置是否正确
3. 确保构建过程没有错误

## 贡献指南
1. Fork 项目
2. 创建特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 创建 Pull Request

## 许可证
[MIT License](LICENSE)
