# LEGB (Local)-->(Enclosed)--->(Global)---->(Built-In)
import math
def name1():
    name = "Local for num1"
    print(name)

def name2() :
    name = "Local for num2"
    print(name)

name1() #BOTH ARE PRINTING NAME BUT DIFFERENCE IS THAT BOTH FUNCTION HAVE DIFFERENT NAMES VARRIABLE
name2() 
print()
print("-------------------------------------------------------")

def greet(name): 
    inner = "Enclosed" 
    
    def Birthday() :
        print(f"This is {inner},and the name is {name} !")
    return Birthday

greeting = greet("Raj")

greeting()

#here Both fuctions are as one so the whole varriables in the function can be accessed but data vanishes as the fuction ran 
print("------------------------")
varriable = "math.e"
varriable2 = math.e
print(varriable) #Global varriable
print(varriable2)  #Built in varrable

from example import Square
Result = Square(2)
print(f"{Result}")



