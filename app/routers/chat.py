import json
import re

from fastapi import APIRouter, HTTPException, WebSocket, WebSocketDisconnect

from app.services.database import Database
from app.services.message_service import MessageService

router = APIRouter()

db = Database()
message_service = MessageService(db)

chat_connections = {}

# Ограничения
USERNAME_MAX_LENGTH = 32
CHAT_ID_MAX_LENGTH = 64
ASCII_PATTERN = re.compile(r'^[ -~]+$')  # Только ASCII-символы

def validate_input(value: str, max_length: int, field_name: str):
    if len(value) > max_length:
        raise HTTPException(status_code=400, detail=f"{field_name} слишком длинный. Максимальная длина: {max_length} символов.")
    if not ASCII_PATTERN.match(value):
        raise HTTPException(status_code=400, detail=f"{field_name} содержит недопустимые символы. Разрешены только ASCII.")

@router.websocket("/ws/{chat_id}/{username}")
async def websocket_endpoint(websocket: WebSocket, chat_id: str, username: str):
    # Проверка ограничений
    validate_input(chat_id, CHAT_ID_MAX_LENGTH, "chat_id")
    validate_input(username, USERNAME_MAX_LENGTH, "username")

    await websocket.accept()
    
    if chat_id not in chat_connections:
        chat_connections[chat_id] = []
    chat_connections[chat_id].append(websocket)
    
    history = message_service.get_chat_history(chat_id)
    await websocket.send_text(json.dumps({"history": history}))
    
    try:
        while True:
            data = await websocket.receive_text()
            message_data = {"username": username, "message": data}
            message_service.save_message(chat_id, username, data)
            
            for connection in chat_connections[chat_id]:
                await connection.send_text(json.dumps(message_data))
    except WebSocketDisconnect:
        chat_connections[chat_id].remove(websocket)