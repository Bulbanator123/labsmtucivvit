from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Query
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import uvicorn
import json
import datetime

from pydantic import ValidationError, Field, BaseModel
from fastapi import Request

app = FastAPI()

html_path = Path(__file__).parent / "templates"
templates = Jinja2Templates(directory=html_path)
app.mount("/static", StaticFiles(directory=html_path), name="static")

clients = {}


class Message(BaseModel):
    text: str = Field(..., min_length=1, max_length=200)


async def broadcast(data: dict):
    message = json.dumps(data)
    for client in clients:
        await clients[client].send_text(message)


@app.get("/")
async def get(request: Request, username: str = Query(None)):
    return templates.TemplateResponse("chat.html", {"request": request, "user": username})


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, username: str = Query(None)):

    if not username or username.strip() == "":
        await websocket.close(code=1008)
        return

    await websocket.accept()
    clients[username] = websocket

    await broadcast({
        "type": "info",
        "user": "System",
        "text": f"{username} joined. Online: {len(clients)}",
        "ts": datetime.datetime.now().isoformat()
    })

    try:
        while True:
            raw_data = await websocket.receive_text()

            try:
                data_json = json.loads(raw_data)

                msg_valid = Message(**data_json)

                if msg_valid.text.startswith("/w "):
                    pred_msg = msg_valid.text.split()
                    if len(pred_msg) > 2:
                        target = pred_msg[1]
                        text = " ".join(pred_msg[2:])
                        if target in clients:
                            private_msg = {
                                "type": "private",
                                "from": username,
                                "to": target,
                                "text": text,
                                "ts": datetime.datetime.now().isoformat()
                            }

                            await clients[target].send_text(json.dumps(private_msg))

                            await websocket.send_text(json.dumps(private_msg))

                        else:

                            await websocket.send_text(json.dumps({
                                "type": "error",
                                "detail": f"User {target} not found"
                            }))
                        continue
                response_payload = {
                    "type": "message",
                    "user": username,
                    "text": msg_valid.text,
                    "ts": datetime.datetime.now().isoformat()
                }
                await broadcast(response_payload)

            except (json.JSONDecodeError, TypeError):
                await websocket.send_text(json.dumps({
                    "type": "error",
                    "detail": "Invalid JSON format"
                }))
            except ValidationError as e:
                await websocket.send_text(json.dumps({
                    "type": "error",
                    "detail": "Message is empty or too long (max 200 chars)"
                }))

    except WebSocketDisconnect:
        del clients[username]
        await broadcast({
            "type": "info",
            "user": "System",
            "text": f"{username} left. Online: {len(clients)}",
            "ts": datetime.datetime.now().isoformat()
        })

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)