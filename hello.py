import aiofiles
import asyncio


async def func():
    async with aiofiles.open('main.py', mode='r') as f:
     contents = await f.read()
     print(contents)

asyncio.run(func())