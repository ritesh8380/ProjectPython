
while True : #as we all know that loop will execute only if its true (we by default created a loop which will always true or always execute)
    principal = float(input("Enter the principal amount you have invested :"))
    if principal < 0 :
        print("principal amount cannot be negative !")
    else :
        break

while True :
    Rate = float(input("Enter the Rate of interest :"))
    if Rate < 0 :
        print("Rate of interest cannot be negative !")
    else :
        break

while True :
     time = float(input("Enter for how many years you are investing the money :"))
     if time < 0 :
        print("Time cannot be negative !")
     else :
         break
         

final_amt = principal*pow(1+Rate/100,time)
print(f"you will get {final_amt :,.2f} after {time} years")

           