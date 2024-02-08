

from random import choice

A="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

captcha =""
for i in range(5):
    captcha+=choice(A)

    print("Your captcha :",captcha)
