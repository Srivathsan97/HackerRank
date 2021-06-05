# Enter your code here. Read input from STDIN. Print output to STDOUT
a = str(input())
eval(a)


"""
eval() is python's in-built function that considers the input values/string as expressions and returns integer values


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