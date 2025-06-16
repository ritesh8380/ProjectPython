num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*",0,"#"))

for row in num_pad : #outer loop
 for num in row : #inner loop
  print( num ,end = " ") #part of inner loop
 print() #part of outer loop

#Here we can say that what is happeining here
# 1.Tuple is declared and making  four tuple representing 4 rows
# 2.Now Ist loop will execute and run for each row i.e 4 times
# 3.Then This will run for each number
# 4.end = " " space will be given after each number
# 5.At the last the new line will be given for each row completion 