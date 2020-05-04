'''
使用threading模块创建线程
py3中主要使用theading模块创建线程
'''

import threading
import time

exitFlag = 0

class myThread(threading.Thread):

    def __init__(self, threadId, threadName, delay):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.threadName = threadName
        self.delay = delay

    def run(self):
        print("开始线程："+self.threadName)
        print_name(self.threadName,self.delay,5)
        print("结束线程:"+self.threadName)

def print_name(threadName,delay,count):
    while count:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("{}:{}".format(threadName,time.ctime(time.time())))
        count -=1

thread1 = myThread(1,"Thread-1",1)
thread2 = myThread(2,"Thread-2",2)

thread1.start()
thread2.start()
thread1.join()    # join方法会阻塞调用线程，直到调用join方法的线程执行完毕或者出错或者超时，这里调用线程就是主线程，
                  # 主线程调用了thread1和thread2线程，直到这两个线程都执行完毕了主线程才能继续执行。
                  # 这个方法就相当于控制线程执行流程的一个方法
thread2.join()
print("推出主线程")