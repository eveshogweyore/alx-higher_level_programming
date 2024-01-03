#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) in range(91, 123):
            c = chr(ord(c) - 32)
            print('{}'.format(c), end="")
        else:
            print('{}'.format(c), end="")

    print("")
