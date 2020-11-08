def is_leap(year):
    leap = False
    
    if (year >= 1900 and year <= (10000)):
        # Write your logic here
        if (year%4 == 0 and (year%100 !=0 or year%400 == 0)):
            leap = True
        else:
            leap = False
    return leap

#locked
year = int(input())
print(is_leap(year))
#locked


"""
Function is a block of code that contains statement(s) that are executed only when called for.
Additionally, functions reduce the size of the code, when the same code needs to be executed in multiple places.

Functions can take one or more parameters and data can be passed into the function through the parameters

Syntax:
def <function_name>([input parameters1, 2...]):
	statement(s)
	
<function_name>([paramater input])


Example 1:
def printAsItIs():
	print("You are inside a funtion")
	
printAsItIs()

Example 2:
def printWhatIsReceived(inputValue):
	print("Your input value is : " + str(inputValue))
	
printWhatIsReceived(int(10))

Resources:
1. https://www.w3schools.com/python/python_functions.asp
2. https://www.programiz.com/python-programming/function
3. https://www.tutorialspoint.com/python/python_functions.htm
"""
