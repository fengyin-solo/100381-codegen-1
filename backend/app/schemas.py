"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class CanalEntry(BaseModel):
    """干渠明细结构。"""

    field_0: str | None = None  # 渠道编号
    field_1: str | None = None  # 渠道名称
    field_2: str | None = None  # 设计流量
    field_3: str | None = None  # 渠道长度
    field_4: str | None = None  # 衬砌形式
    field_5: str | None = None  # 管理所
    field_6: str | None = None  # 上次清淤日
    field_7: str | None = None  # 渠道状态

class BranchEntry(BaseModel):
    """支渠明细结构。"""

    field_0: str | None = None  # 支渠编号
    field_1: str | None = None  # 所属干渠
    field_2: str | None = None  # 设计流量
    field_3: str | None = None  # 控制面积
    field_4: str | None = None  # 灌溉村组
    field_5: str | None = None  # 上次巡护日
    field_6: str | None = None  # 分水口数
    field_7: str | None = None  # 支渠状态

class GateEntry(BaseModel):
    """节制闸明细结构。"""

    field_0: str | None = None  # 闸门编号
    field_1: str | None = None  # 所在渠道
    field_2: str | None = None  # 闸门型式
    field_3: str | None = None  # 孔口尺寸
    field_4: str | None = None  # 启闭方式
    field_5: str | None = None  # 管理所
    field_6: str | None = None  # 上次保养日
    field_7: str | None = None  # 闸门状态

class PumpEntry(BaseModel):
    """泵站明细结构。"""

    field_0: str | None = None  # 泵站编号
    field_1: str | None = None  # 装机台数
    field_2: str | None = None  # 设计扬程
    field_3: str | None = None  # 配套功率
    field_4: str | None = None  # 管理所
    field_5: str | None = None  # 上次检修日
    field_6: str | None = None  # 运行台数
    field_7: str | None = None  # 泵站状态

class PlanEntry(BaseModel):
    """灌溉计划明细结构。"""

    field_0: str | None = None  # 计划编号
    field_1: str | None = None  # 灌溉季度
    field_2: str | None = None  # 计划面积
    field_3: str | None = None  # 计划水量
    field_4: str | None = None  # 计划起止日
    field_5: str | None = None  # 编制单位
    field_6: str | None = None  # 审批人
    field_7: str | None = None  # 计划状态

class RequestEntry(BaseModel):
    """用水申请单明细结构。"""

    field_0: str | None = None  # 申请单号
    field_1: str | None = None  # 申请村组
    field_2: str | None = None  # 申请面积
    field_3: str | None = None  # 申请水量
    field_4: str | None = None  # 期望引水日
    field_5: str | None = None  # 申请人
    field_6: str | None = None  # 联系电话
    field_7: str | None = None  # 申请状态

class AllocationEntry(BaseModel):
    """配水方案明细结构。"""

    field_0: str | None = None  # 方案编号
    field_1: str | None = None  # 关联计划
    field_2: str | None = None  # 轮次编号
    field_3: str | None = None  # 分配流量
    field_4: str | None = None  # 分配水量
    field_5: str | None = None  # 分水时段
    field_6: str | None = None  # 调度员
    field_7: str | None = None  # 方案状态

class MeteringEntry(BaseModel):
    """水量计量记录明细结构。"""

    field_0: str | None = None  # 计量编号
    field_1: str | None = None  # 计量点位
    field_2: str | None = None  # 计量方式
    field_3: str | None = None  # 累计水量
    field_4: str | None = None  # 瞬时流量
    field_5: str | None = None  # 计量日期
    field_6: str | None = None  # 计量员
    field_7: str | None = None  # 计量状态

class SeepageEntry(BaseModel):
    """渗漏监测记录明细结构。"""

    field_0: str | None = None  # 监测编号
    field_1: str | None = None  # 监测断面
    field_2: str | None = None  # 渠道桩号
    field_3: str | None = None  # 渗漏量
    field_4: str | None = None  # 渗漏系数
    field_5: str | None = None  # 监测日期
    field_6: str | None = None  # 监测人
    field_7: str | None = None  # 监测状态

