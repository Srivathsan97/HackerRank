#!/bin/python3

import sys

numberOfElements = int(input().strip())
arrayOfIntegers = list(map(int, input().strip().split(' ')))
# Write Your Code Here
numberOfSwaps = 0
for iteration in range(numberOfElements + 1):
    for position in range(numberOfElements - 1):
        if (arrayOfIntegers[position] > arrayOfIntegers[position + 1]):
            a = arrayOfIntegers[position]
            arrayOfIntegers[position] = arrayOfIntegers[position + 1]
            arrayOfIntegers[position + 1] = a

            numberOfSwaps += 1

print("Array is sorted in " + str(numberOfSwaps) + " swaps.")
print("First Element: " + str(arrayOfIntegers[0]))
print("Last Element: " + str(arrayOfIntegers[numberOfElements - 1]))