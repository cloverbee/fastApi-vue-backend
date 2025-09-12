from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel  # 数据验证
from typing import List, Optional
from datetime import datetime
import uuid  # 用于生成唯一存档ID

# 1. 初始化 FastAPI 应用
app = FastAPI(title="TodoList API", version="1.0")

# 配置 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源（开发环境用，生产环境需指定具体域名）
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有 HTTP 方法
    allow_headers=["*"],  # 允许所有请求头
)

# 3. 定义数据模型（DTO：规范前后端数据交互格式）
class TodoCreate(BaseModel):
    """创建任务时的请求体格式"""
    title: str  # 任务标题（必传）
    completed: Optional[bool] = False  # 是否完成（可选，默认未完成）

class TodoResponse(TodoCreate):
    """返回任务时的格式（包含 ID）"""
    id: int  # 任务唯一标识

class Archive(BaseModel):
    id: str  # 存档唯一标识
    name: str  # 存档名称
    created_at: str  # 存档时间
    todos: list[TodoResponse]  # 存档的任务列表

# 4. 模拟数据库（实际项目中替换为真实数据库）
fake_db = []
next_id = 1  # 自增 ID

archives = []  # 存档列表（不可修改）


# 5. API 接口（核心业务逻辑）
@app.get("/todos", response_model=List[TodoResponse])
def get_all_todos():
    """获取所有任务"""
    return fake_db

@app.post("/todos", response_model=TodoResponse, status_code=201)
def create_todo(todo: TodoCreate):
    """创建新任务"""
    global next_id
    new_todo = {
        "id": next_id,
        "title": todo.title,
        "completed": todo.completed
    }
    fake_db.append(new_todo)
    next_id += 1
    return new_todo

@app.delete("/todos/{todo_id}", status_code=204)   # status_code什么意思？
def delete_todo(todo_id: int):
    """删除任务"""
    todelete = -1
    for index, node in enumerate(fake_db):
        if node["id"] == todo_id:
            todelete = index
            fake_db.pop(todelete)
            return
    raise HTTPException(status_code=404, detail=f"任务 ID {todo_id} 不存在")


@app.put("/todos/{todo_id}", response_model=TodoResponse, status_code=200)
def changeCompleteState(todo_id:int, completed:bool):
    for index, node in enumerate(fake_db):
        if node["id"] == todo_id:
            fake_db[index]["completed"] = completed
            return node
    raise HTTPException(status_code=404, detail=f"任务 ID {todo_id} 不存在")


@app.post("/archive", response_model=Archive, status_code=200)
def archiveCurrent(archive_name: str):
    global fake_db
    if not fake_db:
            raise HTTPException(status_code=400, detail="当前列表为空，无法存档")
    archive_id = str(uuid.uuid4())  # 先生成ID并保存
    newArchive = {
        "id": archive_id,  # 存档唯一标识
        "name": f"存档列表--{archive_name}" ,  # 存档名称
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # 存档时间
        "todos":  fake_db # 存档的任务列表
    }
    fake_db = []
    archives.append(newArchive)
    return newArchive

@app.get("/archives", status_code=200)
def getArchiveList():
    return archives

@app.delete("/archives/{archive_id}")
def deleteArchive(archive_id: str):
    for index, node in enumerate(archives):
        if node["id"] == archive_id:
            archives.pop(index)
            break

    return archive_id

