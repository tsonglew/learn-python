#-*- coding: utf-8 -*-

import threading
l = threading.Lock()
global_num = 0


def thread_cal():
    global global_num
    for _ in xrange(1000):
        l.acquire()
        global_num += 1
        l.release()


def show(num):
    print(threading.current_thread().getName(), num)


def thread_cal():
    local_num = 0
    for _ in xrange(1000):
        local_num += 1
    show(local_num)


threads = []
for i in range(10):
    threads.append(threading.Thread(target=thread_cal))
    threads[i].start()
