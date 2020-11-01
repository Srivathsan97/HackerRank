#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    sum_of_all_hourglass = []
    for rows in range(0, 4):
        for column in range(0, 4):
            sum_of_each_hourglass = sum(arr[rows][column:column+3]) + arr[rows+1][column+1] + sum(arr[rows+2][column:column+3])
            sum_of_all_hourglass.append(sum_of_each_hourglass)
    
    print(max(sum_of_all_hourglass))

    
