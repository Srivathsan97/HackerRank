# Enter your code here. Read input from STDIN. Print output to STDOUT
actualReturnDate = list(map(int,input().rstrip().split(" ")))
expectedReturnDate = list(map(int,input().rstrip().split(" ")))
fineForDelayedReturn = 0

if actualReturnDate[2] > expectedReturnDate[2]:
    fineForDelayedReturn = 10000
elif actualReturnDate[2] == expectedReturnDate[2]:
    if actualReturnDate[1] > expectedReturnDate[1]:
        fineForDelayedReturn = (actualReturnDate[1] - expectedReturnDate[1]) * 500
    elif actualReturnDate[1] == expectedReturnDate[1]:
        if actualReturnDate[0] > expectedReturnDate[0]:
            fineForDelayedReturn = (actualReturnDate[0] - expectedReturnDate[0]) * 15
        
print(fineForDelayedReturn)