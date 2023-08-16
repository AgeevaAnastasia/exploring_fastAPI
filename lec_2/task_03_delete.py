"""Обработка запросов DELETE

Метод DELETE используется для удаления данных на сервере. В FastAPI обработка
DELETE-запросов происходит с помощью декоратора @app.delete(). Например:"""


import logging
from fastapi import FastAPI
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
app = FastAPI()


@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    logger.info(f'Отработал DELETE запрос для item id = {item_id}.')
    return {"item_id": item_id}


"""Этот код создает приложение FastAPI и добавляет обработчик DELETE-запросов для
URL-адреса /items/{item_id}. Функция delete_item() принимает идентификатор
элемента и возвращает JSON-объект с этим идентификатором.


🔥 Важно! Зачастую операция удаления не удаляет данные из базы данных, а
изменяет специально созданное поле is_deleted на значение Истина. Таким
образов вы сможете восстановить ранее удалённные данные
пользователя, если он передумает спустя время.


Валидация данных запроса и ответа

FastAPI позволяет автоматически валидировать данные запроса и ответа с
помощью модуля pydantic. Например, можно создать класс Item для валидации
данных:"""

...
from typing import Optional
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
"""
...
Этот класс содержит поля name, description, price и tax. Поля name и price
обязательны, а поля description и tax необязательны. Затем можно использовать
этот класс для валидации данных запроса и ответа:"""
...
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
...
app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
...


@app.post("/items/")
async def create_item(item: Item):
    logger.info('Отработал POST запрос.')
    return item
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    logger.info(f'Отработал PUT запрос для item id = {item_id}.')
    return {"item_id": item_id, "item": item}
"""...


Этот код добавляет обработчики POST и PUT запросов, которые принимают объект
Item и возвращают его же. Если данные не соответствуют описанию класса Item, то
FastAPI вернет ошибку 422 с описанием ошибки.
"""