from fastapi import FastAPI
import redis
import json

from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response

app = FastAPI()

# Prometheus Counter
REQUEST_COUNT = Counter('request_count', 'Total API Requests')

# Redis connection
r = redis.Redis(host="redis", port=6379, decode_responses=True)

@app.get("/")
def read_root():
    REQUEST_COUNT.inc()
    return {"message": "API Service Running"}

@app.post("/task")
def add_task(data: dict):
    REQUEST_COUNT.inc()
    r.lpush("tasks", json.dumps(data))
    return {"status": "task added"}

# ✅ Metrics endpoint (CRITICAL FIX)
@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)