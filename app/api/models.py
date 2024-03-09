from pydantic import BaseModel, Field


class UsersSchema(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    surname: str = Field(..., min_length=3, max_length=50)
    email: str = Field(..., min_length=5, max_length=50)


class UsersDB(UsersSchema):
    id: int
