#-*- coding: utf-8 -*-
#!/usr/bin/env python


import threading
import time
import logging


logging.basicConfig(level=logging.DEBUG,
        format='(%(threadName)-10s) %(message)s'
        )


def daemon():
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')


d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)  # 设置daemon模式,主程序结束,这个子线程依然在


def non_daemon():
    logging.debug('Starting')
    logging.debug('Exiting')


t = threading.Thread(name='non-daemon', target=non_daemon)


d.start()
t.start()
