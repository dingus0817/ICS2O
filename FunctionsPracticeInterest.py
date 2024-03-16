#File name: FunctionsPracticeInterest.py
#Author: Jamie Zhang

import random

def interestRate():
    rate = (random.randint(325,576))/10000
    return rate
def simpleInterest(P,r,t):
    interest = P * r * t
    return interest
def compoundInterest(P,t):
    interest = P *(1 + (0.05/2))**(2*t)
    return interest

borrowed = int(input("enter how much money you have borrowed: "))
years = int(input("enter how many years you have borrowed the money: "))
option = input("do you want simple or compound interest (enter 1 or 2): ")

if option == "1":
    rate = interestRate() * 100
    interest = simpleInterest(borrowed,rate,years)
elif option == "2":
    rate = 5
    interest = compoundInterest(borrowed,years)
else:
    print("hm")
print("the amount of interest you owe at the rate of", rate, "% is:", round(interest,2))
