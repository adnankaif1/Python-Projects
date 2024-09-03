operator = input("Enter an operator ( + - * /): ")
num1 = float(input ("Enter Number 1:"))
num2 = float(input ("Enter NUmber 2:"))

if operator == "+":
    print (num1 + num2)
elif  operator == "-":  
    print(num1 - num2)
elif operator == "*":
    print (num1 * num2)
elif operator == "/":
    result = num1 / num2
    print( round(result, 3))
else:
    print (f" {operator} is not a valid operator")
