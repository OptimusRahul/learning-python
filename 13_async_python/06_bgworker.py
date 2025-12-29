import asyncio
import threading
import time

def background_worker():
    while True:
        time.sleep(1)
        print("Background worker is running...")

async def main():
    await asyncio.sleep(3)
    print("Main coroutine is done")

threading.Thread(target=background_worker, daemon=True).start()

asyncio.run(main())