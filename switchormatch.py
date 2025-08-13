def switch_board(switch):
    match switch:
        case 1 :
            print("Switch 1 is on")
        case 2:
            print("Switch 2 is on")
            
        case _:
           print("No switch found please check !")  # Default case for invalid input

switch = int(input("Enter the switch number : "))
switch_board(switch)

def is_weekend(day) :
     match day :
         case "Monday" | "Tuesday" |"Wednesday" |"Thursday" | "Friday" :
             return False
         case "Saturday" | "Sunday" :
             return True
         case _: print("Please enter valid input !")

day = input("Tell me the day i will tell you about holiday : ")
print(is_weekend(day)) 

def is_weekend(day) : 
     match day :
         case "Monday" | "Tuesday" |"Wednesday" |"Thursday" | "Friday" :
             print("No Holiday today !")
         case "Saturday" | "Sunday" :
             print("Yes Rest time no work today !")
         case _: print("Please enter valid input !")

day = input("Tell me the day i will tell you about holiday : ")
is_weekend(day)

