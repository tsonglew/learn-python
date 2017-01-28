import threading, time, random

counter_lock = threading.Lock()
printer_lock = threading.Lock()

counter = 0

def worker():
    global counter
    with counter_lock:
        counter += 1
        with printer_lock:
            print('The count is %d' % counter)
            print('----------------')

with printer_lock:
    print('Starting up')

worker_threads = []
for i in range(10):
    t = threading.Thread(target=worker)
    worker_threads.append(t)
    t.start()

for t in worker_threads:
    t.join()

with printer_lock:
    print('Finishing up')
