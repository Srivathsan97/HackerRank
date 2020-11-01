#Write your code here
class Calculator():
    def power(self, number, p_exponent):
        if (number < 0 or p_exponent < 0):
            raise Exception("n and p should be non-negative")
        else:
            return pow(number,p_exponent)

#locked
myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   
#locked