'''
函数相关
'''

def show(a:int,b:str)->str:
    return str(a)+":"+b

print(show(12,"12"))

c = lambda arg1,arg2:arg1*arg2
print(c(12,23))

list1 = [12,3,4,3,4,1]
list1.clear()
print(list1)