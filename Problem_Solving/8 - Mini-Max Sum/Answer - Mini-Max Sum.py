#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    #initialising an array to store the sum of each iteration, i.e., arrSum
    arrMinMax = []
    arrSum = 0
    
    for _ in range(0,len(arr)):
        
        #length of first array is considered in both places because, we need to iterate the loop as many times.
        
        for j in range(0,len(arr)):
            
            #we check the length of second array to make sure index value of the second array is omitted, in order to add elements from other positions of the first array
            if j != len(arrMinMax):
                arrSum += arr[j]
        arrMinMax.append(arrSum)
        
        #the sum is initialised to Zero for using in the next iteration
        arrSum = 0
    
    print (str(min(arrMinMax)) + " " + str(max(arrMinMax)))
        

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
