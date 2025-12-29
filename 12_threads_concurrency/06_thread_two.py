import threading
import time

def prepare_chai(type_, wait_time):
    print(f"Started the {type_} chai preparation thread..")
    time.sleep(wait_time)
    print(f"Finished the {type_} chai preparation thread..")

thread1 = threading.Thread(target=prepare_chai, args=("Masala", 2), name="Thread-1")
thread2 = threading.Thread(target=prepare_chai, args=("Elaichi", 3), name="Thread-2")

start = time.time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
end = time.time()
print(f"Time taken: {end - start:.2f} seconds")