#-*- coding: utf-8 -*-
#!/usr/bin/env python

import threading


def worker(num):
    print('Worker: %s' % num)
    return


threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()
