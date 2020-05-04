'''
使用队列实现线程同步
'''

import queue
import time
import threading

exitFlag = 0

class myThread(threading.Thread):

    def __init__(self,threadname,q):
        threading.Thread.__init__(self)
        self.threadname = threadname
        self.q = q

    def run(self):
        print("开启线程:"+self.threadname)
        process_data(self.threadname,self.q)
        print("结束线程："+self.threadname)

def process_data(threadname,q):
    while not exitFlag:  # 这里是一个循环
        queuelock.acquire()
        if not workQueue.empty():
            data = q.get()
            queuelock.release()
            print("{} procee {}".format(threadname,data))
        else:
            queuelock.release()
        time.sleep(1)

queuelock = threading.Lock()
threadlist = ["Thread-1","Thread-2","Thread-3"]
namelist = ['one',"two","three","four","five"]
workQueue= queue.Queue(10)
threads = []

for tName in threadlist:
    thread = myThread(tName,workQueue)
    thread.start()
    threads.append(thread)

queuelock.acquire()
for word in namelist:
    workQueue.put(word)
queuelock.release()

while not workQueue.empty():
    pass

exitFlag = 1

for t in threads:
    t.join()

print("退出主线程")
