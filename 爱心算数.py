# coding=utf-8
import random


def add(a, b):
    return a + b


def show_express():
    a = random.randint(10, 20)
    b = random.randint(5, 10)
    c = input('{} + {} = '.format(a, b))
    c = int(c)
    if c == add(a, b):
        print('小爱心你答对了, 真棒, 奖励一个小瓜子!')
        return True
    else:
        print('哎呀, 你答错了, 打一下小屁股')
        return False


all_correct = True
for i in range(1, 11):
    print('第{}题:'.format(i))
    if not show_express():
        all_correct = False

if all_correct:
    print('小爱心真棒, 你有10个小瓜子啦')
else:
    print('哎呀, 你没有小瓜子了')