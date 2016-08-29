#-*- coding: utf-8 -*-

import threading
global_data = {}
threads = []


def show():
    cur_thread = threading.current_thread()
    print cur_thread.getName(), global_data[cur_thread]


def thread_cal():
    global global_data
    cur_thread = threading.current_thread()
    global_data[cur_thread] = 0
    for _ in xrange(1000):
        global_data[cur_thread] += 1
    show()

for i in range(10):
    threads.append(threading.Thread(target=thread_cal))
    threads[i].start()
