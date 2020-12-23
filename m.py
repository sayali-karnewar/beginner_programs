import multiprocessing

def sender1(msg1, que):
	que.put(msg1)



def sender2(msg2, que):
	if not que.empty():
		que.put(msg2)

if __name__ == '__main__':
	msg1 = 'hi!'
	msg2 = 'oh hie!'

	que = multiprocessing.Queue()

	p1 = multiprocessing.Process(target = sender1, args = (msg1, que))
	p2 = multiprocessing.Process(target = sender2, args = (msg2, que))

	p1.start()
	p1.join()

	p2.start()
	p2.join()