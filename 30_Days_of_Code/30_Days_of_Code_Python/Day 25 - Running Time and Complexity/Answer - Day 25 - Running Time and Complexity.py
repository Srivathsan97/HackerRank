# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
numberOfTestCases = int(input())
def isItPrime(inputValue):
    if int(inputValue) < 2:
        return False
    rangeValue = int(math.sqrt(inputValue))
    for number in range(2, rangeValue + 1):
        if inputValue%number == 0:
            return False;
    return True;

for i in range(numberOfTestCases):
    if isItPrime(int(input())):
        print("Prime")
    else:
        print("Not prime")