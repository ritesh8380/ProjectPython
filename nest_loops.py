rows = int(input("How many rows do you want in your rectangle :"))
columns = int(input("How many column do you want in your rectangle :"))
symbol = input("choose any symbol like @#$ for rectangle : ")
print("\n")
for y in range(rows) :
    for x in range (columns):
           print(symbol,end="")
    print()
print("\n")
