# -*- coding: utf-8 -*-

import asyncio
import datetime

async def show_date(loop):
    end_time = loop.time() + 5.0
    while True:
        print(datetime.datetime.now())
        if loop.time() + 1.0 > end_time:
            break
        else:
            await asyncio.sleep(1)

loop = asyncio.get_event_loop()
loop.run_until_complete(show_date(loop))
loop.close()
