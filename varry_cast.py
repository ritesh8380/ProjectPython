#Varriable : containers for the value (string,integer,float,boolean)

#1.strings : combination of different data types.(always in comma)
My_mail = "Ritezh8380@gmail.com"
print(type(My_mail))

#2.integers : not in commas.
CGPA = 10
print(type(CGPA))

#3.float : Decimal numbers.
actual_marks = 99.60
print(type(actual_marks))

#4.boolean : either true or false.  
is_student = False 
print(type(is_student))

if is_student : print("The user is student")
else: print("access denied\n")


#Typecasting :int(),float(),bool(),str().
Name = "Ritesh Sharma"
print(type(Name))
Name = bool(Name)
print(Name) 
#This will print True for any letter present in the string Name but if empty it will print false.

My_Marks = 10.89
print(type(My_Marks))
My_Marks = int(My_Marks)
print(My_Marks)

My_Marks=float(My_Marks)
print(type(My_Marks))
print(My_Marks)

