#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    new = []
    for i in range(my_list):
        if (my_list[i] % 2) == 0:
            new[i] = True
        else:
            new[i] = False
    return new
