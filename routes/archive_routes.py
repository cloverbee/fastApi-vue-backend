from fastapi import APIRouter, Depends, status
from dto.todo_dto import ArchiveDto
from dependencies import get_todo_service, get_archive_service
from service.todo_service import TodoService
from service.archive_service import ArchiveService
from typing import List


# 创建路由实例，统一前缀和标签
router = APIRouter(prefix="/archive", tags=["archive"])  # 用于API文档分组


@router.post("", response_model=ArchiveDto, status_code=status.HTTP_201_CREATED)
def create_Archive(
    archiveService: ArchiveService = Depends(get_archive_service),
    todoService: TodoService = Depends(get_todo_service),
) -> ArchiveDto:
    new_archive = archiveService.create_archive(todoService)
    return new_archive


@router.get("", response_model=List[ArchiveDto], status_code=status.HTTP_200_OK)
def archive_list(
    archiveService: ArchiveService = Depends(get_archive_service),
) -> List[ArchiveDto]:
    archive_list = archiveService.get_archive()
    return archive_list
