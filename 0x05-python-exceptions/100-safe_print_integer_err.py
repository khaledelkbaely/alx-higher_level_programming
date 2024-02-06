#!/usr/bin/python3
import sys


def safe_print_integer(value):
    isint = True
    try:
        print("{:d}".format(value))
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        isint = False
    return isint
