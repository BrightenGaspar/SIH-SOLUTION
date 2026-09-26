import asyncio
import json
import time
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="SIH 0.5s Realtime Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.websocket("/ws/sih-updates")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    req_count = 14290
    try:
        while True:
            req_count += 1
            payload = {
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime()),
                "total_requests": req_count,
                "status": "ONLINE"
            }
            await websocket.send_text(json.dumps(payload))
            await asyncio.sleep(0.5)
    except WebSocketDisconnect:
        pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)