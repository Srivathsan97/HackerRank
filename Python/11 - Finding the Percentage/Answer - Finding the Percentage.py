#scores_avg = 0
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

#reading the names and scores for each student
for name,scores in student_marks.items():
    scores_avg = 0
	
	#validating if the input name is present in the dictionary
    if name == query_name:
	
		#reading the scores sepertely to calculate average
        for score in scores:
            scores_avg += score
		
		#reading the length of the scores to know the total number of scores
        scores_avg = scores_avg/len(scores)

#printing the average value with precision of 2 decimal points
print("{0:.2f}".format(scores_avg))




"""
Python String Formatting is done to provide a neater and clearer output

format() function helps in formatting the strings

Example 1:
print("{0:.2f}".format(1.222223457890427856298824))

Example 2:
print("{0:1.2f}".format(1.222223457890427856298824))
print("{0:4.2f}".format(1.222223457890427856298824))

Example 3:
print("{0:9.5f}".format(1223.222223457890427856298824))
print("{0:6.3f}".format(2685921.222223457890427856298824))
print("{0:12 .3f}".format(2685921.222223457890427856298824))


Resources:
1. https://www.programiz.com/python-programming/methods/string/format
2. https://www.geeksforgeeks.org/nested-list-comprehensions-in-python/
"""