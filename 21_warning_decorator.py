import time, random
from my_functions.decorators import temp_warning

@temp_warning
def get_sensor_data():
    temp = random.randint(100, 2000)
    print(f"Temperature: {temp}")
    return temp

while True:
    get_sensor_data()
    time.sleep(1)