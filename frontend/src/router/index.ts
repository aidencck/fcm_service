import { createRouter, createWebHistory } from 'vue-router'
import type { RouteRecordRaw } from 'vue-router'

const routes: RouteRecordRaw[] = [
  {
    path: '/login',
    name: 'Login',
    component: () => import('../pages/Login.vue')
  },
  {
    path: '/',
    name: 'Home',
    component: () => import('../pages/Home.vue')
  },
  {
    path: '/site',
    name: 'Site',
    component: () => import('../pages/Site.vue')
  },
  {
    path: '/cart',
    name: 'Cart',
    component: () => import('../pages/Cart.vue')
  },
  {
    path: '/notifications',
    name: 'Notifications',
    component: () => import('../pages/Notifications.vue')
  },
  {
    path: '/notifications/:id',
    name: 'NotificationDetail',
    component: () => import('../pages/NotificationDetail.vue')
  },
  {
    path: '/account',
    name: 'Account',
    component: () => import('../pages/Account.vue')
  },
  {
    path: '/account/edit-profile',
    name: 'EditProfile',
    component: () => import('../pages/account/EditProfile.vue')
  },
  {
    path: '/account/change-password',
    name: 'ChangePassword',
    component: () => import('../pages/account/ChangePassword.vue')
  },
  {
    path: '/account/two-factor-auth',
    name: 'TwoFactorAuth',
    component: () => import('../pages/account/TwoFactorAuth.vue')
  },
  {
    path: '/account/devices',
    name: 'Devices',
    component: () => import('../pages/account/Devices.vue')
  },
  {
    path: '/account/privacy',
    name: 'PrivacySettings',
    component: () => import('../pages/account/PrivacySettings.vue')
  },
  {
    path: '/account/notifications',
    name: 'NotificationSettings',
    component: () => import('../pages/account/NotificationSettings.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router 