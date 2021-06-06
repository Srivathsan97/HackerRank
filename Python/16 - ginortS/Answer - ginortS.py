# Enter your code here. Read input from STDIN. Print output to STDOUT
upprcase_ltrs = []
lowrcase_ltrs = []
digits_odd = []
digits_evn = []

string_input = str(input())
for i in string_input:
    if i.islower():
        lowrcase_ltrs.append(i)
    elif i.isupper():
        upprcase_ltrs.append(i)
    else:
        if int(i)%2 == 0:
            digits_evn.append(i)
        else:
            digits_odd.append(i)

lowrcase_ltrs.sort()
upprcase_ltrs.sort()
digits_evn.sort()
digits_odd.sort()

print(''.join(lowrcase_ltrs) + ''.join(upprcase_ltrs) + ''.join(digits_odd) + ''.join(digits_evn))


##############or the below can also be done
#whole_string = lowrcase_ltrs + upprcase_ltrs + digits_odd + digits_evn
#print(''.join(whole_string))


"""
isalpha() - helps in validating if the character is alphabet
islower() - helps in checking in the character is lowercase
isupper() - helps in checking in the character is uppercase
isdigit() - helps in checking in the character is a digit
"""