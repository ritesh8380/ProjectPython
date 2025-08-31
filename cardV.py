sum_odd_digits = 0  #Initialization of the varriables
sum_even_digits = 0
total = 0 

card_number = input("Enter the card number : ") 
card_number = card_number.replace("-","")
card_number = card_number[::-1]  # [start:end:step]
# print(card_number)

for number in card_number[::2] :
    sum_odd_digits += int(number)

for number in card_number[1::2] : #start = 1 and second step
    number = int(number)*2  #double the integer
    if number >= 10 :
        sum_even_digits += (1+(number%10)) # 1 + (number%10) = modulus 
    else :
        sum_even_digits += number
    
total = sum_odd_digits + sum_even_digits

if total % 10 == 0 :
    print("VALID")
else :
    print("INVALID")
