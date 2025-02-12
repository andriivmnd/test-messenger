import sqlite3


class Database:
    def __init__(self, db_name="messages.db"):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chat_id TEXT NOT NULL,
            username TEXT NOT NULL,
            message TEXT NOT NULL
        )
        """)
        self.conn.commit()

    def save_message(self, chat_id: str, username: str, message: str):
        self.cursor.execute("INSERT INTO messages (chat_id, username, message) VALUES (?, ?, ?)", (chat_id, username, message))
        self.conn.commit()

    def get_chat_history(self, chat_id: str):
        self.cursor.execute("SELECT username, message FROM messages WHERE chat_id = ?", (chat_id,))
        return self.cursor.fetchall()