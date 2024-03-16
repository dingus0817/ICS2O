#File name: SchoolBusCalculator.py
#Description: This program calculates the transportation cost and other costs using inputed data and then outputs the relevant information
#Author: Jamie Zhang
#Date: March 2, 2023

FIXED = 425
VARIABLE = 3.95
CAPACITY = 47 

#user input
hourStart = abs(int(input("Enter the hour when the trip starts in 24h format(eg. 15 but not 3PM): ")))
minStart = abs(int(input("Enter the minutes when the trip starts: ")))
hourEnd = abs(int(input("Enter the hour when the trip ends in 24h format: ")))
minEnd = abs(int(input("Enter the minutes when the trip ends: ")))
numStudents = abs(int(input("Enter the number of students: ")))

#putting into time format
if (minStart < 10):
    minStartForm = "0" + str(minStart)
else:
    minStartForm = str(minStart)

if (minEnd < 10):
    minEndForm = "0" + str(minEnd)
else:
    minEndForm = str(minEnd)
    
timeStart = str(hourStart) + ":" + minStartForm
timeEnd = str(hourEnd) + ":" + minEndForm

#calculate duration 
if (hourStart > hourEnd):
    hours = abs((hourStart - hourEnd) - 24)
else:
    hours = abs(hourStart - hourEnd)
    
minutes = abs(minStart - minEnd)

if (minStart > minEnd):
    hours = hours - 1

#number of buses calculation
numBus = numStudents/CAPACITY
if (numBus is float(numBus)):
    numBus = int(numBus) + 1

#cost calculations
timeFraction = hours + (minutes/60) 
transportCost = round((FIXED*numBus + numBus*(VARIABLE*timeFraction)),2)
studentCost = round(transportCost/numStudents, 2)

#output the results
if (hourStart > 24 or hourEnd > 24):
    print("Please enter a number less than 24 for the hour next time")

elif (minStart > 59 or minEnd > 59):
    print("Please enter a number less than 59 for the minute next time")

elif (hourStart == 0 or hourEnd == 0):
    print("Please enter a number that's not 0 for the hour next time")

else:
    print("The number of students is", numStudents)
    print("The transportation cost is $", transportCost)
    print("The cost for each student is $", studentCost)
    print("The time that the trip started is", timeStart)
    print("The time that the trip ended is", timeEnd)
    print("The duration of the trip is", hours, "hours,", minutes, "minutes")

