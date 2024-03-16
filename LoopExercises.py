#File name: LoopExercises.py
#Description: This program is practice for coding loops
#Author: Jamie Zhang 



while True:
    print("Have a good day")


name = input("What's your name? ")
while True:
    print(name)



num = float(input("Enter a number: "))
from math import sqrt
while (num > 0):
    print(sqrt(num))
    num = float(input("Enter a number: "))



l = int(input("Enter the length: "))
w = int(input("Enter the width: "))
while (l > 0 and w > 0):
    area = l*w
    print(area)
    l = int(input("Enter the length: "))
    w = int(input("Enter the width: "))



subject = input("Enter a subject: ")
mark = input("Enter your mark: ")

while (subject != ""):
    print("Okay, cool")
    subject = input("Enter a subject: ")
    mark = input("Enter your mark: ")
print("\nWhat a relief I thought youd never stop hahahahahaha\n")



print("Welcome to the coin toss simulator program!")
from random import randint
result = False
while (result == False):
    number = randint(0,1)
    guess = input("heads or tails? ")
    
    if (guess == "heads" and number == 0):
        result = True

    elif (guess == "tails" and number == 1):
        result = True

    else:
        result = False 
        print("Try again")
print("You guessed correct!")


    
    





