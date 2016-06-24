#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import asyncio

async def hello():
	print("Hello world! (%s)" % threading.currentThread())
	r = await asyncio.sleep(1)
	print("Hello agin! (%s)" % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()