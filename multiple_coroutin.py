import asyncio, time

async def func1():
    while True:
        await asyncio.sleep(1)
        print("1")

async def func2():
    while True:
        await asyncio.sleep(1)
        print("2")        


async def func3():
    while True:
        await asyncio.sleep(1)
        print("3")        



if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    try:
        asyncio.ensure_future(func1())
        asyncio.ensure_future(func2())      
        asyncio.ensure_future(func3())
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        print("close the event loop")
        loop.close()