# Pg.80 - How to think like a cs
# example 2
# refer to isLower1.py for notes

import string

def isLower2(ch):
    l = string.ascii_lowercase
    return ch in l

print(isLower2('e')) # in['e']: print(isLower1('e')) out['e']: True
print(isLower2('E')) # in['E']: print(isLower1('E')) out['E']: False

# Python 2 code from book:
# def isLower(ch):
    # return ch in string.lowercase
