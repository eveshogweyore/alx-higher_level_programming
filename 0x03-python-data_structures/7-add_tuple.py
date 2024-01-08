#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    count = 0
    new_tuple = ()
    if len(tuple_a) == 0:
        tuple_a += (0, 0, )
    if len(tuple_a) == 1:
        tuple_a += (0, )
    if len(tuple_b) == 0:
        tuple_b += (0, 0, )
    if len(tuple_b) == 1:
        tuple_b += (0, )
    while count < 2:
        add = tuple_a[count] + tuple_b[count]
        new_tuple += (add, )
        count += 1
    return new_tuple
