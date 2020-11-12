#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    #We are declaring the number of spaces in order in move the "#" towards left.
    #"n-1" is used, in order to hold the first "#" at "n"th position.
    numberOfSpaces = n - 1
    
    for i in range(0,n):
        for j in range(0,numberOfSpaces):
            print(end = " ")
        
        #numberOfSpaces is reduced in order to reduce the spaces to occupy the increasing
        #count of "#"
        numberOfSpaces = numberOfSpaces - 1
        
        #we iterate with "i" as we need to "#" in cohesion with the value of "i"
        for j in range(0,i+1):
            print("#",end = "")
        
        print("\r")

if __name__ == '__main__':
    n = int(input())

    staircase(n)
