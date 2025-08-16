def circum(radius) :
    pi = 3.14
    return 2*pi*radius

def Areasquare(side) :
    return side*side

def Square(num) :
    return num ** 2

def Cube(num) :
    return num ** 3 

Result = Cube(3) 
print(f"Result")

if __name__== "__main__" :
    print("Finally you called me!") 
#So here __name__ is default created in python when you run the programme using python command the __name__ = "__main__"
# but when you import the file or module __name__ = "file_name"