# Pg.80 - How to think like a cs
# example 3
# refer to isLower1.py for notes

import string

def isLower3(ch):
    return 'a' <= ch <= 'z'

print(isLower3('e')) # in['e']: print(isLower1('e')) out['e']: True
print(isLower3('E')) # in['E']: print(isLower1('E')) out['E']: False

# Python 2 code from book:
# def isLower(ch):
    # return 'a' <= ch <= 'z'
