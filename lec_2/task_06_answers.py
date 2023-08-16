"""Форматирование ответов API

FastAPI позволяет форматировать ответы API в различных форматах, например, в
JSON или HTML. Для этого нужно использовать соответствующие функции модуля
fastapi.responses.

● HTML текст
Например:"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def read_root():
    return "<h1>Hello World</h1>"


"""Этот код создает конечную точку для корневого URL-адреса, которая возвращает
HTML-страницу с текстом "Hello World". Функция read_root() использует класс
HTMLResponse для форматирования ответа в HTML.


● JSON объект
В этом примере возвращается ответ JSON с настраиваемым сообщением и кодом
состояния."""

from fastapi import FastAPI
from fastapi.responses import JSONResponse
app = FastAPI()


@app.get("/message")
async def read_message():
    message = {"message": "Hello World"}
    return JSONResponse(content=message, status_code=200)


"""В этом примере мы импортируем класс JSONResponse из модуля FastAPI.responses.
Внутри функции read_message мы определяем словарь, содержащий ключ
сообщения со значением «Hello World». Затем мы возвращаем объект
JSONResponse со словарем сообщений в качестве содержимого и кодом состояния
200.
"""