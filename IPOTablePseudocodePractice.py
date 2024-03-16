#File name: IPOTablePseudocodePractice.py
#Description: This program is practice for using IPO tables and pseudocodes 
#Author: Jamie Zhang

CALORIES = 225
JOGGING = 1/100

#user input
name = input("What is your full name? ")
pieces = float(input("How many pieces of cake have you eaten? "))

#calculations
cals = pieces*CALORIES
distance = round(cals*JOGGING, 1)

#output
print(name, "you need to jog", distance, "km.")


