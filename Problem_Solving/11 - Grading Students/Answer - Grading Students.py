#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    """
    The "%" symbol is used, in the below code, to fetch the remainder of the grade when divided by 5. 
    If the remainder is >= 3, it means the grade is <= 2 from the next rounding number.
    For example, consider grade 58. 58 is 2 numbers less than 60.
    Now divide 58 by 5. The remainder would be 3, i.e., 58 % 5 will give 3, since 58 is 3 greater than 55.
    Now, we need to add 2 to 58 to round it to 3. Hence 5 - remainder will give the value to be added.
    Therefore, 5 - (58 % 3) = 5 - 3 = 2. Thus, 2 must be added to the 58 to make it 60.
    Hence, 58 + (5 - (58 % 5)) = 60. This is the logic used in the below code.
    
    NOTE : If the grade is less than 38, it would be a failing grade, anyway. Hence, no rounding is needed.
    """
    for i in range(len(grades)):
        if grades[i] >= 38:
                if grades[i]%5 >= 3:
                    grades[i] = grades[i] + (5 - (grades[i]%5))
        
    return grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
