from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class UserCreate(BaseModel):
    username: str

@router.post("/")
def create_user(user: UserCreate):
    return {"message": f"Usuário '{user.username}' criado com sucesso!"}

@router.post("/login")
def login(user: UserCreate):
    return {"message": f"Login de '{user.username}' realizado com sucesso!"}

@router.get("/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "username": "exemplo"}
