from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from app.routers import chat

app = FastAPI()

# Подключение статики и маршрутов
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(chat.router)

@app.get("/", response_class=HTMLResponse)
def get_chat_page():
    with open("static/index.html", "r") as file:
        return file.read()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
