# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
b = int(input())
m = int(input())

print(pow(a,b))
print(pow(a,b,m))




"""
pow() usually returns the value of first arguement to the power of second arguement in the fuction, i.e., pow(x,y) provides the output for (x ** y)
pow(), apart from 2 arguements, can take a thrid arguement that gives the modulus of the pow(x,y), i.e., pow(x,y,z) provides output for ((x ** y) % z)

NOTE:
1. pow() and math.pow() are not same, completely. They are different
2. If pow() has a third input arguement, then the second arguement cannot be negative, i.e., pow(1,-2,2) is not accepted


Syntax:
pow(x, y[, z])


Example 1:
print(pow(4,4))

Example 2:
print(pow(4,4,4))

Example 3:
print(pow(4,-4,4))


Resources:
1. https://www.w3schools.com/python/ref_func_pow.asp
2. https://www.programiz.com/python-programming/methods/built-in/pow
3. https://stackoverflow.com/questions/10282674/difference-between-the-built-in-pow-and-math-pow-for-floats-in-python
"""