from fastapi import FastAPI
import redis
import json

app = FastAPI()

r = redis.Redis(host="redis", port=6379, decode_responses=True)

@app.get("/")
def read_root():
    return {"message": "API Service Running"}

@app.post("/task")
def add_task(data: dict):
    r.lpush("tasks", json.dumps(data))
    return {"status": "task added"}