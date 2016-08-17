# -*- coding: utf-8 -*-


import asyncio


# 把一个generator标记为coroutine类型，放入EventLoop中
@asyncio.coroutine
def hello():
    print("Hello World!")
    # 调用另一个generator
    r = yield from asyncio.sleep(1)
    print("Hello again!")

# 获取EventLoop
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()
