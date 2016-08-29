#-*- coding: utf-8 -*-

import threading
global_num = 0
l = threading.Lock()


def thread_cal():
    global global_num
    for i in xrange(1000):
        l.acquire()
        global_num += 1
        l.release()


threads = []
for i in xrange(10):
    threads.append(threading.Thread(target=thread_cal))
    threads[i].start()

for i in xrange(10):
    threads[i].join()


print global_num
