from typing import List, Optional
from models.todo import Todo
from dto.todo_dto import TodoCreateRequestDto


class TodoService:
    def __init__(self):
        self.todo_repository = {}
        self.curr_idx = 0

    def create_todo(self, requestDto: TodoCreateRequestDto) -> Todo:
        # self.todo_repository[self.curr_idx]
        # = Todo(todoCreateRequestDto.id, todoCreateRequestDto.desc)

        # 1. 生成新ID
        new_id = self.curr_idx + 1
        self.curr_idx += 1

        # 2. 创建Todo实体（业务模型）models
        new_todo = Todo(
            id=new_id, title=requestDto.title, completed=requestDto.completed
        )

        # 3. 存储到仓库
        self.todo_repository[new_id] = new_todo
        return new_todo

    def get_todolist(self) -> List[Todo]:
        return list(self.todo_repository.values())

    def clear_todolist(self) -> bool:
        self.todo_repository = {}
        return True

    def delete_todo(self, delete_id: int) -> Optional[int]:
        if not delete_id:
            return None
        else:
            # res = self.todo_repository[delete_id]
            del self.todo_repository[delete_id]
            return delete_id

    def change_status(self, change_status_id: int, new_status: bool) -> Optional[int]:
        if not change_status_id:
            return None
        else:
            self.todo_repository[change_status_id].completed = new_status
            return change_status_id


#   from typing import Dict
#   from app.models.todo import Todo
#   from app.dtos.todo_dtos import TodoCreateRequestDto
#
#   class TodoService:
#       def __init__(self):
#           self._repository: Dict[int, Todo] = {}  # 模拟数据库存储
#           self._next_id = 0  # 自增ID计数器
#
#       def create_todo(self, request_dto: TodoCreateRequestDto) -> Todo:
#           """
#           创建新的Todo任务
#           :param request_dto: 包含任务描述的请求DTO
#           :return: 创建成功的Todo实体
#           """
#           # 1. 生成新ID
#           new_id = self._next_id
#           self._next_id += 1
#
#           # 2. 创建Todo实体（业务模型）models
#           new_todo = Todo(id=new_id, desc=request_dto.desc)
#
#           # 3. 存储到仓库
#           self._repository[new_id] = new_todo
#
#           return new_todo

#         @app.post("/todos", response_model=TodoResponse,
#           status_code=201)
#         def create_todo(todo: TodoCreateRequestDto,
#           todo_service=Depends(get_todo_service)
#           -> TodoCreateResponseDto:
#             """创建新任务"""
#             global next_id
#             new_todo = {"id": next_id, "title": todo.title,
#             "completed": todo.completed}
#             todo_service.create()
#             todo_service.delete()
#             fake_db.append(new_todo)
#             next_id += 1
#             return new_todo

#     def update():
#         pass
#
#     def delete(self, id: int):
#         del self.todo_repository[id]
#
#     def get(self, id: int) -> Todo:
#         return self.todo_repository.get(id, None)
#
#     def get_all(self) -> List[Todo]:
#         pass
