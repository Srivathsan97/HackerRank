#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    #The below count variables are added to store the number of apples and oranges that landed on Sam's House.
    appleCount = 0
    orangeCount = 0
    
    for i in range(len(apples)):
        apples[i] = apples[i] + a
        if apples[i] >= s and apples[i] <= t:
            appleCount += 1
            
    for i in range(len(oranges)):
        oranges[i] = oranges[i] + b
        if oranges[i] >= s and oranges[i] <= t:
            orangeCount += 1
    
    print(appleCount)
    print(orangeCount)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
