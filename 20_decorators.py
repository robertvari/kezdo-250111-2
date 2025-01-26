import time, random
from my_functions.decorators import my_timer


@my_timer
def worker1():
    print("Worker1 started...")
    time.sleep(random.randint(1, 4))
    print("Worker1 finished.")

@my_timer
def worker2():
    print("Worker2 started...")
    time.sleep(random.randint(1, 4))
    print("Worker2 finished.")

@my_timer
def worker3():
    print("Worker3 started...")
    time.sleep(random.randint(1, 4))
    print("Worker3 finished.")


worker1()
worker2()
worker3()