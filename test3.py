import threading
import time
import random

def executeThread(i):
    print("Thread {} sleeps at {} ".format(i,time.strftime("%H:%M:%S",time.gmtime())))
    randSleepTime=random.randint(1,4)
    print("randSleepTime is {}".format(randSleepTime))
    time.sleep(randSleepTime)
    print("Thread {} stops sleepting at {} gmtitme este {}".format(i, time.strftime("%H:%M:%S"), time.gmtime()))


executeThread(3)
lock=threading.Lock()

'''
for i in range(10):
    thread=threading.Thread(target=executeThread,args=(i,))
    thread.start()
    lock.acquire()
    print("Active Threads :",threading.activeCount())
    print("Threads Objects :",threading.enumerate())
    lock.release()
'''
#semaphore
max_connections = 2
semaphore = threading.BoundedSemaphore(max_connections)
for i in range(10):
    thread=threading.Thread(target=executeThread,args=(i,))
    thread.start()
    semaphore.acquire()
    print("Active Threads :",threading.activeCount())
    print("Threads Objects :",threading.enumerate())
    semaphore.release()