'''import time 
def Timer(end,start=0) :  #There should be first positonal arguments be before defaut arguments
    for x in range(start,end+1) :
       print(x)    
       time.sleep(1)
    print("Done !")
Timer(100)'''

'''def Name(title,Name,Father_name,Lastname) :
    print(f"{title} {Name} {Father_name} {Lastname}")
     
Name("Mr","Ritesh", Father_name="Jeetnarayan", Lastname ="Sharma") #if you change the order of the default arguments it will still run but not for the positional arguments ie.Ritesh,mr'''

for x in range(1,11) :
   print(x,end = " ") #Here end is default argument so here print fuction have built in default arguments place
print()

print("1","2","3","4","5",sep ="-") #default arguments ar end,sep 

