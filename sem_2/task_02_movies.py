"""Создать API для получения списка фильмов по жанру. Приложение должно
иметь возможность получать список фильмов по заданному жанру.
Создайте модуль приложения и настройте сервер и маршрутизацию.
Создайте класс Movie с полями id, title, description и genre.
Создайте список movies для хранения фильмов.
Создайте маршрут для получения списка фильмов по жанру (метод GET).
Реализуйте валидацию данных запроса и ответа.
"""

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn
from fastapi import HTTPException

app = FastAPI()


class Genre(BaseModel):
    id: int
    name: str


class Movie(BaseModel):
    id: int
    title: str
    description: Optional[str]
    genre: Genre


movies = [
    Movie(id=1, title='movie_1', description='cool movie', genre=Genre(id=1, name='drama')),
    Movie(id=2, title='movie_2', description='bad movie', genre=Genre(id=2, name='thriller')),
    Movie(id=3, title='movie_3', description='default movie', genre=Genre(id=2, name='thriller')),
]

genres = [
    Genre(id=1, name='drama'),
    Genre(id=2, name='thriller'),
    Genre(id=3, name='comedy'),
]


# response_model - то, что возвращает endpoint
@app.get("/", response_model=list[Movie], summary='Получить список фильмов по жанру', tags=['Фильмы'])
async def read_tasks(genre_id: int):
    result_list = []
    for movie in movies:
        if movie.genre.id == genre_id:
            result_list.append(movie)
    return result_list


if __name__ == '__main__':
    uvicorn.run(
        "task_02_movies:app",
        host="127.0.0.1",
        port=8000,
        # host="0.0.0.0",
        # port=6000,
        reload=True
    )
