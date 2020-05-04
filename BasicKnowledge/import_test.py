'''
关于import的相关测试
也就是说在使用import或者from..import模块或者函数时，会自动运行被导入模块的主线程，
因此需要将被导入模块的一些相关操作放在__main__里面，避免执行
一些不相干的操作
'''

def add(a,b,):
    t = 123
    s = "showme"
    return a+b

def sub(a,b):
    return a-b;

print("hello world")

