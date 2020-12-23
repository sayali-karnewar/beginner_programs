import asyncio, time

async def myfunc():
    print("function started")
    await asyncio.sleep(3)
    print('finished')
    


try:
    asyncio.run(myfunc())
finally:
    print("close")    