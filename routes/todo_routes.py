from fastapi import APIRouter, Depends, status, HTTPException
from dto.todo_dto import TodoCreateRequestDto, TodoCreateResponseDto
from dependencies import get_todo_service
from service.todo_service import TodoService
from typing import List


# 创建路由实例，统一前缀和标签
router = APIRouter(prefix="/todos", tags=["todos"])  # 用于API文档分组


@router.post(
    "", response_model=TodoCreateResponseDto, status_code=status.HTTP_201_CREATED
)  # 创建成功返回201
def create_todo(
    todoRequest: TodoCreateRequestDto,
    todoService: TodoService = Depends(get_todo_service),
) -> TodoCreateResponseDto:
    # 注入服务
    """创建新的Todo任务"""
    # 调用服务层处理业务逻辑
    new_todo = todoService.create_todo(todoRequest)
    return new_todo


@router.get(
    "", response_model=List[TodoCreateResponseDto], status_code=status.HTTP_200_OK
)
def get_todo_list(
    todoService: TodoService = Depends(get_todo_service),
) -> List[TodoCreateResponseDto]:
    todolist = todoService.get_todolist()
    return todolist


# 通过URL路径参数传递ID（RESTful规范）
@router.delete("/{delete_id}", response_model=int, status_code=status.HTTP_200_OK)
def delete_todo(
    delete_id: int, todoService: TodoService = Depends(get_todo_service)
) -> int:
    deleted_id = todoService.delete_todo(delete_id)

    # 如果ID不存在，返回404错误
    if not deleted_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Todo with ID {delete_id} not found",
        )
    return deleted_id


# 路径参数：要修改的Todo ID（URL中体现资源）
@router.put("/{change_status_id}", response_model=int, status_code=status.HTTP_200_OK)
def change_status(
    change_status_id: int,
    completed: bool,
    todoService: TodoService = Depends(get_todo_service),
) -> int:
    change_status_id = todoService.change_status(change_status_id, completed)

    # 如果ID不存在，返回404错误
    if not change_status_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Todo with ID {change_status_id} not found",
        )
    return change_status_id
