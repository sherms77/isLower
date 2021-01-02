# Pg.80 - How to think like a cs
# example 1

import string, timeit

def isLower1(ch):
    l = string.ascii_lowercase
    return l.find(ch) != -1

exe_time = timeit.timeit(test_code, number = 1)
print(exe_time)

# print(isLower1('e')) # in['e']: print(isLower1('e')) out['e']: True
# print(isLower1('E')) # in['E']: print(isLower1('E')) out['E']: False

# timeit does not work for function. have to work out.


# Python 2 code to return index no. - to understand logic
# string.lowercase - output = 'abcdefghijklmnopqrstuvwxyz'
# def isLower(ch):
    # return string.find(string.lowercase, ch)
# print isLower ('e') - output = 4 - returns index 4 from string.lowercase
# print isLower ('gh') - output = 4 - returns index 6 from string.lowercase

# Python 2 code from book:
# def isLower(ch):
    # return string.find(string.lowercase, ch)

# 151220: I was having trouble understanding what the author was trying to achieve here but I think I understand it now.
# Firstly the output for the first version of the isLower(ch) function is:
# in ['c']: print isLower('c')
# out ['c']: True

