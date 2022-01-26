# coding=utf-8
import random
from datetime import datetime
import time


def add(a, b):
    return a + b


def show_express():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    
    while a + b >= 100:
        a = random.randint(1, 100)
        b = random.randint(1, 100)

    c = input('{} + {} = '.format(a, b))
    c = int(c)
    if c == add(a, b):
        print('小爱心你答对了, 真棒, 奖励一个小瓜子!')
        return True
    else:
        print('哎呀, 你答错了, 打一下小屁股')
        return False


all_correct = True
correct_count = 0
incorrect_count = 0
start = datetime.now()
for i in range(1, 11):
    print('第{}题:'.format(i))
    if not show_express():
        incorrect_count = incorrect_count + 1
        all_correct = False
    else:
        correct_count = correct_count + 1
end = datetime.now()

delta_time = end - start
print('小爱心, 你答题一共用了 {} 秒'.format(delta_time.seconds))

if (correct_count >= 8):
    print('你真棒, 答对了 {} 题, 奖励一个小糖果'.format(correct_count))
else:
    print('你答错 {} 题, 没有奖励'.format(incorrect_count))


if all_correct:
    print('小爱心真棒, 你有10个小瓜子啦')
else:
    print('哎呀, 你没有小瓜子了')