import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { fileURLToPath, URL } from 'node:url'
import legacy from '@vitejs/plugin-legacy'
import { VitePWA } from 'vite-plugin-pwa'
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
  plugins: [
    vue(),
    legacy(),
    VitePWA({
      registerType: 'autoUpdate',
      manifest: {
        name: 'TV Mount',
        short_name: 'TV Mount',
        description: '专业的电视挂架解决方案',
        theme_color: '#4F46E5',
        icons: [
          {
            src: '/logo.svg',
            sizes: '120x40',
            type: 'image/svg+xml',
            purpose: 'any'
          }
        ]
      }
    })
  ],
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