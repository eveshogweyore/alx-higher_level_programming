#!/usr/bin/python3
def no_c(my_string):
    count = 0
    list_string = list(my_string)
    while count <= len(list_string) - 1:
        if list_string[count] in 'cC':
            list_string.pop(count)
            continue
        count += 1
    new_string = ''
    for i in list_string:
        new_string += i
    return new_string
