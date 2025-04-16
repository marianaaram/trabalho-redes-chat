from fastapi import FastAPI
from app.routes import users, messages, rooms


app = FastAPI(
    title="API de Whatzapling",
    version="1.0.0"
)

#Rotas
app.include_router(users.router, prefix="/users", tags=["Usuarios"])
app.include_router(rooms.router, prefix="/rooms", tags=["Salas"])
app.include_router(messages.router, prefix="/messages", tags=["Mensagens"])
