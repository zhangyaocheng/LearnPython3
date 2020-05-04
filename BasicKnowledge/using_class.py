'''
测试python中的类
'''

class Myclass:
    i = 0  # 类对象
    __prive_var = 0;
    def __init__(self):
        self.show = "Hello, zyc!" # 实例对象

        # self.i = n
    def f(self):
        print("hello world")

    def __pri_func(self):
        print("私有函数")

x = Myclass()
# x.f()
# Myclass.f(x)
# print(dir(x))       # 属于实例
# print(dir(Myclass)) # 属于类
# x._Myclass__pri_func()
# print(x._Myclass__prive_var)
# x._Myclass__prive_var = 2
# print(x._Myclass__prive_var)
# print("x.i = ",x.i)
# print("x.f() = ",x.f())
# print(x.show)

# print("Myclass.i = ",Myclass.i)
# print("Myclass.f() = ",Myclass.f(x))

# print(x.i)
# print(Myclass.i)
# x.i = 100
# print(x.i)
# print(Myclass.i)
# Myclass.i = 120
# print(x.i)
# print(Myclass.i)

# print(Myclass.i)
# y = Myclass(2)
# print(y.i)
# print(Myclass.i)
# Myclass.i = 12
# print(y.i)
# print(Myclass.i)

# print(id(x.i))
# print(id(Myclass.i))
#
# x.i=100
# print(x.i)
# print(Myclass.i)
#
# print(id(x.i))
# print(id(Myclass.i))
