#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    numberOfTestCases = int(input())

    for _ in range(numberOfTestCases):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])
        print(k-1 if ((k-1) | k) <= n else k-2)
