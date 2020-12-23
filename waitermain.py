import threading
from waiter import Waiter

def main():
    thread1 = Waiter()
    thread2 = Waiter()
    thread3 = Waiter()
    thread1.start()
    thread2.start()
    thread3.start()

if __name__=="__main__":
    main()
    