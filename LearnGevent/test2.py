# -*- coding: utf-8 -*-
import time
import gevent
from gevent import select

start = time.time()
tic = lambda: 'at %1.1f seconds' % (time.time()-start)

def gr1():
    # Busy waits for a second, but we don't want to stick around...
    print 'Started Polling: %s' % tic()
    gr1start = time.time()
    select.select([], [], [], 4)
    print 'start: %s 1 Ended Polling: %s' % (gr1start, tic())

def gr2():
    # Busy waits for a second, but we don't want to stick around...
    print 'Started Polling: %s' % tic()
    gr2start = time.time()
    select.select([], [], [], 3)
    print 'start: %s 2 Ended Polling: %s' % (gr2start, tic())

def gr3():
    print 'Hey lets do some stuff while the greenlets poll, %s' % tic()
    gevent.sleep(1)

gevent.joinall([
    gevent.spawn(gr1),
    gevent.spawn(gr2),
    gevent.spawn(gr3),
    ])
