#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    c = 0
    for i in my_list:
        try:
            if c == x:
                break
            print("{:d}".format(i), end="")
            c += 1
        except Exception as e:
            pass
    print()
    return c
