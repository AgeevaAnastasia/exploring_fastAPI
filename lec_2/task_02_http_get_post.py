"""Обработка HTTP-запросов и ответов

HTTP (Hypertext Transfer Protocol) — это протокол передачи данных в интернете,
используемый для обмена информацией между клиентом и сервером. В FastAPI
обработка HTTP-запросов и ответов происходит автоматически.


Основы протокола HTTP

Протокол HTTP работает по схеме "клиент-сервер". Клиент отправляет запрос на
сервер, а сервер отвечает на этот запрос. Запрос состоит из трех частей: метод,
адрес и версия протокола. Методы запроса могут быть GET, POST, PUT, DELETE и
другие. Адрес - это URL-адрес ресурса, к которому обращается клиент. Версия
протокола указывает на версию HTTP, которую использует клиент.

Обработка запросов GET

Метод GET используется для получения ресурсов с сервера. В FastAPI обработка
GET-запросов происходит с помощью декоратора @app.get(). Например:"""

import logging
from fastapi import FastAPI
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
app = FastAPI()


@app.get("/")
async def read_root():
    logger.info('Отработал GET запрос.')
    return {"Hello": "World"}


"""Этот код создает приложение FastAPI и добавляет обработчик GET-запросов для
корневого URL-адреса. Функция read_root() возвращает JSON-объект {"Hello":
"World"}.


Обработка запросов POST

Метод POST используется для отправки данных на сервер. В FastAPI обработка
POST-запросов происходит с помощью декоратора @app.post(). Например:"""


import logging
from fastapi import FastAPI
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
app = FastAPI()
@app.post("/items/")
async def create_item(item: Item):
    logger.info('Отработал POST запрос.')
    return item


"""Этот код создает приложение FastAPI и добавляет обработчик POST-запросов для
URL-адреса /items/. Функция create_item() принимает объект Item и возвращает его
же.


🔥 Внимание! Код выше не будет работать, так как мы не определили объект
Item. Речь о модуле pydantic позволяющем создать класс Item будет позже
в рамках курса.


Обработка запросов PUT

Метод PUT используется для обновления данных на сервере. В FastAPI обработка
PUT-запросов происходит с помощью декоратора @app.put(). Например:"""


import logging
from fastapi import FastAPI
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
app = FastAPI()


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    logger.info(f'Отработал PUT запрос для item id = {item_id}.')
    return {"item_id": item_id, "item": item}


"""Этот код создает приложение FastAPI и добавляет обработчик PUT-запросов для
URL-адреса /items/{item_id}. Функция update_item() принимает идентификатор
элемента и объект Item и возвращает JSON-объект с этими данными.


🔥 Внимание! Код выше не будет работать, так как мы не определили объект
Item. Речь о модуле pydantic позволяющем создать класс Item будет позже
в рамках курса."""