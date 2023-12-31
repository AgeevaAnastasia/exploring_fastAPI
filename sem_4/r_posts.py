from models import *
from fastapi.responses import HTMLResponse
from fastapi import APIRouter
from fastapi import Request
from db import *
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
router = APIRouter()


@router.get('/posts/', response_model=list[Post])
async def get_post():
    query = sqlalchemy.select(
        posts_db.c.id, posts_db.c.post,
        # alias
        users_db.c.id.label("user_id"),
        users_db.c.login).join(users_db)
    rows = await db.fetch_all(query)
    # query = posts_db.select()
    # return await db.fetch_all(query)
    # for row in rows:
    #     print(row)
    return [
        Post(id=row.id, post=row.post, user=User(id=row.user_id, login=row.login, password='xxxxxx', email='zzzzzz'))
        for row in rows]


@router.post('/posts/', response_model=dict)
async def inp_post(post: InputPost):
    query = posts_db.insert().values(
        user_id=post.us_id,
        post=post.post, )
    last_record_id = await db.execute(query)
    return {**post.dict(), "id": last_record_id}


sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
sqlalchemy.Column("user_id", sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'), nullable=False),
sqlalchemy.Column("post", sqlalchemy.String(1000)),
