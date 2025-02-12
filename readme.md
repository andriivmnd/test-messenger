# WebSocket Messenger

Простой мессенджер на FastAPI с WebSockets и хранением сообщений в SQLite.

## 🚀 Функционал
- Подключение к чату через WebSockets.
- Автоматическое создание чата при первом сообщении.
- Отправка и получение сообщений в реальном времени.
- Сохранение истории сообщений в базе данных.

## 📂 Структура проекта
```
/test-messenger
│── /app
│   │── /routers
│   │   ├── chat.py  # WebSocket логика
│   │── /services
│   │   ├── database.py  # Работа с БД
│   │   ├── message_service.py  # Обработка сообщений
│   │── __init__.py
│── /static
│   ├── index.html  # Фронтенд
│── main.py  # Запуск приложения
│── req.txt
│── README.md
```

## 🛠 Технологии
- **Backend**: FastAPI, WebSockets
- **Database**: SQLite
- **Frontend**: HTML + JavaScript (WebSockets)

## 📌 Установка
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/andriivmnd/test-messenger.git
   cd test-messenger
   ```
2. Создайте виртуальное окружение и установите зависимости:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Linux/Mac
   venv\Scripts\activate  # Для Windows
   pip install -r req.txt
   ```
3. Запустите сервер:
   ```bash
   uvicorn main:app --reload
   ```

## 🖥 Использование
1. Откройте браузер и перейдите по адресу:
   ```
   http://127.0.0.1:8000/
   ```
2. Введите **Username** и **Chat ID**, затем нажмите **Connect**.
3. Чат загружается и можно отправлять сообщения.

## 📝 API Эндпоинты
- `GET /` – Возвращает веб-интерфейс чата.
- `WS /ws/{chat_id}/{username}` – WebSocket для чата.