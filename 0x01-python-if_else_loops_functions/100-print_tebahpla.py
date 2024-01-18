#!/usr/bin/python3
def toupper(c):
    return c - ord('a') + ord('A')


for c in range(ord('z'), ord('a') - 1, -1):
    print("{:c}".format(c if (c - ord('z')) % 2 == 0 else toupper(c)), end='')
