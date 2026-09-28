# 灌区灌溉调度平台

面向干渠支渠输配水调度、闸门泵站运行、灌溉计划轮次编排与水费计收的一体化灌区管理后台。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 干渠 | `canal` | 干渠 | 渠道编号、渠道名称、设计流量 |
| 支渠 | `branch` | 支渠 | 支渠编号、所属干渠、设计流量 |
| 节制闸 | `gate` | 节制闸 | 闸门编号、所在渠道、闸门型式 |
| 泵站 | `pump` | 泵站 | 泵站编号、装机台数、设计扬程 |
| 灌溉计划 | `plan` | 灌溉计划 | 计划编号、灌溉季度、计划面积 |
| 用水申请 | `request` | 用水申请单 | 申请单号、申请村组、申请面积 |
| 配水方案 | `allocation` | 配水方案 | 方案编号、关联计划、轮次编号 |
| 水量计量 | `metering` | 水量计量记录 | 计量编号、计量点位、计量方式 |
| 渗漏监测 | `seepage` | 渗漏监测记录 | 监测编号、监测断面、渠道桩号 |
| 墒情监测 | `soil` | 墒情监测记录 | 监测编号、监测点位、土壤含水率 |
| 作物需水 | `cropwater` | 作物需水记录 | 需水编号、作物名称、生育期 |
| 灌溉轮次 | `rotation` | 灌溉轮次 | 轮次编号、所属计划、轮次序号 |
| 水费计收 | `waterfee` | 水费计收单 | 计费单号、用水村组、计量水量 |
| 渠道清淤 | `dredge` | 渠道清淤单 | 清淤编号、渠道桩号、淤积厚度 |
| 险工险段 | `danger` | 险工险段 | 险段编号、渠道桩号、险情类型 |
| 灌区用户 | `wateruser` | 灌区用户 | 用户编号、用户名称、所属村组 |
| 渠道巡护 | `patrol` | 渠道巡护单 | 巡护单号、巡护区段、巡护人员 |
| 渠道防汛 | `flood` | 渠道防汛响应 | 防汛编号、所在渠道、汛期等级 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。
