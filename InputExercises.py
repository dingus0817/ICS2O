#File Name: InputExercises.py
#Description: This is practice for inputting
#Author: Jamie Zhang


colour = input("What is your favourite colour? ")
print(colour + ".")


name = input("What is your name? ")
subject = input("What is your favourite subject? ")
print(name + ".",subject + ".")


firstName = input("What is your first name? ")
lastName = input("What is your last name? ")
print("Hello", firstName, lastName + ".", "How are you?")


name = input("Your name:" )
street = input("Street:" )
city = input("City:" )
province = input("Province:" )
postalCode = input("Postal code:" )
print("Address of", name + ":", street + ",", city + ",", province + ",", postalCode + ".")


num1 = int(input("input a number: "))
num2 = int(input("input another number: "))
print(num1*num2)


number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))
print("The sum of the numbers is", number1+number2)
print("The difference of the numbers is", number1-number2)
print("The product of the numbers is", number1*number2)
print("The quotient of the numbers is", number1/number2) 

inch = 2.54
length = float(input("Enter the length of a door in inches:" ))
answer = length*inch
print("The length from inches to centimetres is", answer)

subject = input("What is the subject?" )
total = int(input("Enter the total number of marks on the test:" ))
mark = float(input("Enter your marks:" ))
percent = round(mark/total, 1)*100
print("Subject:", subject)
print("You got", str(percent) + "%", "on your test.")

radius = float(input("Enter a radius for a circle: "))
pi = 3.14159
diameter = radius*2
circumference = round(pi*diameter, 3)
print("The circumference of the circle rounded to three decimal places is " + str(circumference))

print("You are investing money in a savings account with simple interest.")
principal = int(input("Enter your principal amount: "))
rate = float(input("Enter an interest rate: "))
time = int(input("Enter in years how long you want to invest: "))
interest = round(principal*(rate/100)*time, 2)
print("The amount of interest you would earn is", interest, "dollars.")


