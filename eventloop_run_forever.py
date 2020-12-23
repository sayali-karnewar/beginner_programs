import asyncio, time

async def myfunc():
    while True:
        await asyncio.sleep(1)
        print('hello')

try:
    asyncio.run(myfunc()).run_forever()
finally:
    print("close")    