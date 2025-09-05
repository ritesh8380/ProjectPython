class Engineer :   #Class is engineer#

    count = 0 

    def __init__(self,name,cgpa) : #self is constructor __init__ is important#
        self.name = name           #name and cgpa are parameters#
        self.cgpa = cgpa
        Engineer.count += 1         # after fuction runs the count increases#
    def __str__(self):
        return f"The Engineer is {self.name} and with cgpa {self.cgpa}"  #output of the class  will be stored into Engineer varriables#
    
E1 = Engineer('Ritesh','9.82')  #Function calling#
E2 = Engineer('Rakesh','8.82')
E3 = Engineer('Virat','9.62')
E4 = Engineer('Ranvijay','9.00')
print(E1)
print(E2)
print(E3)
print(E4)
print(f"Total no. of engineers are {Engineer.count}")