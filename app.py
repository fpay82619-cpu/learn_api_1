from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Sum API")

class Numbers(BaseModel):
    x: float
    y: float

@app.get("/health")
async def health():
    return {"ok": True}

@app.get("/sum")
async def sum_get(x: float, y: float):
    s = x + y
    return {"result": s, "text": f"сумма = {s}"}

@app.post("/sum")
async def sum_post(n: Numbers):
    s = n.x + n.y
    return {"result": s, "text": f"сумма = {s}"}
