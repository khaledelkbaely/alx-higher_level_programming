#!/usr/bin/python3
def islower(c):
    return True if ord(c) >= ord('a') and ord(c) <= ord('z') else False
def uppercase(str):
    for ch in str:
        print("{:c}".format(ord(ch) - ord('a') + ord('A') if islower(ch) else ord(ch)), end='')
    print()
