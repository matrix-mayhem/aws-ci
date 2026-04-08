import redis
import time
import json

r = redis.Redis(host="redis", port=6379, decode_responses=True)

while True:
    task = r.rpop("tasks")
    if task:
        data = json.loads(task)
        print(f"Processing task: {data}")
    time.sleep(2)