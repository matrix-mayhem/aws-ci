from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Frontend running"}

@app.get("/send")
def send_task():
    res = requests.post("http://api-service:8000/task", json={"task": "hello"})
    return res.json()