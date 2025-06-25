capitals = {"INDIA" : "NEW DELHI","CHINA" : "beijing","USA" : "Washington D.C"}

while True :
   entry = input("Please enter the country name i will tell you capital of that country (q for quit) and (a to contribute):").upper()
   
   if entry == "Q" :
         print("Exiting the program...")
         break
   elif entry == "A" :
       add_country = input("Enter country name : ").upper()
       add_capital = input(f"Enter the capital of {add_country} : ")
       capitals[add_country] = add_capital #only for single entries and dictionary.upadate({"keys","values"}) for mumltiple keys and values
       print(f"your {add_country} and its capital {add_capital} has been added successfully !")
       print()
       print("The current capitals an the country in dictionnary are :")
       for country,capital in capitals.items() :
                    print(f"{country} : {capital}")
       print()
       break
    
   else:
       result = capitals.get(entry)
    
       if result :
           print(f"{result} is the capital of {entry}.") 
       else :
        print("sorry , I dont have the capital for {entry}.")