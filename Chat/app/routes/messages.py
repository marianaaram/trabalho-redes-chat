from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Message(BaseModel):
    content: str

@router.post("/direct/{receiver_id}")
def send_direct_message(receiver_id: int, message: Message):
    return {"to": receiver_id, "content": message.content}

@router.post("/rooms/{room_id}/messages")
def send_room_message(room_id: int, message: Message):
    return {"room": room_id, "content": message.content}

@router.get("/rooms/{room_id}/messages")
def get_room_messages(room_id: int):
    return {"room": room_id, "messages": ["Mensagem 1", "Mensagem 2"]}
