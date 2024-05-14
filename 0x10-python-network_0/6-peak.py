#!/usr/bin/python3
""" Module for find_peak function """


def find_peak(list_of_integers):
    """ return max int in the list """

    if not list_of_integers or not isinstance(list_of_integers, list):
        return None

    ls = list_of_integers.copy()
    ls.sort()

    return ls[-1]
