"""Создание API операций CRUD

Обсудим, как создать API операций CRUD (создание, чтение, обновление и
удаление) с использованием FastAPI и SQLAlchemy ORM.

Операции CRUD — это основные функции, которые используются в любом
приложении, управляемом базой данных. Они используются для создания, чтения,
обновления и удаления данных из базы данных. В FastAPI с SQLAlchemy ORM мы
можем создавать эти операции, используя функции и методы Python.
● CREATE, Создать: добавление новых записей в базу данных.
● READ, Чтение: получение записей из базы данных.
● UPDATE, Обновление: изменение существующих записей в базе данных.
● DELETE, Удалить: удаление записей из базы данных.


Работа с БД в CRUD операциях с SQLAlchemy и databases

Для работы с базой данных в операциях CRUD с SQLAlchemy ORM нам необходимо
сначала установить соединение с базой данных. Мы можем использовать любую
базу данных по нашему выбору, такую как MySQL, PostgreSQL или SQLite. После того,
как мы установили соединение, мы можем выполнять операции CRUD в базе
данных, используя SQLAlchemy ORM.

Например, предположим, что у нас есть база данных SQLite, в которой мы создадим
таблицу под названием «пользователи». Мы можем подключиться к базе данных,
используя следующий код:"""


import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel
DATABASE_URL = "sqlite:///mydatabase.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
users = sqlalchemy.Table(
    "users", metadata, sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(32)),
    sqlalchemy.Column("email", sqlalchemy.String(128)),
)

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)


"""💡 Внимание! По умолчанию SQLite разрешает взаимодействовать с ним
только одному потоку, предполагая, что каждый поток будет обрабатывать
независимый запрос. Это сделано для предотвращения случайного
использования одного и того же соединения для разных вещей (для
разных запросов). Но в FastAPI при использовании обычных функций (def)
несколько потоков могут взаимодействовать с базой данных для одного и
того же запроса, поэтому нам нужно сообщить SQLite, что он должен
разрешать это с помощью connect_args={"check_same_thread": False}."""