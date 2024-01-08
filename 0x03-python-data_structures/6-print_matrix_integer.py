#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for inner_list in matrix:
        for i, j in enumerate(inner_list):
            if i == len(inner_list) - 1:
                print('{:d}'.format(j), end='')
            else:
                print('{:d}'.format(j), end=' ')
        print()
