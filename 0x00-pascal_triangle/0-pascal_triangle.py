#!/usr/bin/python3


def pascal_triangle(n):
    """
    pascal triangle function
    """
    if n <= 0:
        return []
    pascal = []
    my_list = [1]

    for row_len in range(n):
        if row_len > 0:
            helper_list = my_list[:]
            helper_list.insert(0, 0)
            helper_list.append(0)
            del my_list
            my_list = []
            for index in range(len(helper_list) - 1):
                my_list.append(helper_list[index] + helper_list[index + 1])
        pascal.append(my_list[:])
    return pascal
