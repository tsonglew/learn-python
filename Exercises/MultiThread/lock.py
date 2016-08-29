#!/usr/bin/env python
#-*- coding: utf-8 -*-

# A factory function that returns a new primitive lock object. Once a thread
# has acquired it, subsequent attempts to acquire it block, until it is
# released; ** any thread may release it. **
import threading
import time


lock = threading.Lock()


def lock_holder(lock):
    print('Starting')
    while True:
        lock.acquire()
        print('Holding')
        time.sleep(100)
        print('Sleep done')


def lock_release(lock):
    time.sleep(1)
    lock.release()
    print('Release it')



holder = threading.Thread(target=lock_holder, args=(lock,), name='LockHolder')
holder.setDaemon(True)
holder.start()


release = threading.Thread(target=lock_release, args=(lock,), name='release')
release.start()


holder = threading.Thread(target=lock_holder, args=(lock,), name='LockHolder')
holder.setDaemon(True)
holder.start()
