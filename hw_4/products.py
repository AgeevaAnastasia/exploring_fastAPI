from models import *
from fastapi.responses import HTMLResponse
from fastapi import APIRouter
from fastapi import Request
from db import *
from fastapi.templating import Jinja2Templates
from random import randint

templates = Jinja2Templates(directory="templates")
router = APIRouter()


# Создание тестовых товаров
@router.get("/fake_prods/{count}")
async def create_prods(count: int):
    for i in range(1, count + 1):
        query = products.insert().values(
            product_name=f'product_name_{i}',
            description=f'description_of_product_number {i}',
            price=randint(100, 10000),)
        await db.execute(query)
    return {'message': f'{count} fake products create'}


# Создание нового товара
@router.post("/prods/new/", response_model=Product)
async def create_product(product: InputProduct):
    query = products.insert().values(
        product_name=product.product_name,
        description=product.description,
        price=product.price)
    last_record_id = await db.execute(query)
    return {**product.dict(), "id": last_record_id}


# Получить список товаров
@router.get("/prods/", response_model=list[Product])
async def read_products():
    query = products.select()
    return await db.fetch_all(query)


# Просмотр одного товара
@router.get('/products/{product_id}', response_model=Product)
async def get_product(product_id: int):
    query = products.select().where(products.c.id == product_id)
    return await db.fetch_one(query)


# Редактирование товара
@router.put('/products/replace/{product_id}', response_model=Product)
async def replace_product(product_id: int, new_product: InputProduct):
    query = products.update().where(products.c.id == product_id).values(**new_product.dict())
    await db.execute(query)
    return {**new_product.dict(), "id": product_id}


# Удаление товара
@router.delete('/products/del/{product_id}')
async def delete_product(product_id: int):
    query = products.delete().where(products.c.id == product_id)
    await db.execute(query)
    return {'message': f'Product deleted'}


# Вывод товаров в HTML
@router.get("/l_prods/", response_class=HTMLResponse)
async def list_products(request: Request):
    query = products.select()
    return templates.TemplateResponse("db.html",
                                      {"request": request,
                                       'products': await db.fetch_all(query)})
