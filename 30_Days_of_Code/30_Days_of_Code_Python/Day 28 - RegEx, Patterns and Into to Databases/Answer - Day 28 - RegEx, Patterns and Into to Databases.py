#!/bin/python3

import math
import os
import random
#importing re as regex for easier understanding. This format may not be used for your works
import re as regex
import sys



if __name__ == '__main__':
    N = int(input())
    arrayOfNames = []

    for N_itr in range(N):
        firstName_emailID = input().split(" ")

        firstName = firstName_emailID[0]

        emailID = firstName_emailID[1]
        
        if regex.search("@gmail\.com$",emailID):
            arrayOfNames.append(firstName)
    
    arrayOfNames.sort()
            
    for namesOfGmailUsers in arrayOfNames:
        print(namesOfGmailUsers)
