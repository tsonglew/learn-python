# -*- coding: utf-8 -*-


import threading
import asyncio


@asyncio.coroutine
def hello():
    print('Hello World! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello Again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
