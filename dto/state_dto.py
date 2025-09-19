from pydantic import BaseModel


class ChangeStateRequestDto(BaseModel):
    todo_id: int
    completed: bool
