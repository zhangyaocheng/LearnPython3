'''
使用python的数据结构
'''

# from collections import deque
#
# queue = deque([1,2,3])
# queue.append(13)
# queue.append(45)
# print(queue)
# queue.popleft()
# print(queue)
# print(type(queue))

# 使用zip函数
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
age = [1,2,3]
for a,b,c in zip(questions,answers,age):
    print("what is your {0}? it is {1}, how old are you? i am {2}".format(a,b,c))
