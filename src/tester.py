"""
tester.py
"""
import sys # system arguments
import time # time execution
from cows import Cows as c # the cows, themselves

if __name__ == '__main__':
    test_txt = sys.argv[0]

    print('Begin cows test')
    start = time.time()
    with open(test_txt) as test:
        for line in test:
            cows.process_record(test)
    exec_time = round(time.time() - start, 4)
    print('Execution time was ' + str(exec_time))
