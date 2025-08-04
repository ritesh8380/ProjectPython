import random
option = ["rock","paper","scissor"]
computer_choice = random.choice(option) 
rounds = int(input("How many rounds do you want to play ? :"))

computerscore = 0
Playerscore = 0

for round_num in range(1,rounds + 1):
 print(f"\nRound {round_num}")
 print("---------------------------------------------------------------------------")
 your_choice = input("lets play rock,paper and scissor press q to quit YOUR Choice : ").lower()
 print(f"Your choice : {your_choice} and computer choice : {computer_choice}")
 print("----------------------------------------------------------------------------")

 if(your_choice == "q") : 
    print("thanks for your Time hope you will play again !")
    break
 
 elif(computer_choice == your_choice) :
   print("IT'S TIE !")
 
 elif(your_choice not in option) :
   print("Invalid input please enter either Rock paper or scissor !")
 
 elif(your_choice == 'rock' and computer_choice =='paper') or \
     (your_choice == 'paper' and computer_choice =='scissor') or \
     (your_choice == 'scissor' and computer_choice =='rock') : 
    print("computer won this Round !")
    computerscore += 1
    continue
 else :
   print("well done you won this round !")
   Playerscore += 1
print(f"Computer score = {computerscore} and your score = {Playerscore}")

