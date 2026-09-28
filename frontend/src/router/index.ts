import { createRouter, createWebHistory } from 'vue-router'

import Dashboard from '@/views/Dashboard.vue'
const Canal = () => import('@/views/canal/index.vue')
const Branch = () => import('@/views/branch/index.vue')
const Gate = () => import('@/views/gate/index.vue')
const Pump = () => import('@/views/pump/index.vue')
const Plan = () => import('@/views/plan/index.vue')
const Request = () => import('@/views/request/index.vue')
const Allocation = () => import('@/views/allocation/index.vue')
const Metering = () => import('@/views/metering/index.vue')
const Seepage = () => import('@/views/seepage/index.vue')
const Soil = () => import('@/views/soil/index.vue')
const Cropwater = () => import('@/views/cropwater/index.vue')
const Rotation = () => import('@/views/rotation/index.vue')
const Waterfee = () => import('@/views/waterfee/index.vue')
const Dredge = () => import('@/views/dredge/index.vue')
const Danger = () => import('@/views/danger/index.vue')
const Wateruser = () => import('@/views/wateruser/index.vue')
const Patrol = () => import('@/views/patrol/index.vue')
const Flood = () => import('@/views/flood/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'dashboard', component: Dashboard },
    { path: '/canal', name: 'canal', component: Canal },
    { path: '/branch', name: 'branch', component: Branch },
    { path: '/gate', name: 'gate', component: Gate },
    { path: '/pump', name: 'pump', component: Pump },
    { path: '/plan', name: 'plan', component: Plan },
    { path: '/request', name: 'request', component: Request },
    { path: '/allocation', name: 'allocation', component: Allocation },
    { path: '/metering', name: 'metering', component: Metering },
    { path: '/seepage', name: 'seepage', component: Seepage },
    { path: '/soil', name: 'soil', component: Soil },
    { path: '/cropwater', name: 'cropwater', component: Cropwater },
    { path: '/rotation', name: 'rotation', component: Rotation },
    { path: '/waterfee', name: 'waterfee', component: Waterfee },
    { path: '/dredge', name: 'dredge', component: Dredge },
    { path: '/danger', name: 'danger', component: Danger },
    { path: '/wateruser', name: 'wateruser', component: Wateruser },
    { path: '/patrol', name: 'patrol', component: Patrol },
    { path: '/flood', name: 'flood', component: Flood },
  ],
})

export default router
