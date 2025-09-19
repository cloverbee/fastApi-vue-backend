from pydantic import BaseModel
from typing import Optional  # 新增：导入Optional


class TodoCreateRequestDto(BaseModel):
    """创建任务时的请求体格式  创建Todo的请求DTO：客户端需要提供的字段"""

    title: str  # 任务标题（必传）
    completed: Optional[bool] = False  # 是否完成（可选，默认未完成）


class TodoCreateResponseDto(TodoCreateRequestDto):
    """返回任务时的格式（包含 ID）  创建Todo的响应DTO：返回给客户端的字段"""

    id: int  # 任务唯一标识


class ArchiveDto(BaseModel):
    id: int  # 存档唯一标识
    name: str  # 存档名称
    created_at: str  # 存档时间
    todos: list[TodoCreateResponseDto]  # 存档的任务列表


# class TodoCreateRequestDto(BaseModel):
#     """创建Todo的请求DTO：客户端需要提供的字段"""
#     desc: str  # 任务描述（id由系统自动生成，无需客户端提供）
#
# class TodoResponseDto(BaseModel):
#     """创建Todo的响应DTO：返回给客户端的字段"""
#     id: int
#     desc: str
#
#     class Config:
#         orm_mode = True  # 支持从ORM模型或dataclass直接转换
