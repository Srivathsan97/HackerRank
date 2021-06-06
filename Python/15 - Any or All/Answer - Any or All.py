# Enter your code here. Read input from STDIN. Print output to STDOUT
n,numbers_input =input(), input().split()
print(all(map(lambda n:int(n)>-1,numbers_input)) and any(map(lambda n:n==n[::-1],numbers_input)))



"""
all() - Returns boolean True if all the iterations are true
any() - Returns boolean True if any one of the iterations is true


Example 1:
print(any([1>10,1==1,2>1,3<0]))

Example 2:
print(all([1>10,1==1,2>1,3<0]))

Example 3:
print(all([True,True]))
print(any([True,False]))

Example 4:
print(all([True,False]))
print(any([False,False]))


Resources:
1. https://towardsdatascience.com/python-eval-built-in-function-601f87db191

"""