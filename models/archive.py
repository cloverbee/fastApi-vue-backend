from dataclasses import dataclass
from .todo import Todo  # 若在同一models目录下，用相对导入


@dataclass
class Archive:
    """Archive业务实体：表示一个待办任务列表存档"""

    #     id: int       # 唯一标识
    #     title: str     # 任务描述
    #     completed: bool
    id: int  # 存档唯一标识
    name: str  # 存档名称
    created_at: str  # 存档时间
    todos: list[Todo]  # 存档的任务列表
