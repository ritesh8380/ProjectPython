user = input("Please enter your username : \t")
if len(user) > 12 : 
    print("Username cannot exceed 12")
elif not user.find(" ") == -1 :
    print("Your username can't contain spaces")
    # here not will reverse the result if -1 which means not found but not operator is making it that found spaces
elif not user.isalpha() : 
    print("username cannnot contain any numbers")
else : 
    print(f"your username is {user} welcome to our webportal")
    print("Now set the password please")
    pwd = input("please enter the password :\t")
    if len(pwd) > 12 : print("password cannot be more than 12 characters")
    elif pwd.find("*") and pwd.find("@") and pwd.find("#") and pwd.find("$") == -1  : 
        print("please insert any special characters at the begining like *#$@")
    elif pwd.find(" ") == -1 :
        print("password should contain spaces for extra security")
    else:
        print("Password set successfully") 
    