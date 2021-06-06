#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

#key arguement is used to difine the function that needs to take place while sorting
#here, we sort based on the Kth element of each sublist in the list
arr.sort(key=lambda x:x[k])


for i in arr:
    print(*i, sep = ' ')





"""
Lambda functions are anonymous, in-line functions which can take multiple arguements and perform simple operation on them and can have only one expression.
Key arguement in "sort()/sorted()" functions is a key for the sort comparison, i.e., the key mentions how the list must be sorted.

Syntax:
1. sort()
list.sort(key=..., reverse=...)

2. sorted()
sorted(list, key=..., reverse=...)


Example 1:
a = [3,1,5,8,2,3,5,0,2,1]
a.sort()
print(a)

Example 2:
a = [3,1,5,8,2,3,5,0,2,1]
a.sort(reverse=True)
print(a)

Example 3:
a = [3,1,5,8,2,3,5,0,2,1]
sorted(a)

Example 4:
a = [3,1,5,8,2,3,5,0,2,1]
sorted(a,reverse=True)


Resources:
1. https://www.programiz.com/python-programming/methods/list/sort
2. https://www.geeksforgeeks.org/sorted-function-python/
3. https://stackoverflow.com/questions/51269263/what-does-this-mean-key-lambda-x-x-1/51269284

"""