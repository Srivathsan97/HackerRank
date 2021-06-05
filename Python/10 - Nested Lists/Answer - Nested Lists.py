#declare the variable for use
stud_details = []

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        stud_details.append([name,score])

#converting the list to dict for easier usage
stud_details = dict(stud_details)

#set funtion removes the duplicates and retains unique values
#sorted function is used to sort the data
scores_sorted = sorted(set(stud_details.values()))

#fetching the second record from the sorted array to find the second lowest score
second_lowest_score = scores_sorted[1]

#fetching the student names who have the second lowesr score and storing them in array
second_lowest_score_stud_names = sorted([name for name,score in stud_details.items() if score == second_lowest_score])

#dispalying the values as required
for name in second_lowest_score_stud_names:
    print(name)




"""
Nested Lists are lists withing a list


Example 1:
a = [1,2,3]
print(a)

Example 2:
a = [1,'2',[int('3')]]
print(a)

Eaxmple 3:
a = [1, 2, [3,4,[5,6]],[7,8,[10,[11,[12,13,14]]],9]]
print(a)
print(a[2])
print(a[2][2])
print(a[2][2][1])
print(a[3][2])
print(a[3][2][1])
print(a[3][2][1][1])
print(a[3][2][1][1][2])


Resources:
1. https://www.learnbyexample.org/python-nested-list/
2. https://www.geeksforgeeks.org/nested-list-comprehensions-in-python/
"""