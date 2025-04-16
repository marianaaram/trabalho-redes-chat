from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import uuid

router = APIRouter()
rooms = {}  # Ex: {room_id: {"id": room_id, "name": "Sala 1", "users": []}}

class Room(BaseModel):
    name: str

class UserAction(BaseModel):
    username: str  # A gente identifica os usuários só pelo nome por enquanto

@router.post("/")
def create_room(room: Room):
    room_id = str(uuid.uuid4())
    rooms[room_id] = {"id": room_id, "name": room.name, "users": []}
    return rooms[room_id]

@router.get("/")
def list_rooms():
    return list(rooms.values())

@router.delete("/{room_id}")
def delete_room(room_id: str):
    if room_id not in rooms:
        raise HTTPException(status_code=404, detail="Sala não encontrada")
    del rooms[room_id]
    return {"message": f"Sala {room_id} removida com sucesso."}

@router.post("/{room_id}/enter")
def enter_room(room_id: str, user: UserAction):
    if room_id not in rooms:
        raise HTTPException(status_code=404, detail="Sala não encontrada")
    if user.username in rooms[room_id]["users"]:
        return {"message": f"{user.username} já está na sala."}
    rooms[room_id]["users"].append(user.username)
    return {"message": f"{user.username} entrou na sala {room_id}."}

@router.post("/{room_id}/leave")
def leave_room(room_id: str, user: UserAction):
    if room_id not in rooms:
        raise HTTPException(status_code=404, detail="Sala não encontrada")
    if user.username not in rooms[room_id]["users"]:
        return {"message": f"{user.username} não está na sala."}
    rooms[room_id]["users"].remove(user.username)
    return {"message": f"{user.username} saiu da sala {room_id}."}

@router.delete("/{room_id}/users/{username}")
def remove_user_from_room(room_id: str, username: str):
    if room_id not in rooms:
        raise HTTPException(status_code=404, detail="Sala não encontrada")
    if username not in rooms[room_id]["users"]:
        raise HTTPException(status_code=404, detail="Usuário não está na sala")
    rooms[room_id]["users"].remove(username)
    return {"message": f"Usuário {username} removido da sala {room_id}."}