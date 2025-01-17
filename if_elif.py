import math 
info =input("What is your name ? \t")
info = bool(info)
if info == False : 
    (input("sorry no input found please type your Name : \t"))
elif info == True : 
    marks = float(input("please type your marks in maths subject :")) 
    print(f"your round off marks of mathematics is {marks}")
    if marks < 60 : 
       print("You Need To Work Hard")
    elif marks >= 60 : 
        satm = float(input("please enter your SAT marks : "))
        if satm < 60 : 
           print("Sorry you should work upon your SAT subject")
        else : 
         print("You Have crack the exam wait for your interveiw call congratulations !") 

#same block of code or related block of code should be at same level to avoid errors
# nested if alays exactly below so that compiler can understand the following is related to each other   