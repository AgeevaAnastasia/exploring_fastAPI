from pydantic import BaseModel, Field
from datetime import date


class InputUser(BaseModel):
    login: str = Field(..., title="Login", min_length=3)
    password: str = Field(..., title="Password", min_length=3)
    email: str = Field(..., title="E-mail", min_length=5)


class User(InputUser):
    id: int


class InputProduct(BaseModel):
    product_name: str = Field(..., title='product_name', min_length=4)
    description: str = Field(title='description')
    price: int = Field(..., title='price')


class Product(InputProduct):
    id: int


class InputOrder(BaseModel):
    user_id: int
    product_id: int
    order_date: date = Field(..., title='order_date')
    status: str = Field(..., title='status')


class Order(InputOrder):
    id: int
