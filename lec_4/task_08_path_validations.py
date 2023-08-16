"""Больше про валидацию данных

Ранее мы рассматривали возможность указать тип для переменной, чтобы FastAPI
сделал проверку данных по типу. В начале лекции поговорили о модели данных и
возможностях pydantic.Field для валидации полей модели. Рассмотрим работу с
fastapi.Path и fastapi.Query


Проверка параметра пути через Path

fastapi.Path — это класс, который используется для работы с параметрами пути
(path parameters) в URL и проверки данных. Он позволяет определять параметры
пути, которые будут передаваться в URL, а также задавать для них ограничения на
тип данных и значения.


Пример 1:"""

from fastapi import FastAPI, Path
app = FastAPI()
@app.get("/items/{item_id}")
async def read_item(item_id: int = Path(..., ge=1), q: str = None):
    return {"item_id": item_id, "q": q}


"""В этом примере мы создаем маршрут "/items/{item_id}" с параметром пути "item_id".
Параметр "item_id" имеет тип int и должен быть больше или равен 1. Мы используем
многоточие (...) в качестве значения по умолчанию для параметра "item_id", что
означает, что параметр обязателен для передачи в URL. Если параметр не передан
или его значение меньше 1, то будет сгенерировано исключение.

Пример 2:"""

from fastapi import FastAPI, Path
app = FastAPI()
@app.get("/items/{item_id}")
async def read_item(item_id: int = Path(..., title="The ID of the item"), q: str = None):
    return {"item_id": item_id, "q": q}


"""В этом примере мы создаем маршрут "/items/{item_id}" с параметром пути "item_id".
Кроме ограничений на тип данных и значения, мы также задаем для параметра
"item_id" заголовок "The ID of the item". Это заголовок будет использоваться при
генерации документации API: http://127.0.0.1:8000/redoc.
Примеры демонстрируют использование fastapi.Path для работы с параметрами
пути и проверки данных. При использовании Path мы можем определять параметры
пути, задавать для них ограничения на тип данных и значения, а также указывать
заголовки для документации API.
"""