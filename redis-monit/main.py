# Example code for test redis connected client count
# pip install redis first
import redis
from datetime import datetime
import time

r = redis.Redis(
    host='localhost',
    port=6379)

for i in range(1,100):
    cur = datetime.now()
    cur_str = cur.strftime("%d/%m/%Y %H:%M:%S")
    print(f"now = {cur_str}")
    r.set(f'cur_{i}', cur_str)
    time.sleep(10)
    print("===== result =====")
    var = r.get(f'cur_{i}')
    print(f"var = {var}")
    print("===== end ======")