import threading
import time

lock = threading.Lock()
list = [0, 0, 0]
count = 3

class Thread1(threading.Thread):

    def __init__(self):
        super().__init__()
        self.count = 3
    
    def run(self):
        lock.acquire()
        while self.count > 0:
            list[self.count - 1] = 1
            self.count -= 1
            time.sleep(1)
            print('thread1', list)
        lock.release()

class Thread2(threading.Thread):

    def __init__(self):
        super().__init__()
        self.count = 3
        self.a = 0
    
    def run(self):
        lock.acquire()
        while self.count > 0:
            list[self.count - 1] = 2
            self.count -= 1
            print('thread2',list)
            time.sleep(1)
        lock.release()

thread = Thread1()
thread.start()
threads = Thread2()
threads.start()

while count > 0:
    list[count - 1] = 3
    count -= 1
    print('main',list)
    time.sleep(1
