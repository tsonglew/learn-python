# -*- coding: utf-8 -*-
# 每个线程可以通过global_data.num获得自己独有的数据，做到线程之间的隔离

import threading


global_data = threading.local()
threads = []


def show():
    print threading.current_thread().getName(), global_data.num


def thread_cal():
    global_data.num = 0
    for _ in xrange(1000):
        global_data.num += 1
    show()


for i in range(10):
    threads.append(threading.Thread(target=thread_cal))
    threads[i].start()
