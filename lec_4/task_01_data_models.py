"""Введение в модели данных в FastAPI


FastAPI предоставляет возможность определять модели данных для описания
формата запросов и ответов API. Это позволяет автоматически генерировать
документацию и проверять данные.


Определение моделей данных

Pydantic — это библиотека для валидации данных и сериализации объектов Python.
Она используется в FastAPI для валидации данных, получаемых из запросов, и
генерации документации API на основе моделей данных.
Модель данных — это класс Python, определяющий поля и их типы для описания
данных. Для определения моделей данных в FastAPI используется класс BaseModel
из модуля pydantic. Классы моделей содержат поля, которые описывают структуру
данных.


Пример:"""

from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


class User(BaseModel):
    username: str
    full_name: str = None


class Order(BaseModel):
    items: List[Item]
    user: User


"""В этом примере определены три модели данных: Item, User и Order. Каждая модель
данных содержит поля с указанными для них типами. Поле is_offer в модели Item
имеет значение по умолчанию None.
"""
