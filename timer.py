import time

my_time = int(input("Enter time in seconds : "))

for  x  in range(my_time,0,-1):
    seconds = x%60
    minutes = int(x/60)%60
    Hours = int(x/3600)
    print(f"{Hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("time is up !") 