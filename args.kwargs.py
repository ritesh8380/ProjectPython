def add(*nums) : 
    total = 0
    for num in nums :
        total += num
    return total

result = add(1,2,3,4,5,6,7,8,9,10)
print(result,end=" verrify matkar sahi hai ! ")
print()
print("------------------------------")


def display_name(*names) :
    for name in names :
     print(name,end = " ")
    print()

display_name("Ritesh","Sharma")
print("------------------------------")


def Address(**kwargs) :
   for every_keys,and_values in kwargs.items() : #Keys will be stored in kwrgs.keys() and values will be stored in kwargs.values() and both will be in kwargs.items()
      print(f"{every_keys} : {and_values}")

Address(street = "Narayan street",
        Apartment = "Dev apartment",
        City = "Nashik",
        State = "Maharashtra",
        Country = "India")
print("------------------------------")





