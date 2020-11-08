if __name__ == '__main__':
    n = int(input())
    if (n<=20 and n>=1):
        for i in range (0,n):
            print(i*i)


"""
Loops are statements that help us execute statement(s) continously, multiple times, until the condition becomes False.
Different looping statements are : for ; While and nested loops.

Example 1:
for i in range(10):
	print(i)

Example 2:
i = 3
while i < 3:
	print(i)
	i += 1

Resources:
1. http://tutorialspoint.com/python/python_loops.htm
2. http://learnpython.org/en/Loops
3. For Loop : https://www.w3schools.com/python/python_for_loops.asp
"""