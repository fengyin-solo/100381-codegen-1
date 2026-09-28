"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import canal as router_canal
from app.routers import branch as router_branch
from app.routers import gate as router_gate
from app.routers import pump as router_pump
from app.routers import plan as router_plan
from app.routers import request as router_request
from app.routers import allocation as router_allocation
from app.routers import metering as router_metering
from app.routers import seepage as router_seepage
from app.routers import soil as router_soil
from app.routers import cropwater as router_cropwater
from app.routers import rotation as router_rotation
from app.routers import waterfee as router_waterfee
from app.routers import dredge as router_dredge
from app.routers import danger as router_danger
from app.routers import wateruser as router_wateruser
from app.routers import patrol as router_patrol
from app.routers import flood as router_flood

ROUTERS = [router_canal, router_branch, router_gate, router_pump, router_plan, router_request, router_allocation, router_metering, router_seepage, router_soil, router_cropwater, router_rotation, router_waterfee, router_dredge, router_danger, router_wateruser, router_patrol, router_flood]
