# 1.len(name) : length of the string with space example length of the name (correct)
user = input("Please enter your USERNAME : \t")
user = len(user)
print(f" \"{user}\" This the no. of Members including space")

# 2.name.find("a") : it will find for 'a' in the string and tell the position in numeric form and if no then -1 will be output and 0,1,2,,string (correct)
use = input("Tell me the word to find the 'r' letter ?\n")
finder = use.find("r")
print(f"{finder} This is the position of \"r\" with space ")

#3.name.rfind("o") : find for o from reverse side 
esu = input("Tell me the word to find the 'r' letter reversely ?\n") 
sfind = esu.rfind("r")
print(f"{sfind} This is the position of \"r\" with space") 

#4.name.capitalize() : first letter always capital form
Use = input("Tell me the word I will capitalize the first letter?\n")
Finder = Use.capitalize()
print(f"{Finder} This is the capitalization ")

# 5.name.upper() or name.lower() : to make the string upper or lower case
USE = input("Tell me the word I will Upper case the string?\n")
FINDER = USE.upper() 
print(f"{FINDER} This is the upper cased string") 

use = input("Tell me the word I will Lower case the string?\n")
finder = use.lower()
print(f"{finder} This is the lower cased string") 

#6.name.isdigit() : if only number then true otherwise false
Input = input("Provide the input i will analyze for digit :\t")
output = Input.isdigit()
print(f"{output}") 

#7.name.isalpha() : if only alphabet then true otherwise false
name = input("Alphabetical input please :\n")
naam = name.isalpha()
print(f"{naam}")

#8.name.count("*"):Counts the star character in string
gin = input("Enter the string contains the * character :\n")
gin_liya = gin.count("*")
print(f"{gin_liya} no. of * character in the string")

#9.name.replace('from','to this') Replaces the character or text from the string
change = input("Tell me the string for replacemet :\n")
changed = change.replace('*',' ')
print(f"{changed} is the replaced string")


