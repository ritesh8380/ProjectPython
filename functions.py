'''def Function_name(parameter) :
    print(f"When you call me i will appear with parameter {parameter}")

Function_name("Ritesh")'''

def ID_card() :
    name = input("Whats your name : ")
    department = input("whats you department : ")
    cgpa = float(input("Whats your cgpa in First year : "))
    print()
    print(f"Hii {name} of {department} department and congratulations for {cgpa:.2f} cgpa your  ID card has been generated you can go and collect it from department Have a nice day !")
    print()

ID_card() #dont pass parameters if you are taking from user