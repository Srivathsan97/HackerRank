#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    #intialise the varisles to store the values of the summed diagonals
    diagonalSum1 = 0
    diagonalSum2 = 0
    
    for position1 in range(len(arr)):
        for position2 in range(len(arr)):
            
            #condition check to add the element in Major Diagonal
            if position1 == position2:
                diagonalSum1 += arr[position1][position1]
            
            #condition check to add the element in Minor Diagonal
            if position1 == len(arr) - position2 - 1:
                diagonalSum2 += arr[position1][position2]
            
    return abs(diagonalSum1 - diagonalSum2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
