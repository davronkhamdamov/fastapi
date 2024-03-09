from app.api.models import UsersSchema
from app.db import database, users


async def register(payload: UsersSchema):
    query = users.insert().values(
        name=payload.name, surname=payload.surname, email=payload.email
    )
    return await database.execute(query=query)


async def get(user_id: int):
    query = users.select().where(user_id == users.c.id)
    return await database.fetch_one(query=query)


async def get_all():
    query = users.select()
    return await database.fetch_all(query)


async def put(user_id: int, payload: UsersSchema):
    query = (
        users.update()
        .where(user_id == users.c.id)
        .values(name=payload.name, surname=payload.surname, email=payload.email)
        .returning(users.c.id)
    )
    return await database.execute(query=query)


async def delete(user_id: int):
    query = users.delete().where(user_id == users.c.id)
    return await database.execute(query=query)
