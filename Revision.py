

#Simple Calculator
'''
operand1 = float(input("Enter the First Number: "))
operator = input("please select the operator +,-,/,*: ")
operand2= float(input("Enter the Second Number: "))



if operator == "+":
    print(operand1+operand2)

elif operator=="-":
    print (operand1-operand2)

elif operator=="*":
    print(operand1*operand2)

elif operator=="/":
    print (operand1/operand2)

else:
    print ("None")

print ("Thank you")
'''
from math import factorial

'''
#even or odd

operand1 = int(input("Please enter the Number: "))
if operand1 %2==0:
    print(f"{operand1} is a Even Number")

elif operand1 %2|0:
    print(f"{operand1} is a Odd number")

else:
    print ("None")

print("Thank you")
'''
'''
def add(a,b):
    return a+b
def square(c):
    return c*c

result = square(add(5,5))

print (result)

'''

#import math
#print(math.pi)

#from math import pi
#print(pi)

#from math import *
#print (pi)

def factorial(n):
    if n<2:
        return 1

    else:
        return n*(factorial(n-1))

result = factorial(5)

print(result)








































