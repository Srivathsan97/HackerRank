#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    candles.sort()
    numberOfCandlesWithMaxHeight = candles.count(candles[len(candles) - 1])
    
    #NOTE: We can use the for loop and check for xount of the max value of max height, but the time for execution will be exceed the expected limit. 
    #Hence using count() gets a faster reply for bigger arrays.
    
    """
    numberOfCandlesWithMaxHeight = 0
    
    for i in len(candles):
        if candles[i] == max(candles):
            numberOfCandlesWithMaxHeight += 1
    """
    
    return numberOfCandlesWithMaxHeight

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
