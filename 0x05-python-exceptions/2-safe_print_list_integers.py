#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    total_num = 0
    for num in range(x):
        try:
            print("{:d}".format(my_list[num]), end="")
            total_num += 1
        except (ValueError, TypeError):
            continue
    print()
    return(total_num)

