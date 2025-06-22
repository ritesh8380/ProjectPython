rows = int(input("How many rows do you want in your rectangle :"))
columns = int(input("How many column do you want in your rectangle :"))
symbol = input("choose any symbol like @#$ for rectangle : ")
print("\n")
for y in range(1,rows+1) : #Here y stores the values y=0 then if rows is 3 it will run till 2 i.e row-1 example 3 then 0,1,2 not include 3 it will be excluded thats why (start,stop,steps)
    for x in range (1,columns+1):
           print(symbol,end="")
    print()
print("\n")
