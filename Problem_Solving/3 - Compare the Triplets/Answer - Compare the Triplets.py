#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    #initialise the score variables
    aPoints = 0
    bPoints = 0
    
    #looping and finding whose rating is greater and based on the value, we update the scrores
    for position in range(len(a)):
        if a[position] > b[position]:
            aPoints += 1
        elif a[position] < b[position]:
            bPoints += 1
    
    return [aPoints,bPoints]
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
