from multiprocessing import Process
import time

def brew_chai(name):
    print(f"Start of {name} chai brewing")
    time.sleep(3)
    print(f"End of {name} chai brewing")



if __name__ == "__main__":
    chai_makers = [
        Process(target=brew_chai, args=(f"Chai Maker #{i+1}",))
        for i in range(3)
    ]
    # start processes
    for process in chai_makers:
        process.start()

    # wait for processes to complete
    for process in chai_makers:
        process.join()
        
    print("All chai brewing processes completed")