#locked
class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError
#locked

class Calculator(AdvancedArithmetic):
    def divisorSum(self, number):
        #pass
        sumOfDivisors = 0

        for divisor in range(1,number+1):
            if(number%divisor == 0):
                sumOfDivisors += divisor
        
        return sumOfDivisors

#locked
n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
#locked