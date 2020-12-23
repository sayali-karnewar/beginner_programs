import threading

def task():
    print("hello world", threading.current_thread())


thread1 = threading.Thread(target=task)

thread1.start()