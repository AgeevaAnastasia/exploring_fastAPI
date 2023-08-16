"""Создать API для управления пользователями в базе данных.

Приложение должно иметь возможность принимать POST запросы с данными
нового пользователя и сохранять их в базу данных.
Создайте модуль приложения и настройте сервер и маршрутизацию.
Создайте класс User с полями id, name, email и password.
Создайте список users для хранения пользователей.
Создайте маршрут для добавления нового пользователя (метод POST).
Создайте маршрут для обновления информации о пользователе (метод PUT).
Создайте маршрут для удаления информации о пользователе (метод DELETE).
Реализуйте валидацию данных запроса и ответа.

Создайте HTML шаблон для отображения списка пользователей. Шаблон должен
содержать заголовок страницы, таблицу со списком пользователей и кнопку для
добавления нового пользователя.
Создайте маршрут для отображения списка пользователей (метод GET).
Реализуйте вывод списка пользователей через шаблонизатор Jinja.
"""

from fastapi import FastAPI, Request, Form
from typing import Optional
from pydantic import BaseModel
import uvicorn
from fastapi import HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates


# для ввода
class UserInput(BaseModel):
    name: str
    email: Optional[str]
    password: str


class User(UserInput):
    id: int


users = [
    User(id=1, name='Alex', email='alex@yahoo.com', password='111'),
    User(id=2, name='Helen', email='helen@yahoo.com', password='222'),
    User(id=3, name='Daniel', email='daniel@yahoo.com', password='333'),
    User(id=4, name='Ruth', email='ruth@yahoo.com', password='444'),
    User(id=5, name='Ethan', email='ethan@yahoo.com', password='555')
]


@app.get("/", response_model=list[User], summary='Получить список пользователей',
         tags=['Список пользователей'])
async def get_users():
    return users


@app.get("/get_html", response_class=HTMLResponse, summary='Получить html-представление',
         tags=['Страница html с пользователями'])
async def get_html(request: Request):
    title = 'Список пользователей'
    return templates.TemplateResponse('main.html', {'request': request, 'title': title, 'users': users})


@app.post('/add_new_user/', summary='Добавить нового пользователя', tags=['Добавить пользователя'])
async def add_new_user(request: Request, name=Form(), email=Form(), password=Form()):
    user = User
    user.id = len(users) + 1
    user.name = name
    user.email = email
    user.password = password
    users.append(user)
    return user


@app.put("/user/{id}", response_model=User, summary='Изменить существующего пользователя',
         tags=['Изменить пользователя'])
async def put_user_by_id(id: int, new_user: UserInput):
    for user in users:
        if user.id == id:
            user.name = new_user.name
            user.email = new_user.email
            user.password = new_user.password
            return user
        raise HTTPException(status_code=404, detail=f'Пользователь с {id = } не существует')


@app.get("/user/{id}", response_model=User, summary='Получить пользователя по id', tags=['Получить по id'])
async def get_user_by_id(id: int):
    for user in users:
        if user.id == id:
            return user
        raise HTTPException(status_code=404, detail=f'Пользователь с {id = } не существует')


@app.delete("/user/{id}", summary='Удалить пользователя по id', tags=['Удалить пользователя'])
async def delete_user(id: int):
    for user in users:
        if user.id == id:
            users.remove(user)
            return users
        raise HTTPException(status_code=404, detail=f'Пользователь с {id = } не существует')


if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
