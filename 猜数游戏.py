# coding=utf-8


import random
secret = random.randint(1, 99)
guess = 0
tries = 0
print('我是一个海盗, 我有一个秘密')
print('有一个数字在1-99之间, 我让你猜6次')
while guess != secret and tries < 6:
    guess = int(input('你猜的数字是什么: '))
    if guess < secret:
        print('数字太小')
    elif guess > secret:
        print('数字太大')
    
    tries = tries + 1

if guess == secret:
    print('啊, 你发现了我的秘密')
else:
    print('你没有机会再猜了, 等下次吧')
    print('秘密数字是: ', secret)


   