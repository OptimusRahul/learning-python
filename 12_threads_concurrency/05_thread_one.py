import threading
import time

def boil_milk():
    print(f"Started the milk boiling thread..")
    time.sleep(2)
    print(f"Finished the milk boiling thread..")

def toast_bread():
    print(f"Started the bread toasting thread..")
    time.sleep(3)
    print(f"Finished the bread toasting thread..")

thread1 = threading.Thread(target=boil_milk, name="Thread-1")
thread2 = threading.Thread(target=toast_bread, name="Thread-2")

start = time.time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
end = time.time()
print(f"Time taken: {end - start:.2f} seconds")