from datetime import datetime
from time import sleep
def my_decorator(function):
    def horario():
        print(datetime.now())
        function()
        print(datetime.now())
    return horario

@my_decorator
def soma_decimal(number=10):
    for num in range(10):
        sleep(2)
        print(num)

soma_decimal()