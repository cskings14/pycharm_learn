'''
Exceptions are used to find errors and not automaticallly crash
'''

try:
    age = int(input('Age: '))  # if we don't input a number
    income = 20.000
    risk = income/age
    print(age)
except ZeroDivisionError:
    print('Age cannot be zero...')
except ValueError:
    print('Invalid value')









