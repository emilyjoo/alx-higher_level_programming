#!/usr/bin/python3
# 9-max_integer.py


def max_integer(my_list=[]):
    """Return the biggest integer of the list."""
    if len(my_list) == 0:
        return (None)

    maxv = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > maxv:
            maxv = my_list[i]

    return (maxv)
