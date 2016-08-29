#!/usr/bin/env python
#-*- coding: utf-8 -*-

import threading
import logging


logging.basicConfig(level=logging.DEBUG,
        format='(%(threadName)-10s) %(message)s',
        )


class MyThreadWithArgs(threading.Thread):  # 继承threading.Thread，实例化，重写run()，调用start()启动
    def __init__(self, group=None, target=None, name=None,
            args=(), kwargs=None, verbose=None):
        threading.Thread.__init__(self, group=group, target=target, name=name,
                verbose=verbose)
        self.args = args
        self.kwargs = kwargs
        return

    def run(self):
        logging.debug('running with %s and %s', self.args, self.kwargs)
        return


for i in range(5):
    t = MyThreadWithArgs(args=(i,), kwargs={'a': 'A', 'b': 'B'})
    t.start()
