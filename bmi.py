import math
wt = float(input("what is your weight in (kg):\t"))
if not wt : 
   print("invalid input !")
else :   
    Ht = float(input("what is your Height in (cm): \t"))
    if not Ht : 
      print("invalid input !")
    else:
        bmi = round(wt / pow(Ht / 100, 2), 2)
    print(f"The body Mass index is : {bmi} kg/m^2")
    
    if 18.5 <= bmi <= 25:
        print(f"{bmi} is Healthy Body mass index. Be happy, live long, and continue exercising.")
    elif bmi <= 25 :
        print(f"{bmi} is Healthy Body mass index Be happy live long continue exercise")
    else : 
        print(f"{bmi} is Unhealthy Body mass index Be happy live long continue exercise")
    






