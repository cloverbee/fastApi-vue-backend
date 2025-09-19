from dataclasses import dataclass


@dataclass
class Todo:
    """Todo业务实体：表示一个待办任务"""

    id: int  # 唯一标识
    title: str  # 任务描述
    completed: bool
