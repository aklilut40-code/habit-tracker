import sqlite3, json
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
db = sqlite3.connect("data.db", check_same_thread=False)
db.execute("CREATE TABLE IF NOT EXISTS state (visitor TEXT PRIMARY KEY, data TEXT)")
app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
def vid(r: Request): return r.headers.get("x-visitor-id", "local")
@app.get("/api/state")
def get_state(request: Request):
    row = db.execute("SELECT data FROM state WHERE visitor=?", [vid(request)]).fetchone()
    return json.loads(row[0]) if row else {}
@app.put("/api/state")
async def put_state(request: Request):
    body = await request.json()
    db.execute("INSERT INTO state(visitor,data) VALUES(?,?) ON CONFLICT(visitor) DO UPDATE SET data=excluded.data", [vid(request), json.dumps(body)])
    db.commit()
    return {"ok": True}
if __name__ == "__main__":
    import uvicorn; uvicorn.run(app, host="0.0.0.0", port=8000)
