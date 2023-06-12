#!/usr/bin/python3
# 10-divisible_by_2.py


def divisible_by_2(my_list=[]):
    """Return multiples of 2 in the list."""
    mult = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            mult.append(True)
        else:
            mult.append(False)

    return (mult)
