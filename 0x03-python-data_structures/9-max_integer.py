#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    my_list = sorted(my_list)
    return my_list[len(my_list) - 1]
