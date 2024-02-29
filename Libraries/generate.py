#随机生成——random.choice,random.randint,random.shuffle

import random
# import random中的所有module
"""
coin = random.choice(["heads","tails"])
print(coin)



# from random import choice,这种就只import choice这一个module,而不是所有的random
from random import choice
coin = choice(["heads","tails"])
print(coin)




number = random.randint(1,10)#1-10之间的随机int，包括1和10
print(number)
"""

cards = ["jack","queen","king"]
random.shuffle(cards) #shuffle是打乱cards这个list里面内容物的顺序
for card in cards:
    print(card)