"""Создание моделей для взаимодействия с таблицей в БД

Создадим две модели данных Pydantic:"""


class UserIn(BaseModel):
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)


class User(BaseModel):
    id: int
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)


"""Первая модель нужна для получения информации о пользователе от клиента. А
вторая используется для возврата данных о пользователе из БД клиенту.


Добавление тестовых пользователей в БД

Прежде чем работать над созданием API и проходить всю цепочку CRUD для
клиента сгенерируем несколько тестовых пользователей в базе данных."""


@app.get("/fake_users/{count}")
async def create_note(count: int):
    for i in range(count):
        query = users.insert().values(name=f'user{i}',
        email=f'mail{i}@mail.ru')
        await database.execute(query)
    return {'message': f'{count} fake users create'}


"""Принимаем целое число count и создаём в БД указанное число пользователей с
именами и почтами. Теперь мы готовы не только разрабатывать CRUD, но и
тестировать его.


🔥 Важно! Не забудьте перейти по адресу http://127.0.0.1:8000/fake_users/25
чтобы добавить пользователей.


💡 Внимание! В реальном проекте подобные функции должны быть
отключены перед запускам в продакшен.
"""