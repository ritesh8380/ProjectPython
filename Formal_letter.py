name = str(input("position/designation or name of the person :"))
orgname = str(input("whats the Name of the organization/institution :"))
address = str(input("whats the address of the organization/institution :"))
subject = str(input("whats the objective express in short : "))
salute = str(input("Salution like dear sir/mam or respected sir/mam : "))
main_body = str(input("Input the Main body please express your problem in 20-30 words\n"))
print()
print("Sorry for the few more questions now your information is required !")
s_name = str(input("whats your name :"))
s_add = str(input("what is your address :"))
date = str(input("Date in dd-month-year format :"))


print()
print("To",end = ",\n" )
print(name,end = ",")
print()
print(orgname,end = ",")
print()
print(address,end = ",\n")
print()
print(f"Subject: {subject}")
print()
print(salute,end = ",\n")
print(main_body,end = ".\n")
print()
print("Hope you Will understand my problem and will take necessary action as soon as possible.")
print()
print("yours faithfully")
print(s_name)
print(s_add)
print(date)