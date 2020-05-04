'''
使用迭代器和生成器
'''

import sys

dict = {'apples' : 'tasty',
  'bananas' : 'the best',
  'brussel sprouts' : 'evil',
  'cauliflower' : 'pretty good'
    }

set = {"1","2","3",4,"5"}

it = iter(set)
while True:
    try:
        result = next(it)
        print(str(result)+":"+str(type(result)))
    except StopIteration:
        print(dir())
        sys.exit()

