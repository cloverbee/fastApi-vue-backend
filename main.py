from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from pydantic import BaseModel  # 数据验证
# from typing import List, Optional
# from datetime import datetime
# import uuid  # 用于生成唯一存档ID
# from fastapi import Depends
from routes.todo_routes import router as todo_router
from routes.archive_routes import router as archive_router

# 1. 初始化 FastAPI 应用
app = FastAPI(
    title="Todo API",
    version="1.0",
    description="一个按分层架构设计的Todo应用",
)

# 注册路由
app.include_router(todo_router)
app.include_router(archive_router)

# 配置 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源（开发环境用，生产环境需指定具体域名）
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有 HTTP 方法
    allow_headers=["*"],  # 允许所有请求头
)


# 根路径测试
@app.get("/")
def read_root():
    return {"message": "Todo API 运行中"}


# def get_todo_service():
#     return TodoService()
#
#
# # 4. 模拟数据库（实际项目中替换为真实数据库）
# fake_db = []
# next_id = 1  # 自增 ID
#
# archives = []  # 存档列表（不可修改）
#
#
# # 5. API 接口（核心业务逻辑）
# @app.get("/todos", response_model=List[TodoResponse])
# def get_all_todos():
#     """获取所有任务"""
#     return fake_db
#
#
#
#
#
# @app.delete("/todos/{todo_id}", status_code=204)  # status_code什么意思？
# def delete_todo(todo_id: int):
#     """删除任务"""
#     todelete = -1
#     for index, node in enumerate(fake_db):
#         if node["id"] == todo_id:
#             todelete = index
#             fake_db.pop(todelete)
#             return
#     raise HTTPException(status_code=404, detail=f"任务 ID {todo_id} 不存在")
#
#
# @app.put("/todos/{todo_id}", response_model=TodoResponse, status_code=200)
# def changeCompleteState(changeStateRequestDto: ChangeStateRequestDto):
#     for index, node in enumerate(fake_db):
#         if node["id"] == changeStateRequestDto.todo_id:
#             fake_db[index]["completed"] = changeStateRequestDto.completed
#             return node
#     raise HTTPException(status_code=404, detail=f"任务 ID {todo_id} 不存在")
#
#
# @app.post("/archive", response_model=Archive, status_code=200)
# def archiveCurrent(archive_name: str):
#     global fake_db
#     if not fake_db:
#         raise HTTPException(status_code=400, detail="当前列表为空，无法存档")
#     archive_id = str(uuid.uuid4())  # 先生成ID并保存
#     newArchive = {
#         "id": archive_id,  # 存档唯一标识
#         "name": f"存档列表--{archive_name}",  # 存档名称
#         "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # 存档时间
#         "todos": fake_db,  # 存档的任务列表
#     }
#     fake_db = []
#     archives.append(newArchive)
#     return newArchive
#
#
# @app.get("/archives", status_code=200)
# def getArchiveList():
#     return archives
#
#
# @app.delete("/archives/{archive_id}")
# def deleteArchive(archive_id: str):
#     for index, node in enumerate(archives):
#         if node["id"] == archive_id:
#             archives.pop(index)
#             break
#
#     return archive_id
