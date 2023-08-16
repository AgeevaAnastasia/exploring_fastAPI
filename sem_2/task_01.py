"""Создать API для управления списком задач. Приложение должно иметь
возможность создавать, обновлять, удалять и получать список задач.
Создайте модуль приложения и настройте сервер и маршрутизацию.
Создайте класс Task с полями id, title, description и status.
Создайте список tasks для хранения задач.
Создайте маршрут для получения списка задач (метод GET).
Создайте маршрут для создания новой задачи (метод POST).
Создайте маршрут для обновления задачи (метод PUT).
Создайте маршрут для удаления задачи (метод DELETE).
Реализуйте валидацию данных запроса и ответа.
"""

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn
from fastapi import HTTPException

app = FastAPI()


class TaskIn(BaseModel):
    title: str
    description: Optional[str]
    status: bool


class Task(TaskIn):
    id: int


tasks = []


# response_model - то, что возвращает endpoint
@app.get("/", response_model=list[Task])
async def read_tasks():
    return tasks


# response_model - то, что возвращает endpoint
@app.post("/task/", response_model=Task)
# в аргументах - то, что принимаем
async def create_task(item: TaskIn):
    id = len(tasks) + 1
    task = Task
    task.id = id
    task.status = item.status
    task.title = item.title
    task.description = item.description
    tasks.append(task)
    return task


@app.get("/task/{id}", response_model=Task)
async def get_task_by_id_root(id: int):
    for task in tasks:
        if task.id == id:
            return task


@app.put("/task/{id}", response_model=Task)
async def put_task_by_id_root(id: int, new_task: TaskIn):
    for task in tasks:
        if task.id == id:
            task.status = new_task.status
            task.title = new_task.title
            task.description = new_task.description
            return task
    raise HTTPException(status_code=404, detail="Task not found")


if __name__ == '__main__':
    uvicorn.run(
        "task_01:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
