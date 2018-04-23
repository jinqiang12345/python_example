import threading
import time

exitflag = 0

class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("thread start:" + self.name)
        threadLock.acquire()
        print_time(self.name, self.counter, 5)
        print("thread close:" + self.name)
        threadLock.release()

def print_time(threadName, counter, delay):
    while counter:
        if exitflag:
            threadName.exit()
        time.sleep(delay)
        print("{0} : {1}".format(threadName, time.ctime(time.time())))
        counter -= 1

threadLock = threading.Lock()
thread = []
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

thread1.start()
thread2.start()

thread.append(thread1)
thread.append(thread2)

for t in thread:
    t.join()
print("out")

