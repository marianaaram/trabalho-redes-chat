from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import uuid

router = APIRouter()
users = {}  # Ex: {"user_id": {"id": ..., "username": ...}}

class User(BaseModel):
    username: str

@router.post("/")
def register_user(user: User):
    if any(u["username"] == user.username for u in users.values()):
        raise HTTPException(status_code=400, detail="Nome já em uso.")
    user_id = str(uuid.uuid4())
    users[user_id] = {"id": user_id, "username": user.username}
    return users[user_id]

@router.post("/login")
def login_user(user: User):
    for u in users.values():
        if u["username"] == user.username:
            return {"message": "Login OK", "user": u}
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

@router.get("/{user_id}")
def get_user(user_id: str):
    if user_id in users:
        return users[user_id]
    raise HTTPException(status_code=404, detail="Usuário não encontrado")




#from fastapi import APIRouter
#from pydantic import BaseModel
#
#router = APIRouter()
#
#class UserCreate(BaseModel):
#    username: str
#
#@router.post("/")
#def create_user(user: UserCreate):
#    return {"message": f"Usuário '{user.username}' criado com sucesso!"}
#
#@router.post("/login")
#def login(user: UserCreate):
#    return {"message": f"Login de '{user.username}' realizado com sucesso!"}
#
#@router.get("/{user_id}")
#def get_user(user_id: int):
#    return {"user_id": user_id, "username": "exemplo"}
