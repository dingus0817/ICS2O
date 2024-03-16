#File name: EmotionalDamage.py
#Description: This program will determine the grade of a student
#Author: Jamie Zhang

mark = int(input("What is your mark for this course? "))
           
a = mark >= 80
b = 80 > mark >= 70
c = 70 > mark >= 60
d = 60 > mark >= 50

if (a):
    print("You got an A: Congrats on being average!")

elif (b):
    print("You got a B: That's bad...")

elif (c):
    print("You got a C: That's a catastrophe!")

elif (d):
    print("You got a D: Don't come home")

else:
    print("You got an F: Congrats on being forgotten forever!")
