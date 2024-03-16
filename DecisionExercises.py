#File name: DecisionExercises.py
#Description: This program is practice for making decisions
#Author: Jamie Zhang


True and not False
True
True or True and False
True
not True or not False
True
True and not 0
True
52 < 52.3
True
1 + 52 < 52.3
False
4 != 4.0
False



mark = int(input("What is your mark? "))

if (mark >= 80):
    print("You got an A!")

else:
    print("Try again! You can do much better!") 



word = input("Guess a secret word (hint: it's my name): ")

if (word == "Jamie"):
    print("Thanks for remembering my name! :D")

elif (word == "jamie"):
    print("Thanks for remembering my name! :D")

else:
    print("Try again :(")



from random import randint
randNumber = randint(1,10)
guess = input("Guess a number from 1 to 10: ")

if (guess == randNumber):
    print("Wow, you guessed right!")

else:
    print("Nice try!") 



tickets = int(input("How many tickets would you like to buy? "))

if (tickets >= 5):
    price1 = '{:.2f}'. format(round(tickets*8.95, 2))
    print("The cost for each ticket will be $8.95 and the total cost will be", price1)

else:
    price2 = '{:.2f}'. format(round(tickets*12.50, 2))
    print("The cost for each ticket will be $12.50 and the total cost will be", price2)



q1 = input("Do you have some money? (Yes or No): ")
q2 = input("Are you free tonight? (Yes or No): ")

if (q1 == "Yes" and q2 == "Yes"):
    print("Ok then, let's go to the movies!")

elif (q1 == "Yes" and q2 == "No"):
    print("Maybe we can go to the movies another time.")

elif (q1 == "No" and q2 == "Yes"):
    print("Well I guess it's another study night instead of the movies.")

else:
    print("Aw ok then.")
    


n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))

smallest = min(n1, n2, n3)
print("The smallest number out of the three numbers is", smallest)



age = int(input("What is your age? "))

if (13 <= age <= 64):
    print("The cost for your ticket is $28")

elif (age >= 65):
    print("The cost for your ticket is $23")

else:
    print("The cost for your ticket is $18")



emotion = input("How are your feeling today? ")

if (emotion == "tired" or emotion == "sleepy"):
    print("Maybe you should go to bed early.")

elif (emotion == "sad"):
    print("Maybe try smiling! :D")

elif (emotion == "happy"):
    print("Then let's go to a party!")

else:
    print("Sorry, I don't know what you mean. After all, I'm just a computer, haha!")



action = input("Enter an action and I will output a response to that choice (sing, laugh, etc): ")

if (action == "sing"):
    print("la la la")

elif (action == "cry"):
    print("boo hoo")

elif (action == "laugh"):
    print("HA HA HA")

elif (action == "eat"):
    print("nom nom")

elif (action == "draw"):
    print(":D OwO UwU OvO <3")

else:
    print("nvm that's too much work lmao")

    

#get input from user     
rate = float(input("Enter the hourly rate of pay: "))
hours = float(input("Enter the number of hours worked: "))

print("a = 0%\nb = 10%\nc = 20%\nd = 29%\ne = 35%")
taxLetter = input("Enter the tax deduction letter: ")

#complex decision to convert tax 
if (taxLetter == "a"):
    tax = 0

elif (taxLetter == "b"):
    tax = 0.1

elif (taxLetter == "c"):
    tax = 0.2

elif (taxLetter == "d"):
    tax = 0.29

else:
    tax = 0.35

#simple decision on gross amount 
if (hours > 40):
    gross = hours*(2*rate)

else:
    gross = round(hours*rate,2)

#calculations
deduction = round(gross*tax, 2)
net = gross - deduction

#output
print("The gross pay, tax deductions, and net pay respectively are "+ str(gross) + ", " + str(deduction) + ", " + str(net))
