questions = (
("What is capital of Maharashtra"), #Definition of 2d list
("What is the capital of Bihar") )

options  =(
("A.Mumbai","B.Nashik","C.Bhusawal","D.Jalgaon"),
("A.Patna","B.Sasaram","C.Ranchi","D.Bhabhua")
)

answers = ("A","A")
guesses = []
scores = 0
question_num = 0

for question in questions :
    print(question)
    for option in options[question_num]:
     print(option)
     print("-------------------------")
    guess = input("Enter your answer: ").upper()
    guesses.append(guess)
    
    if guess == answers[question_num] :
     print("correct")
     scores += 1
    else :
     print(f"Incorrect! \n {answers[question_num]} is the correct answer")
     
    question_num += 1

print("your guesses :")
for guess in guesses:
    print(guess,end = " ")
print()

print("The Answers :")
for answer in answers :
   print(answer,end =" ")
print()
scores = int(scores / len(questions)*100)

print(f"your score is {scores}%")








    





    