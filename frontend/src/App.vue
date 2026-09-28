<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">灌区灌溉调度平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">面向干渠支渠输配水调度、闸门泵站运行、灌溉计划轮次编排与水费计收的一体化灌区管理后台。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "干渠", path: "/canal" }, { label: "支渠", path: "/branch" }, { label: "节制闸", path: "/gate" }, { label: "泵站", path: "/pump" }, { label: "灌溉计划", path: "/plan" }, { label: "用水申请", path: "/request" }, { label: "配水方案", path: "/allocation" }, { label: "水量计量", path: "/metering" }, { label: "渗漏监测", path: "/seepage" }, { label: "墒情监测", path: "/soil" }, { label: "作物需水", path: "/cropwater" }, { label: "灌溉轮次", path: "/rotation" }, { label: "水费计收", path: "/waterfee" }, { label: "渠道清淤", path: "/dredge" }, { label: "险工险段", path: "/danger" }, { label: "灌区用户", path: "/wateruser" }, { label: "渠道巡护", path: "/patrol" }, { label: "渠道防汛", path: "/flood" }]
</script>
