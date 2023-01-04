#!/usr/bin/python3
"""Module makes a pasical triagle"""


def pascal_triangle(n):
    """Function return n rows of pasical triangle """
    if n <= 0:
        return []
    check_list = [[1]]
    for j in range(n - 1):
        check_list.append([1] + [check_list[j][i] + check_list[j][i + 1]
                    for i in range(len(check_list[j]) - 1)] + [1])
    return check_list
