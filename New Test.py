
#Basic_Calculator

operand_1 = int(input("Enter Operand1: "))
operand_2 = int(input("Enter Operand2: "))

operator = input("Enter the operator (+,-,*,/): ")

if operator == "+" :
    print(operand_1+operand_2)

elif operator == "-" :
    print(operand_1-operand_2)

elif operator == "*" :
    print (operand_1*operand_2)

elif operator == "/":
    print(operand_1/operand_2)

else:
    print ("None")

print ("Thank you")
