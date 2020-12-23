import asyncio

async def count():
	print("One")
	await asyncio.sleep(1)
	print("Two")

async def function():
	await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
	import time
	s = time.time()
	asyncio.run(function())
	elapsed = time.time() - s
	print(elapsed)