def Shipping_address(*names,**Address) : #defined the kwargs and args but args are positionaly arguments which have fix value and fix order
   for name in names :
      print(name,end = " ") #It will print the name as it is in the names tuple
   print()
   print("-------------------------------------------------------------------------------")
   '''for pata in Address.values(): #Address.values only consist of values not keys of that 
    print(pata,end = " ")'''
   
   print(Address.get('street'),end =" ") #Default first line
   
   if "Apartment" in Address :
     print(f"{Address.get('street')}")
     print(f"{Address.get('landmark')},{Address.get('city')},{Address.get('country')}-{Address.get('Postal')}")  #Apartment removed
   elif "Postal" in Address :
     print(f"{Address.get('street')}")
     print(f"{Address.get('landmark')},{Address.get('city')},{Address.get('country')},{Address.get('Apartment')}") #Postal removed
   
   else :
     print(f"{Address.get('street')}")
     print(f"{Address.get('landmark')},{Address.get('city')},{Address.get('country')}") 
     

Shipping_address("Mr","Ritesh","Jeetnarayan","Sharma",
                 street="Old datta mandir",landmark="gokuldham society",city="Mumbai",country="India",Apartment ="sai shraddha appartment",Postal ="432994")
print()