from models import User, Gender, Role
from fastapi import FastAPI, HTTPException
from typing import List
from uuid import uuid4, UUID

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("4528c43f-f189-4dda-85fb-0e78cac23f3c"),
        name="Gabriel",
        email="teste@gmail.com",
        cpf="12345678900",
        gender=Gender.male, 
        roles=[Role.admin]
    ),
    User(
        id=UUID("1844e8b8-afa6-4c67-a8a5-db0503e3b5e7"),
        name="Giovana",
        email="abc@gmail.com",
        cpf="77777777900",
        gender=Gender.female, 
        roles=[Role.user]
    ),
    User(
        id=uuid4(),
        name="Marta",
        email="marta@gmail.com",
        cpf="10101019000",
        gender=Gender.female, 
        roles=[Role.admin, Role.user]
    ),
]

@app.get("/")
async def root():
    return {"olá"}

@app.get("/api/v1/users")
async def fetch_users():
    return db

@app.post("/api/v1/users")
async def create_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"message": f"User with id: {user_id} is deleted"}
        raise HTTPException(
            status_code=404,
            detail=f"user with id: {user_id} does not exists."
        )