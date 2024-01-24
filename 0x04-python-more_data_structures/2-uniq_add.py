#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniqList = list(set(my_list))
    sum = 0
    for i in uniqList:
        sum += i
    return sum
