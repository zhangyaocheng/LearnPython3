'''
使用线程
在py3中，主要使用threading模块实现线程相关操作
        也可以使用_thread模块实现函数式线程调用
'''

#!/usr/bin/env python3

import _thread
import time

def print_time(threadName,delay):
    count = 0
    while count<5:
        time.sleep(delay)
        count += 1
        print("{0}:{1}".format(threadName,time.ctime(time.time())))

try:
    _thread.start_new_thread(print_time,("Thread-1",0.2,))
    _thread.start_new_thread(print_time,("Thread-2",0.4,))
    print("线程使用完毕")
except:
    print("Error:无法创建新线程")

while 1:  # 这里是为了等待线程的执行
    pass