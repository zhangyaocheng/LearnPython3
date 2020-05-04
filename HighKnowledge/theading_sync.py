'''
线程同步相关内容
使用threading模块构造相关内容
'''

import threading
import time

class myThread(threading.Thread):

    def __init__(self,threadid,threadname,delay):
        threading.Thread.__init__(self)
        self.threadid = threadid
        self.threadname = threadname
        self.delay = delay

    def run(self):
        print("开启线程:"+self.threadname)
        threadlock.acquire() # 启动锁
        print_time(self.threadname,self.delay,3)
        threadlock.release() #释放锁

def print_time(threadname,delay,count):
    while count:
        time.sleep(delay)
        print("{}:{}".format(threadname,time.ctime(time.time())))
        count -= 1

threadlock = threading.Lock()

thread1 = myThread(1,"Thread-1",2)
thread2 = myThread(2,"Thread-2",3)
thread1.start()
thread2.start()
thread1.join()
thread2.join()

print("线程执行完毕")