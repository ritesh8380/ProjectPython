Multiplication_tabels =[]
y = int(input("Whose table you want : "))
for x in range(1,11) :
    Multiplication_tabels.append(x*y)

print(Multiplication_tabels)
print()
print("---------------------------------")

Apple_Box = [9.82,9.72,9.80,8.82]
Passing_Apples = [Apple for Apple in Apple_Box if Apple <= 6.0]  #[return/put in iterable for loop condition (so that all elemets can be checked) and if condition]
print(Passing_Apples)

#The above list will [Returns-Apple if matched condition,All the appples should be checked,Condition for those apples which will not be into the list]
