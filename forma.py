price1 = 3000.14689
price2 = -4569.8832174987
price3 = 1078.994

print(f"{price1 :.2f} after decimal two numbers are displayed") 
print(f"{price1 :>20} space will be given before the number 20 character wide")
print(f"{price1 :<20} space will be given after the number 20 character wide")
print(f"{price1 :^10} space will be given before and after the number so that it appears to be centred\n")

print(f"{price1 :+} + sign will be given to the number")
print(f"{price2 :+} + sign will be given to the number")
print(f"{price3 :+} + sign will be given to the number\n")
#if we use space instead of '+' or '-' sign then same result but + sign will not appear

print(f"{price1 : } no sign will be given to the number")
print(f"{price2 : } negative sign will be given to the number")
print(f"{price3 : } no sign will be given to the number\n")

print(f"{price1 :,} comma will be given at the thousand place")
print(f"{price2 :,} comma will be given at the thousand place")
print(f"{price3 :,} comma will be given at the thousand place\n")


print(f"{price1 :+,.2f} comma,sign and thousand place specification is provided")
print(f"{price2 :+,.2f} comma,sign and thousand place specification is provided")
print(f"{price3 :+,.2f} comma,sign and thousand place specification is provided\n") 