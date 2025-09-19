from models.archive import Archive
from datetime import datetime
from service.todo_service import TodoService  # 导入TodoService
from typing import List


class ArchiveService:
    def __init__(self):
        self.archive_repository = {}
        self.curr_idx = 0

    def create_archive(self, todo_service: TodoService) -> Archive:
        # param todo_service: TodoService实例，用于获取当前任务列表
        new_id = self.curr_idx + 1
        self.curr_idx += 1

        new_archive = Archive(
            id=new_id,
            name=f"存档列表--{new_id}",
            created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            todos=todo_service.get_todolist(),
        )

        self.archive_repository[new_id] = new_archive

        # clear todolist
        todo_service.clear_todolist()

        return new_archive

    def get_archive(self) -> List[Archive]:
        return self.archive_repository.values()
