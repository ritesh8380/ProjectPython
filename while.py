import math

principle = input("plase tell me the amount you have invested : ")
while principle == "" :
    print("Principle amount is empty please enter valid input!\t")
    input("please enter the amount you have invested :\t ")
print(f"your principle amount is {principle} which you have invested in our organization !\n")
principle = int(principle)

Rate = input(f"at what rate {principle} will increase in percent form : ")
while Rate == "" :
    print("Rate is empty please enter valid input!\t")
    input("please enter the rate of growth at which you have invested in percentage form :\t ")
print(f"your principle amount is {principle} and  at {Rate}% you have invested in our organization !\n")
Rate = float(Rate)

time = input(f"for how much durration you have invested {principle} amount : ")
while time == "" :
    print("time is empty please enter valid input!\t")
    input(f"please enter the durration of the {principle} you have invested in (years) :\t ")
print(f"your principle amount is {principle} and at {Rate}% you have invested in our organization for {time} years !\n")
time = float(time)
correction = input("if the above data is correct then please enter 'y' for further process otherwise 'n' \n")

final_amt = principle*pow((1 + (Rate/100)),time)

if correction == "y" : print(f"the final amount you will recieve on your {principle} rupees for {time} years at {Rate}% interest rate is {final_amt} Rupees Thanks !")
elif correction == "n" : 
    principle = float(input("principle amount : "))
    Rate = float(input("Rate of interest : "))
    time = float(input("Time or Durration : "))
    final_amt = principle*pow((1 + (Rate/100)),time)

print(f"This is your Return of investment : {final_amt:,.2f} in rupees")




