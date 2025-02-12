from app.services.database import Database


class MessageService:
    def __init__(self, db: Database):
        self.db = db

    def save_message(self, chat_id: str, username: str, message: str):
        self.db.save_message(chat_id, username, message)

    def get_chat_history(self, chat_id: str):
        return self.db.get_chat_history(chat_id)