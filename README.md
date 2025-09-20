
#Task 1

n= int(input("Enter a number: "))



def factorial (n):
    if n<2:
        return 1

    else:
        return n*(factorial(n-1))

result =factorial (n)

print(f"Factorial of {n} is: {result}" )


#Task 2

n = int(input("Enter a number: "))

import math


sqrt = math.sqrt(n)
ln=math.log(n)
sine=math.sin(n)
print("Square root: ", sqrt)
print("Logarithm: ", ln)
print("Sine: : ", sine)


