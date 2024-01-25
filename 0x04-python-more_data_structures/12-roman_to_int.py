#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    conversion = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500, 'M': 1000}
    result = 0
    n = 0
    for c in reversed(roman_string):
        n = conversion[c]
        result += n if result < n * 5 else -n
    return result
