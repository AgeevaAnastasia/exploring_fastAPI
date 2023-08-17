from models import *
from fastapi.responses import HTMLResponse
from fastapi import APIRouter
from fastapi import Request
from db import *
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
router = APIRouter()


# Получение всех заказов
@router.get('/orders/', response_model=list[Order])
async def get_orders():
    query = orders.select()
    return await db.fetch_all(query)


# Получение одного заказа
@router.get("/orders/id/{order_id}", response_model=Order)
async def read_order(order_id: int):
    query = orders.select().where(orders.c.id == order_id)
    return await db.fetch_one(query)


# Добавление нового заказа
@router.post('/orders/new/')
async def create_order(order: InputOrder):
    query = orders.insert().values(
        user_id=order.user_id,
        product_id=order.product_id,
        order_date=order.order_date,
        status=order.status)
    last_record_id = await db.execute(query)
    return {**order.dict(), "id": last_record_id}


# Изменение заказа
@router.put('/orders/replace/{order_id}')
async def change_order(order_id: int, new_order: InputOrder):
    query = orders.update().where(orders.c.id == order_id).values(**new_order.dict())
    await db.execute(query)
    return {**new_order.dict(), "id": order_id}


# Удаление заказа
@router.delete('/orders/del/{order_id}')
async def delete_order(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    await db.execute(query)
    return {'message': f'Order deleted'}
