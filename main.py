from contextlib import contextmanager
from time import time, sleep


@contextmanager
def timer():
    time1 = time()
    print(time1)
    print("Start")
    yield
    print("Finish")
    time2 = time()
    print(time2)
    print(time2 - time1)


with timer() as manager:
    for i in range(5):
        print(i * i)

print(100 * "*")


class Timer:
    def __init__(self):
        pass

    def __enter__(self):
        print("Start")
        time3 = time()
        print(time3)
        return time3

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Finish')


with Timer() as manager:
    for i in range(5):
        print(i * i)
        sleep(1)
    time4 = time()
    print(time4)
    print(round(time4 - manager,2))
