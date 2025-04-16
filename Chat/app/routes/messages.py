from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

# Armazenamento em memória
messages = {
    "direct": {},  # direct[receiver_id] = [{from, text, timestamp}]
    "rooms": {}    # rooms[room_id] = [{from, text, timestamp}]
}


class Message(BaseModel):
    sender_id: str
    text: str

# Enviar mensagem direta para outro usuário
@router.post("/direct/{receiver_id}")
def send_direct_message(receiver_id: str, message: Message):
    if receiver_id not in messages["direct"]:
        messages["direct"][receiver_id] = []
    messages["direct"][receiver_id].append({
        "from": message.sender_id,
        "text": message.text,
        "timestamp": datetime.utcnow().isoformat()
    })
    return {"message": "Mensagem enviada com sucesso."}

# Enviar mensagem para uma sala
@router.post("/rooms/{room_id}/messages")
def send_room_message(room_id: str, message: Message):
    if room_id not in messages["rooms"]:
        messages["rooms"][room_id] = []
    messages["rooms"][room_id].append({
        "from": message.sender_id,
        "text": message.text,
        "timestamp": datetime.utcnow().isoformat()
    })
    return {"message": "Mensagem enviada para a sala."}

# Recuperar histórico de mensagens da sala
@router.get("/rooms/{room_id}/messages")
def get_room_messages(room_id: str):
    return messages["rooms"].get(room_id, [])







#from fastapi import APIRouter
#from pydantic import BaseModel
#
#router = APIRouter()
#
#class Message(BaseModel):
#    content: str
#
#@router.post("/direct/{receiver_id}")
#def send_direct_message(receiver_id: int, message: Message):
#    return {"to": receiver_id, "content": message.content}
#
#@router.post("/rooms/{room_id}/messages")
#def send_room_message(room_id: int, message: Message):
#    return {"room": room_id, "content": message.content}
#
#@router.get("/rooms/{room_id}/messages")
#def get_room_messages(room_id: int):
#    return {"room": room_id, "messages": ["Mensagem 1", "Mensagem 2"]}
#

