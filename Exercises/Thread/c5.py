import time
from threading import Thread, Event

def func1(n, evt):
    count = n
    while count > 0:
        if count == 5:
            evt.set()
        print('func1', count)
        count -= 1
        time.sleep(1)

def func2(n, evt):
    evt.wait()
    count = n
    while count > 0:
        print('func2', count)
        count -= 1
        time.sleep(1)

evt = Event()
t1 = Thread(target=func1, args=(10, evt))
t2 = Thread(target=func2, args=(10, evt))
t1.start()
t2.start()
