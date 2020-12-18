if __name__ == '__main__':
    n = int(raw_input())
    arr = list(set(map(int, raw_input().split())))
    arr.sort(reverse=True)
    print(arr[1])


"""
Set is one of the built-in data types which stores immutable element(s)/data.
Set, on the other hand, is mutable, on the whole, i.e., the data can be added or removed in the set, but the existing data cannot be 
modified

Syntax:
set_1 = {<enter value(s)>}

Example 1:
a = {1,2,3}
print(a)

Example 2:
a = {1,'2',int('3')}
print(a)

Eaxmple 3:
a = {1, 2, (3,4,(5,6))}
print(a)

Example 4: #note:The below will produce error
a = {1,2,{3,4}} 
b = {1,2,[3,4]}
print(a)
print(b)

Resources:
1. https://www.programiz.com/python-programming/set
2. https://www.w3schools.com/python/python_sets.asp
"""