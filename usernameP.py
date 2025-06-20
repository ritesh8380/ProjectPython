username = input("entr your Username :") #initialization of the username
if len(username) >= 12 :
    print("Username is too long, please enter a username with 12 characters or less.") #username should not greater than 12
elif username.find(" ") != -1 :
    print("username cant contain spaces") 
#Important logic here the find fuction will find the space and designate a number in positive so if space found  let suppose at 4 so 4 != -1 hence true and code will further get execute  but why only -1 it is default behaviour of python function find i.e if found then index otherwise it will return -1
elif not username.isalpha() :  
    print("username cant contain integers")
else :
    print(f"Welcome your username is {username}")