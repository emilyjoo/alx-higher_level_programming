#!/usr/bin/python3
# 3-print_reversed_list_integer.py

def print_reversed_list_integer(my_list=[]):
      """Print integers of a list in reverse order."""
    my_list.reverse()
    for num in my_list:
        print("{:d}".format(num))
