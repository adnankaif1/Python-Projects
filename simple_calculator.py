#Simple Method-----------------
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


#Another code ------------------------- Another code with defination method


#Calculator
def add (x, y):
    return x+y

def minus ( x, y):
    return x-y 

print("Select option")
print ("1.add")
print ("2.minus")

while True:
    Select = input("slecct number (1.Addition/ 2.Minus):") 
    if Select in ('1','2'):
        try: 
            num1 = int(input ("Enter Number 1:")) 
            num2 = int(input("Enter Number 2:") ) 
        except:
            print ("Invalid number")
            continue
        if Select == '1':
            print (add(num1, num2))

        elif Select == '2':
            print (minus (num1, num2))

        next_calculation = input ("yes/no:")   
        if next_calculation == "no":
            break

    else:
        print("Invalid numbers")            
