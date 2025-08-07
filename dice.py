import random

dice_art = { #dictionary as well as tuple is initialized
    1:(  "┌──────────┐",
         "│          │",
         "│    ●     │",
         "│          │",
         "│          │",
         "└──────────┘" ),
    2:(
         "┌──────────┐",
         "│ ●        │",
         "│          │",
         "│          │",
         "│        ● │",
         "└──────────┘"),
    3:( 
         "┌──────────┐",
         "│  ●       │",
         "│    ●     │",
         "│       ●  │",
         "│          │",
         "└──────────┘"),
    4:(
         "┌──────────┐",
         "│  ●   ●   │",
         "│          │",
         "│  ●   ●   │",
         "│          │",
         "└──────────┘"),
    5:(
         "┌──────────┐",
         "│ ●      ● │",
         "│     ●    │",
         "│          │",
         "│  ●     ● │",
         "└──────────┘"),
    6:(  "┌──────────┐",
         "│          │",
         "│ ●      ● │",
         "│ ●      ● │",
         "│ ●      ● │",
         "└──────────┘")
} #dictionary has been initialized 

dice = [] #list of dice has been created
total = 0
num_of_dice = int(input("Tell me the no. of dice : "))

for die in range(num_of_dice) : #python dont know the grammer die or dim or even ritesh will also considered
    dice.append(random.randint(1,6))

'''for die in range(num_of_dice) :
    for each_tuple_element in dice_art.get(dice[die]): #only access values 
        print(each_tuple_element)'''

for each_line_tuple in range(6) :
    for die in dice :
        print(dice_art.get(die)[each_line_tuple],end="") #Here each_line_tuple is used to print at each line 
    print()
for die in dice :
    total += die #sum up every die values  
print(f"Total : {total}")

