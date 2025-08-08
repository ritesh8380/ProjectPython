Alternative = input("Chose the operation(+,-,*,/) yo want to perform : ")


def add() :
    a = int(input("Whats your first number :"))
    b = int(input("Whats your second number :"))
    return a + b


def subtract() :
    a = int(input("Whats your first number :"))
    b = int(input("Whats your second number :"))
    return a - b


def multiply() :
    a = int(input("Whats your first number :"))
    b = int(input("Whats your second number :"))
    return a * b



def devide() :
    a = int(input("Whats your first number :"))
    b = int(input("Whats your second number :"))
    return a / b


if (Alternative == "+"):
    result = add()
    print(f"Addition is : {result}")

elif(Alternative == "-"):
    result = subtract()
    print(f"Subtraction is : {result}")
    
elif(Alternative == "*"):
    result = multiply()
    print(f"Product is : {result}")

elif (Alternative == "/"):
    result = devide()
    print(f"division is : {result:.2f}")
else : 
   print("please enter the valid input !")

