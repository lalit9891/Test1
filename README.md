<<<<<<< HEAD
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



=======
#Task 1 checking if the number is even or odd

operand_1=int(input("Enter a number: "))
if operand_1 % 2 ==0:
    print(f"{operand_1} is an even number")

elif operand_1 % 2 |0:
    print(f"{operand_1} is an odd number")

else:
    print("none")

# Task 2 Sum of Integers from 1 to 50 Using a Loop

a = 0

for i in range(1,51):
    a += i

print(f"The sum of numbers from 1 to 50 is: {a}")


>>>>>>> 0b4ee7154ec975b181f3a54fa2bd29bf5a14d839
