#range function

a=list(range(0,101,10))

print (a)

a= ("Kush", 5, 1990)

for b in a:
    print(b)

for b in ("Kush"):
    print (b)
for i in range(0,11,2):
    print(i)

operand_1= int(input("Enter the First Number: "))
operator = input("Enter the function (+,-,*,/): ")
operand_2= int(input("Enter the First Number: "))


if operator == "+":
    print (operand_1 + operand_2)
elif operator == "-":
    print (operand_1 - operand_2)

elif operator == "*":
    print (operand_1 * operand_2)
elif operator == "/":
    print (operand_1 / operand_2)

else:
    print ("None")

print ("Thank You")





