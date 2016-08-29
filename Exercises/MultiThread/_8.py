#-*- coding: utf-8 -*-

import logging
import threading
import time


logging.basicConfig(level=logging.DEBUG,
        format='(%(threadName)-10s) %(message)s',
        )


def wait_for_event(e):
    logging.debug('wait_for_event starting')
    event_is_set = e.wait()  # 主线程将被阻塞，它将不会再被分配时间片，直到现有的一些线程退出运行
    logging.debug('event set: %s', event_is_set)


def wait_for_event_timeout(e, t):
    while not e.isSet():
        logging.debug('wait_for_event_timeout starting')
        event_is_set = e.wait(t)  # 设置等待超时
        logging.debug('evnet set: %s', event_is_set)
        if event_is_set:
            logging.debug('processing event')
        else:
            logging.debug('doing other work')


e = threading.Event()  # 替代time.sleep()，用wait()和set()来精确控制线程，2个或者多个线程同步操作
t1 = threading.Thread(
        name='block',
        target=wait_for_event,
        args=(e,)
        )
t1.start()


t2 = threading.Thread(
        name='non-block',
        target=wait_for_event_timeout,
        args=(e, 2)
        )
t2.start()


logging.debug('Waiting before calling Event.set()')
time.sleep(3)
e.set()
logging.debug('Event is set')
