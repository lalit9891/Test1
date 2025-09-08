
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








