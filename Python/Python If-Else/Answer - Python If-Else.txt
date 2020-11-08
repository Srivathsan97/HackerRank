#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    inputNumber = int(input().strip())
    if(inputNumber >= 1 and inputNumber <= 100):
        if inputNumber%2 != 0:
            print("Weird")
        elif (inputNumber%2 == 0 and (inputNumber >= 2 and inputNumber <= 5)):
            print("Not Weird")
        elif (inputNumber%2 == 0 and (inputNumber >= 6 and inputNumber <= 20)):
            print("Weird")
        elif (inputNumber%2 == 0 and (inputNumber > 20)):
            print("Not Weird") 


"""
if-elif-else statements are called as CONDITIONAL statements, in Python, C, C++ etc. languages.
These statements work only based on the expression(conditions) specified.

Syntax:
if expression:
	Statement(s)
elif expression:
	Statement(s)
else:
	Statement(s)

Resources
1. https://www.w3schools.com/python/python_conditions.asp
2. https://www.programiz.com/python-programming/if-elif-else
3. https://www.tutorialspoint.com/python/python_if_else.htm
"""