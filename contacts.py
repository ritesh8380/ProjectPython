contact = { "Ritesh":"ritezh8380@gmail.com",
           "Robot":"eye831@gmail.com",
           "Harsh":"Harshedu@gmail.com"}

Name = input("Type Name for informations :")
if Name in contact :
    print(f"This is email id :{contact[Name]}")
elif Name not in contact :
     ans = input(f"Tell me the email id for {Name} it not in our data station : ")
     contact[Name] = ans
     print(f"email id for {Name} is \"{contact[Name]}\" successfully registered !")
     print()

print("-------------------------")
print("The current data is :")
for key,value in contact.items() :
     print(f"{key}:{value}")
print("-------------------------")
