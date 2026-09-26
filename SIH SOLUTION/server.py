import asyncio
import json
import time
import os
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

app = FastAPI(title="SIH 0.5s Realtime Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_FILE = os.path.join(os.path.dirname(__file__), "problem_statements.json")

def load_problem_statements():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

problem_statements = load_problem_statements()

@app.get("/")
async def serve_index():
    index_path = os.path.join(os.path.dirname(__file__), "index.html")
    return FileResponse(index_path)

@app.get("/api/problem-statements")
async def get_problem_statements():
    return problem_statements

@app.get("/api/stats")
async def get_stats():
    total_ps = len(problem_statements)
    frozen = sum(1 for ps in problem_statements if ps.get("count", 0) >= 500)
    critical = sum(1 for ps in problem_statements if 400 <= ps.get("count", 0) < 500)
    moderate = total_ps - frozen - critical
    total_subs = sum(ps.get("count", 0) for ps in problem_statements)
    return {
        "total_statements": total_ps,
        "frozen_count": frozen,
        "critical_count": critical,
        "moderate_count": moderate,
        "total_submissions": total_subs
    }

@app.websocket("/ws/sih-updates")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    req_count = 14290
    try:
        while True:
            req_count += 1
            # Randomly increment submission count on open PS occasionally
            updated_ps = None
            if len(problem_statements) > 0 and (req_count % 3 == 0):
                target_ps = random.choice(problem_statements)
                if target_ps.get("count", 0) < 500:
                    target_ps["count"] = min(500, target_ps["count"] + 1)
                    updated_ps = {
                        "id": target_ps["id"],
                        "count": target_ps["count"]
                    }

            payload = {
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime()),
                "total_requests": req_count,
                "status": "ONLINE",
                "updated_ps": updated_ps
            }
            await websocket.send_text(json.dumps(payload))
            await asyncio.sleep(0.5)
    except WebSocketDisconnect:
        pass

if __name__ == "__main__":
    import random
    import socket
    import uvicorn

    def is_port_in_use(port: int) -> bool:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex(('127.0.0.1', port)) == 0

    target_port = 8000
    while is_port_in_use(target_port) and target_port < 8050:
        print(f"Port {target_port} is in use. Falling back to port {target_port + 1}...")
        target_port += 1

    print(f"\n=======================================================")
    print(f"🚀 SIH COMMAND CENTER RUNNING AT: http://127.0.0.1:{target_port}")
    print(f"=======================================================\n")
    uvicorn.run(app, host="127.0.0.1", port=target_port)