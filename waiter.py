import threading

class Waiter(threading.Thread):
    def __init__(self):
        super(Waiter,self).__init__()

    def run(self):
        for i in range(5):
            print(i)



def main():
    thread1 = Waiter()
    thread2 = Waiter()
    thread3 = Waiter()
    thread1.start()
    thread2.start()
    thread3.start()

if __name__=="__main__":
    main()