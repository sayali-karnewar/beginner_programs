import asyncio, random

async def myFunc(idd):
    process_length = random.randint(1,5)
    await asyncio.sleep(process_length)
    print("id:",idd," took time ", process_length)

async def main():
    tasks = []
    for i in range(10):
        k = asyncio.ensure_future(myFunc(i))
        tasks.append(k)

    await asyncio.gather(*tasks)    



loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(main())
finally:
    loop.close()    