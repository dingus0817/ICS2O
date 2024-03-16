#File name: CounterAccumulatorExercises.py
#Description: This program is practice for using counters and accumulators
#Author: Jamie Zhang


#sum of all digits between 1 - 50 
total = 0 
for counter in range(1,50):
    total = total + counter 
print(total) 


#the mean of the numbers between 4 - 15 
total = 0
for counter in range(4,15):
    total = total + counter
average = total/(15-4) 
print(average)


#the mean of the numbers in the range the user inputs 
total = 0
x = int(input("Enter the beginning of the range: "))
y = int(input("Enter the end of the range: "))
for counter in range(x,y):
    total = total + counter
average = total/(y-x)
print(average)


#counts the number of votes for each party 
tallyL = ""
tallyC = ""
tallyN = ""
tallyG = ""
counter = "|"
for count in range(20):
    vote = input("Which party did you vote for? (L, C, N, G): ")
    if (vote == "L"):
        tallyL = str(tallyL) + counter
    elif (vote == "C"):
        tallyC = str(tallyC) + counter
    elif (vote == "N"):
        tallyN = str(tallyN) + counter
    else:
        tallyG = str(tallyG) + counter
print("L:", tallyL)
print("C:", tallyC)
print("N:", tallyN)
print("G:", tallyG)



#one wiggly line 
#emily a helped
from random import randint
count = 50
while True:
    number = randint(0,1)
    if number == 0:
        count = count + 1;
    if number == 1:
        count = count - 1;
    print(" "*count + ".oOo.")



#twin wiggly lines
#copied from emily a
from random import randint
space1 = 50
space2 = 50

while True:
    direction1 = randint(0,1);
    if space1 <= 10:
        space1 = space1 + 1
        space2 = space2 - 1
    elif space1 >= 70:
        space1 = space1 - 1
        space2 = space2 + 1
    else:
        if direction1 == 0:
            space1 = space1 - 1
            space2 = space2 + 1
        if direction1 == 1:
            space1 = space1 + 1
            space2 = space2 - 1
            
    direction2 = randint(0,1)
    if space2 <= 10:
        space2 = space2 + 1
    elif space2 >= 70:
        space2 = space2 - 1
    else:
        if direction2 == 0:
            space2 = space2 - 1
        if direction2 == 1:
            space2 = space2 + 1
    print(space1*" ", ".oOoOo.", space2*" ", ".oOoOo.")
    
    
    