class SoilEntry(BaseModel):
    """墒情监测记录明细结构。"""

    field_0: str | None = None  # 监测编号
    field_1: str | None = None  # 监测点位
    field_2: str | None = None  # 土壤含水率
    field_3: str | None = None  # 埋设深度
    field_4: str | None = None  # 作物名称
    field_5: str | None = None  # 监测日期
    field_6: str | None = None  # 监测人
    field_7: str | None = None  # 墒情状态

class CropwaterEntry(BaseModel):
    """作物需水记录明细结构。"""

    field_0: str | None = None  # 需水编号
    field_1: str | None = None  # 作物名称
    field_2: str | None = None  # 生育期
    field_3: str | None = None  # 需水强度
    field_4: str | None = None  # 灌溉定额
    field_5: str | None = None  # 测算日期
    field_6: str | None = None  # 技术员
    field_7: str | None = None  # 需水状态

class RotationEntry(BaseModel):
    """灌溉轮次明细结构。"""

    field_0: str | None = None  # 轮次编号
    field_1: str | None = None  # 所属计划
    field_2: str | None = None  # 轮次序号
    field_3: str | None = None  # 轮灌组数
    field_4: str | None = None  # 轮灌周期
    field_5: str | None = None  # 开始日期
    field_6: str | None = None  # 调度员
    field_7: str | None = None  # 轮次状态

class WaterfeeEntry(BaseModel):
    """水费计收单明细结构。"""

    field_0: str | None = None  # 计费单号
    field_1: str | None = None  # 用水村组
    field_2: str | None = None  # 计量水量
    field_3: str | None = None  # 计费单价
    field_4: str | None = None  # 应收水费
    field_5: str | None = None  # 实收水费
    field_6: str | None = None  # 收费日期
    field_7: str | None = None  # 计费状态

class DredgeEntry(BaseModel):
    """渠道清淤单明细结构。"""

    field_0: str | None = None  # 清淤编号
    field_1: str | None = None  # 渠道桩号
    field_2: str | None = None  # 淤积厚度
    field_3: str | None = None  # 清淤方式
    field_4: str | None = None  # 施工班组
    field_5: str | None = None  # 计划工期
    field_6: str | None = None  # 完成日期
    field_7: str | None = None  # 清淤状态

class DangerEntry(BaseModel):
    """险工险段明细结构。"""

    field_0: str | None = None  # 险段编号
    field_1: str | None = None  # 渠道桩号
    field_2: str | None = None  # 险情类型
    field_3: str | None = None  # 险情等级
    field_4: str | None = None  # 发现日期
    field_5: str | None = None  # 巡查人
    field_6: str | None = None  # 处置措施
    field_7: str | None = None  # 险段状态

class WateruserEntry(BaseModel):
    """灌区用户明细结构。"""

    field_0: str | None = None  # 用户编号
    field_1: str | None = None  # 用户名称
    field_2: str | None = None  # 所属村组
    field_3: str | None = None  # 灌溉面积
    field_4: str | None = None  # 种植结构
    field_5: str | None = None  # 联系人
    field_6: str | None = None  # 联系电话
    field_7: str | None = None  # 用户状态

class PatrolEntry(BaseModel):
    """渠道巡护单明细结构。"""

    field_0: str | None = None  # 巡护单号
    field_1: str | None = None  # 巡护区段
    field_2: str | None = None  # 巡护人员
    field_3: str | None = None  # 巡护日期
    field_4: str | None = None  # 发现问题数
    field_5: str | None = None  # 整改项数
    field_6: str | None = None  # 巡护时长
    field_7: str | None = None  # 巡护状态

class FloodEntry(BaseModel):
    """渠道防汛响应明细结构。"""

    field_0: str | None = None  # 防汛编号
    field_1: str | None = None  # 所在渠道
    field_2: str | None = None  # 汛期等级
    field_3: str | None = None  # 防汛物资数
    field_4: str | None = None  # 值守班组
    field_5: str | None = None  # 值班电话
    field_6: str | None = None  # 响应措施
    field_7: str | None = None  # 防汛状态
