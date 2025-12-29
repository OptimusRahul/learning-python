from multiprocessing import Process, Value

def increment_counter(counter):
    for _ in range(100_000):
        with counter.get_lock():
            counter.value += 1
    print(f"Counter: {counter.value}")

if __name__ == "__main__":
    counter = Value('i', 0)
    processes = [Process(target=increment_counter, args=(counter, )) for _ in range(4)]
    [p.start() for p in processes]
    [p.join() for p in processes]
    print(f"Counter: {counter.value}")