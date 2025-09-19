from service.archive_service import ArchiveService
from service.todo_service import TodoService

# 关键修复：创建全局单例服务实例（所有请求共享）
todo_service_singleton = TodoService()
archive_service_singleton = ArchiveService()


def get_todo_service() -> TodoService:
    """依赖注入函数：提供TodoService实例"""
    # 返回单例实例，而非每次创建新实例
    return todo_service_singleton


def get_archive_service() -> ArchiveService:
    return archive_service_singleton
