from typing import List
from fastapi import HTTPException, APIRouter, Path
import app.api.crud as crud
from app.api.models import UsersDB, UsersSchema

router = APIRouter()


@router.post("/", response_model=UsersDB, status_code=201)
async def create_user(payload: UsersSchema):
    user_id = await crud.post(payload)
    response_object = {
        "id": user_id,
        "name": payload.name,
        "surname": payload.surname,
        "email": payload.email,
    }
    return response_object


@router.get("/", response_model=List[UsersDB])
async def read_all():
    return await crud.get_all()


@router.put("/{id}/", response_model=UsersDB)
async def update_user(payload: UsersSchema, user_id: int = Path(..., gt=0)):
    user = await crud.get(user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    note_id = await crud.put(id, payload)
    response_object = {
        "id": note_id,
        "name": payload.name,
        "surname": payload.surname,
        "email": payload.email,
    }
    return response_object


@router.delete("/{id}/", response_model=UsersDB)
async def delete_user(user_id: int = Path(..., gt=0)):
    user = await crud.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    await crud.delete(user_id)
    return user
