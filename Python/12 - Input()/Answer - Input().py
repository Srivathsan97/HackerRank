# Enter your code here. Read input from STDIN. Print output to STDOUT
x, k = map(int,input().split())
print (eval(input()) == k)


"""
eval() is python's in-built function that considers the input values/string as expressions and returns integer values
input() function is used to get the values from user during runtime

Syntax:
eval(expression, [globals[, locals]])

Example 1:
eval("sum([82 + 92 + 202])")

Example 2:
x = 101.32
eval("x*100")


Resources:
1. https://towardsdatascience.com/python-eval-built-in-function-601f87db191

"""