import asyncio

async def func(future):
    await asyncio.sleep(1)
    print('started')
    future.set_result("this is the future version")
    
async def main():
    future = asyncio.Future()  
    
    await asyncio.ensure_future(func(future)) 
    print("mid")
    print(future.result()) 
    

loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(main())
finally:
    print("close loop")    
    loop.close()




    '''
    direct exchange
    two processes
    send msg from one to another

    python with pika
    '''