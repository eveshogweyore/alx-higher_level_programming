#!/usr/bin/python3
num = 1
while num <= 89:
    if num % 10 == 0:
        num += ((num // 10) + 1)

    if num != 89:
        print('{:02d}'.format(num), end=', ')
    else:
        print('{:02d}'.format(num))
    num += 1
