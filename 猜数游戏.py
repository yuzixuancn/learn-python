# coding=utf-8


import random
secret = random.randint(1, 99)
guess = 0
tries = 0
print('我是爱心, 我们来玩猜数游戏吧')
print('有一个数字在1-100之间, 我让你猜很多次')
while guess != secret and tries < 600:
    guess = int(input('你猜的数字是什么: '))
    if guess < secret:
        print('数字太小')
    elif guess > secret:
        print('数字太大')

    tries = tries + 1

if guess == secret:
    print('你猜对了, 恭喜你')
else:
    print('你没有机会再猜了, 等下次吧')
    print('秘密数字是: ', secret)


   