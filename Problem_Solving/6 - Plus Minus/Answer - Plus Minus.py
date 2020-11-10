#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    #initialising the variables to hold the number of +ve ; -ve ; 0 integers in the array
    positiveSum = 0
    negativeSum = 0
    zeroSum = 0
    
    for position in range(len(arr)):
        
        #condition to check if the element is negative
        if arr[position] < 0:
            negativeSum += 1
            
        #condition to check if the element is positive
        elif arr[position] > 0:
            positiveSum += 1
            
        #condition to check if the element is zero
        elif arr[position] == 0:
            zeroSum += 1
    
    #dividing the sum by length of the array inorder to find the ratio
    print(positiveSum/(len(arr)))
    print(negativeSum/(len(arr)))
    print(zeroSum/(len(arr)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
