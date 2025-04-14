import { describe, it, expect, beforeEach } from 'vitest'
import { mount } from '@vue/test-utils'
import { createRouter, createWebHistory } from 'vue-router'
import { createPinia, setActivePinia } from 'pinia'
import App from '../App.vue'

// Create mock router
const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      component: { template: '<div>Home</div>' }
    },
    {
      path: '/site',
      component: { template: '<div>Site</div>' }
    },
    {
      path: '/cart',
      component: { template: '<div>Cart</div>' }
    },
    {
      path: '/notifications',
      component: { template: '<div>Notifications</div>' }
    },
    {
      path: '/tv-mount',
      component: { template: '<div>TV Mount</div>' }
    }
  ]
})

describe('App.vue', () => {
  beforeEach(() => {
    setActivePinia(createPinia())
  })

  it('renders properly', async () => {
    const wrapper = mount(App, {
      global: {
        plugins: [router, createPinia()]
      }
    })
    await router.isReady()
    expect(wrapper.exists()).toBe(true)
  })

  it('contains router-view', async () => {
    const wrapper = mount(App, {
      global: {
        plugins: [router, createPinia()]
      }
    })
    await router.isReady()
    expect(wrapper.find('router-view').exists()).toBe(true)
  })

  it('has correct class name', async () => {
    const wrapper = mount(App, {
      global: {
        plugins: [router, createPinia()]
      }
    })
    await router.isReady()
    expect(wrapper.classes()).toContain('app')
  })

  it('renders navigation links', async () => {
    const wrapper = mount(App, {
      global: {
        plugins: [router, createPinia()]
      }
    })
    await router.isReady()
    const navLinks = wrapper.findAll('nav a')
    expect(navLinks.length).toBeGreaterThan(0)
  })

  it('has proper layout structure', async () => {
    const wrapper = mount(App, {
      global: {
        plugins: [router, createPinia()]
      }
    })
    await router.isReady()
    expect(wrapper.find('header').exists()).toBe(true)
    expect(wrapper.find('main').exists()).toBe(true)
    expect(wrapper.find('footer').exists()).toBe(true)
  })
})
