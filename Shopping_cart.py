menu = { "PIZZA":50,   #Dictionary initaialization#
        "CRAX":40,
        "VADAPAV" : 20,
        "NACHOS":10,
        "PRINGLES" :350,
        "LITTI":20 }

cart = []  #cart empyty cart
total = 0  #total is initialized to zero

print()
print("----------------Welcome this is Menu---------------")
for key,value in menu.items() :    #menu.items() have keys and values of the dictionary in tuples form
    print(f"{key}: ${value:.2f}")
print("----------------------------------------------------")

while True :
  orders = input("Enter your order please : ").upper()
  if orders == "Q" :
     print()
     print("Thanks we are processing your bill please wait...")
     break
  elif menu.get(orders) is not None : #if key is not in the dictionary the value will be None
     cart.append(orders)

for order in cart :
   total += menu.get(order) #menu.get(order) values of the order is stored in this

print()
print("--------your orders----------")
for order in cart : #here the order for each order this will run means for loops we should use singulars not in plurals
   print() 
   print(order,end = " ")
print()
print("-------------------------------")
print(f" Total amount is : ${total :.2f}")
print("-------------------------------")


