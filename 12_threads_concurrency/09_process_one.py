import threading
import time

def cpu_heavy():
    print(f"Started the CPU heavy process..")
    count = 0
    for i in range(10**7):
        count += i
    print(f"Finished the CPU heavy process..")

start = time.time()
threads = [threading.Thread(target=cpu_heavy) for _ in range(2)]
[t.start() for t in threads]
[t.join() for t in threads]
end = time.time()
print(f"Time taken: {end - start:.2f} seconds")