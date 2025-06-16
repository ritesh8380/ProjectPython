#List[] : Ordered and changeable. Duplicate OK 

fruits = ["apple","pineapple","lime","Mango"]
for fruit in fruits :
       print(fruit)
print(f"'{len(fruits)}' is the number of elements in the list ")
print(f"'{fruits[0]}' is the first element in the list")  
print(f" {fruits[::-1]} listed in oppo order\n")

for fruit in fruits :
       print(fruit)
print() 
# This is the block of code which interpretes for fruit till range fruits

print("apple" in fruits)
print()
# give output in boolean form like true if apple in the list otherwise false 
fruits[0] = "pear"
print(f"This is first fruit of the list '{fruits[0]}'\n")
fruits.append("pineapple")
#append i.e will join the pineapple in the list
fruits.remove("pear")
#remove this will remove the pear element from the list
fruits.insert(0, "apple")
# will add the apple element in the list or we can say insert
fruits.sort()
# Alphabetical order
fruits.reverse()
#Reverse the list from current condition
# fruit.clear()
#elements gone or cleared out
print(f"{fruits.index('apple')} the index or the position of the apple")
print(f"{fruits.count('apple')} This will print the counting of the apple entry")