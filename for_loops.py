import time 
count = int(input("Time for how much seconds :\t"))
for x in range(count,0,-1) :
    seconds = x % 60 
    #This is remainder block of code 
    minutes = int(x/60) % 60
    #To convert seconds in minutes we devide the seconds with 60 
    hours = int(x/3600)
    #To convert the seconds in hours we devide the seconds with 3600 
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("TIME'S UP!") 
