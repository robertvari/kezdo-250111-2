import time

def my_timer(function):
    def wrapper():
        start_time = time.time()
        function()
        stop_time = time.time() - start_time
        print(f"Process time: {stop_time}")

    return wrapper