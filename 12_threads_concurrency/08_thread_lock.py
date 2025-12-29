import threading
import time

counter = 0
lock = threading.Lock()

def increment_counter():
    global counter
    for _ in range(100_000):
        with lock:
            counter += 1
    print(f"Counter: {counter}")

threads = [threading.Thread(target=increment_counter) for _ in range(10)]

start = time.time()
for t in threads:
    t.start()
for t in threads:
    t.join()

end = time.time()
print(f"Time taken: {end - start:.2f} seconds")

print(f"Final Counter: {counter}")