#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    #initialise the variable to hold the sum of all the elements of the array
    veryBigSum = 0
    
    #iterate over the elements and add them to get the final sum
    for position in range(len(ar)):
        veryBigSum += ar[position]
    
    return veryBigSum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
