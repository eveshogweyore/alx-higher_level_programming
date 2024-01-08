#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for l in matrix:
        for i, j in enumerate(l):
            if i == len(l) - 1:
                print('{:d}'.format(j), end='')
            else:
                print('{:d}'.format(j), end=' ')
        print()
