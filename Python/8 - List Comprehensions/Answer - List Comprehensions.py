if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print( [[i,j,k] for i in range( x + 1) for j in range( y + 1) for k in range(z+1) if ( ( i + j + k ) != n )  ])



"""
List Comprehensions are used to create new lists from various other iterables.
List comprehensions are consist of square brackets "[]", whihc contain the expression that is eexecuted for every element based on the "for" loop condition.

Syntax:
[ expression for item in list if conditional ]

Example 1:
new_list = [element for element in range(31,50) if element%3 == 0]
print(new_list)

Example 2:

new_list_1 = [element for element in "You can do it" if element == " "]
print(new_list_1)
new_list_2 = [element for element in "You can do it" if element != " "]
print(new_list_2)

Resources:
1. https://www.programiz.com/python-programming/list-comprehension
2. http://pythonforbeginners.com/basics/list-comprehensions-in-python
"""