from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def create_room():
    return {"message": "Sala criada com sucesso!"}

@router.delete("/{room_id}")
def delete_room(room_id: int):
    return {"message": f"Sala {room_id} removida com sucesso."}

@router.post("/{room_id}/enter")
def enter_room(room_id: int):
    return {"message": f"Entrou na sala {room_id}."}

@router.post("/{room_id}/leave")
def leave_room(room_id: int):
    return {"message": f"Saiu da sala {room_id}."}

@router.delete("/{room_id}/users/{user_id}")
def remove_user_from_room(room_id: int, user_id: int):
    return {"message": f"Usuário {user_id} removido da sala {room_id}."}
