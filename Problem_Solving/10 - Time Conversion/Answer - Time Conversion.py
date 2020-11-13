#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    splitTime = s.split(':')
    if s[-2] == 'P':
        if splitTime[0] != '12':
            splitTime[0] = str(int(splitTime[0]) + 12)
    else:
        if splitTime[0] == '12':
            splitTime[0] = '00'
    
    splitTime = ":".join(splitTime)
    return (splitTime[ : -2])
            

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
