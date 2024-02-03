

from random import choice

A="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
a="abcdefghijklmnopqrstuvwxyz"
num="0123456789"

captcha =""
for i in range(5):
    captcha+=choice(A)+choice(a)+choice(num)

    print("Your captcha :",captcha)
