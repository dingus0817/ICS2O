#File name: PseudocodeLoops.py
#Description: This program is practice for using pseudocodes and writing loops
#Author: Jamie Zhang

population = 5
RATE = 0.016
YEAR_START = 1987
YEAR_END = 2088

for year in range(YEAR_START,YEAR_END):
    population = population*(1 + RATE)
    rounded = round(population)
print("The population in the year", year, "is", rounded, "billion")




RATE = 0.01
topsoil = 30
years = 0
DOOM = 9

while topsoil >= 9:
    topsoil = topsoil*(1 - RATE)
    years = years + 1
print("It takes", years, "years until our doom")




ATTEMPTS = 3
attemptsLeft = ATTEMPTS
PIN = "0000"
guess = ""

while guess != PIN and attemptsLeft > 0:
    guess = input("Enter the PIN: ")
    attemptsLeft = attemptsLeft - 1
    if guess != PIN: 
        print("Incorrect")
        print("You have", attemptsLeft, "attempts left")

if guess != PIN:
    print("Your account has been frozen")
else:
    print("Logging in...") 




##pseudocode:
##- establish constants/variables
##- import a random integer from 1 - 3 
##- assign each integer either rock paper or scissors
##- get input from user (1 for rock, 2 for paper, 3 for scissors)
##- translate input into rock paper or scissors
##- counted loop for 5 rounds, only end loop if player gets 3 points (by winning) or 5 rounds passed
##- set a counter to keep track of the points the player earns
##- print results

points = 0
roundsLeft = 5
print("Welcome to a best-out-of-five game of Rock Paper Scissors!")
print("If you win a round, you get one point")
print("Collect three points to win")
print("Ready?") 
while (points < 3 and roundsLeft > 0):
    from random import randint
    code = randint(1,3)
    if (code == 1):
        code = "rock"
    if (code == 2):
        code = "paper"
    if (code == 3):
        code = "scissors" 
    choice = input("Please enter a number from 1 - 3 (rock, paper, scissors respectively): ")
    if (choice == "1"):
        choice = "rock"
    if (choice == "2"):
        choice = "paper"
    if (choice == "3"):
        choice = "scissors"  
    roundsLeft = roundsLeft - 1
    print("I pick", code)
    print("You picked", choice)
    if (code == "rock" and choice == "paper"):
        print("You get one point!")
        print(roundsLeft, "rounds left")
        points = points + 1
    elif (code == "paper" and choice == "scissors"):
        print("You get one point!")
        print(roundsLeft, "rounds left")
        points = points + 1
    elif (code == "scissors" and choice == "rock"):
        print("You get one point!")
        print(roundsLeft, "rounds left")
        points = points + 1
    else:
        print("You didn't get a point")
        print(roundsLeft, "rounds left")
if (points == 3): 
    print("Congrats! You won the game! 🥳")
else:
    print("You lost! 😭")
    print("But I won :D") 




