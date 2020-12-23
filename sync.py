import time

def count():
	print(1)
	time.sleep(1)
	print(2)


def main():
	for _ in range(3):
		count()


if __name__ == '__main__':
	s = time.time()
	main()
	stop = time.time() - s
	print(stop)