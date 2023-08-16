"""Работа с полями моделей данных

Поля модели данных могут иметь различные атрибуты, такие как заголовок,
описание, значение по умолчанию и другие. Эти атрибуты можно использовать для
создания документации и проверки данных.

Функция Field позволяет задавать различные параметры для поля, такие как тип
данных, значение по умолчанию, ограничения на значения и т.д. Например, чтобы
задать поле типа str с ограничением на длину в 10 символов, можно использовать
следующий код:"""


from pydantic import BaseModel, Field
class User(BaseModel):
    name: str = Field(max_length=10)


"""💡 Внимание! Field импортируется непосредственно из pydantic, а не из
fastapi как для всех остальных (Query, Path и т.д.).


В этом примере мы определили класс User, который содержит поле name, тип
которого str. Мы также использовали функцию Field для задания ограничения на
максимальную длину строки в 10 символов.


Еще один пример использования функции Field — это задание значения по
умолчанию для поля. Например, чтобы задать поле типа int со значением по
умолчанию 0, можно использовать следующий код:"""


class User1(BaseModel):
    age: int = Field(default=0)


"""В этом примере мы определили класс User, который содержит поле age, тип
которого int. Мы также использовали функцию Field для задания значения по
умолчанию равного 0.

Рассмотрим ещё один пример:"""

from fastapi import FastAPI
from pydantic import BaseModel, Field
app = FastAPI()
class Item(BaseModel):
    name: str = Field(title="Name", max_length=50)
    price: float = Field(title="Price", gt=0, le=100000)
    description: str = Field(default=None, title="Description", max_length=1000)
    tax: float = Field(0, title="Tax", ge=0, le=10)

class User2(BaseModel):
    username: str = Field(title="Username", max_length=50)
    full_name: str = Field(None, title="Full Name", max_length=100)


"""В этом примере атрибуты title и description используются для создания
документации. Атрибуты min_length и max_length используются для ограничения
длины строковых полей. Атрибуты ge и le используются для ограничения числовых
полей.



Перечень принимаемых функцией Field параметров

Для валидации данных можно использовать следующие параметры при создании
моделей:
● default: значение по умолчанию для поля
● alias: альтернативное имя для поля (используется при сериализации и
десериализации)
● title: заголовок поля для генерации документации API
● description: описание поля для генерации документации API
● gt: ограничение на значение поля (больше указанного значения)
● ge: ограничение на значение поля (больше или равно указанному значению)
● lt: ограничение на значение поля (меньше указанного значения)
● le: ограничение на значение поля (меньше или равно указанному значению)
● multiple_of: ограничение на значение поля (должно быть кратно указанному
значению)
● max_length: ограничение на максимальную длину значения поля
● min_length: ограничение на минимальную длину значения поля
● regex: регулярное выражение, которому должно соответствовать значение
поля


💡 Внимание! Поля не ограничиваются этим списком. Полный перечень
можно увидеть в актуальной версии документации к FastAPI
"""