# Tests and saves the runtimes of the three different versions of the isLower function.
# Report data is output to log_rpt.txt which saved to the users home folder.

import string, timeit, datetime

test_code1 = """    
def isLower1(ch):
    l = string.ascii_lowercase
    return l.find(ch) != -1
"""

test_code2 = """
def isLower2(ch):
    l = string.ascii_lowercase
    return ch in l
"""

test_code3 = """
def isLower3(ch):
    return 'a' <= ch <= 'z'
"""

exe_time1 = timeit.timeit(test_code1, number = 1)
exe_time2 = timeit.timeit(test_code2, number = 1)
exe_time3 = timeit.timeit(test_code3, number = 1)

stamp = datetime.datetime.now()
print('report date:', stamp)
print('isLower1 runtime is: ', exe_time1) # time is in seconds
print('isLower2 runtime is: ', exe_time2)
print('isLower3 runtime is: ', exe_time3)

def report():
    log = open('log_rpt.txt', 'a')
    
    # report date
    log.write('report date: ')
    log.write(str(stamp))
    log.write('\n')

    # time format info
    log.write('time is in seconds.')
    log.write('\n')
    
    # isLower1 output
    log.write('  isLower1 runtime: ')
    log.write(str(exe_time1))
    log.write('\n')
    
    # isLower2 output
    log.write('  isLower2 runtime: ')
    log.write(str(exe_time2))
    log.write('\n')
    
    # isLower3 ouput
    log.write('  isLower3 runtime: ')
    log.write(str(exe_time3))
    log.write('\n')
    log.write('\n')
        
    log.close()

report()