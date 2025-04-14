import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { fileURLToPath, URL } from 'node:url'
/**
 * 该配置文件包含以下配置项：
 * 1. plugins: [vue()]  // 使用 Vue 插件
 * 2. resolve.alias: 将 '@' 别名映射到项目 src 目录
 * 3. server.port: 开发服务器的端口，当前为 3000
 */
function listConfigItems() {
  return {
    plugins: ['vue()'],
    resolve: {
      alias: {
        '@': './src'
      }
    },
    server: {
      port: 3000
    }
  }
}

console.log('Vite 配置项汇总：', listConfigItems())

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: {
    port: 3000,
    proxy: {
      '/api': {
        target: 'http://localhost:8080',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, '')
      }
    }
  },
  build: {
    target: 'esnext',
    minify: 'terser',
    terserOptions: {
      compress: {
        drop_console: true,
        drop_debugger: true
      }
    },
    rollupOptions: {
      output: {
        manualChunks: {
          'vue-vendor': ['vue', 'vue-router', 'pinia'],
          'ui-vendor': ['axios']
        }
      }
    }
  },
  test: {
    globals: true,
    environment: 'jsdom',
    coverage: {
      provider: 'v8',
      reporter: ['text', 'json', 'html']
    }
  }
}) 