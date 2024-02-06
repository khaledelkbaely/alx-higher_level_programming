#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    isint = True
    try:
        print("{:d}".format(value))
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        isint = False

    return isint
