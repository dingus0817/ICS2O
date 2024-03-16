#File Name: DataTypeExercises.py
#Description: This is practice for data types
#Author: Jamie Zhang

min1 = input("Enter the first number: ")
min2 = input("Enter the second number: ")
min3 = input("Enter the third number: ")
minFunction = min(min1, min2, min3)
print("The smallest out of the numbers is " + minFunction)


max1 = input("Enter the first number: ")
max2 = input("Enter the second number: ")
max3 = input("Enter the third number: ")
maxFunction = max(max1, max2, max3)
print("The largest out of the numbers is " + maxFunction)



roundNum = input("Enter a number: ")
roundFunction = round(float(roundNum))
print("The number rounded to the nearest whole number is " + str(roundFunction))


roundNumber = input("Enter a number: ")
roundFunction2 = round(float(roundNumber), 3)
print("The number rounded to three decimal places is " + str(roundFunction2))


num = input("Enter a number: ")
absFunction = abs(int(num))
print("The absolute value of the number is " + str(absFunction))


char1 = ord("J")
print("The ASCII value of the character J is", char1)
char2 = ord("a")
print("The ASCII value of the character a is", char2)
char3 = ord("m")
print("The ASCII value of the character m is", char3)
char4 = ord("i")
print("The ASCII value of the character i is", char4)
char5 = ord("e")
print("The ASCII value of the character e is", char5)


print(str(chr(116)+chr(104)+chr(101)+chr(32)+chr(98)+chr(101)+chr(115)+chr(116)+chr(32)+chr(99)+chr(111)+chr(117)+chr(114)+chr(115)+chr(101)+chr(32)+chr(101)+chr(118)+chr(101)+chr(114)+chr(33)))
      

a, b, c, x = 3.2, 4, 1.5, 3 
#a)
result1 = b**2 - 4*a*c
print(result1)
print(type(result1))
#b)
y = float(a + c - b**x)
result2 = round(y)
print(result2)
print(type(result2))
#c)
y = float((a+b)/(c+x))
result3 = round(y,2)
print(result3)
print(type(result3))
#d)
y = 1/(1+x**2)
result4 = float(y)
print(result4)
print(type(result4))
#e)
y = -x*abs(b-5*c)
result5 = int(y)
print(result5)
print(type(result5))
#f)
result6 = float((a*c)/4)
print(result6)
print(type(result6))
#g)
y = float((a*c)/x)
result7 = round(y)
print(result7)
print(type(result7))
#h)
result8 = float(x%c)
print(result8)
print(type(result8))
#i
y = float((7/(c+b%a))*x)
result9 = round(y)
print(result9)
print(type(result9))
#j)
y = float((5*x*(a-c))/-b)
result10 = abs(y)
print(result10)
print(type(result10))


x = input("Enter a number: ")
x1 = int(x)
answer = x1*x1*x1
print(answer)
print(type(answer))


g, h = input("Enter two numbers (seperate by space): ").split()
g1, h1 = int(g), int(h)
h = g1 + h1
g = g1 - 3
print(h)
print(type(h))
print(g)
print(type(g))


z = input("Enter a number: ")
zed = int(z)
z1 = zed + 2
print(z1)
print(type(z1))


a, b = input("Enter two numbers (seperate by space): ").split()
a1, b1 = float(a), float(b)
c = a1/b1
d = a1/b1
e = a1%b1
print(c, d, e)
print(type(c),type(d),type(e))


x = "Hello"
y = "world"
print(y)
print(type(y))
z = x + y
print(z)
print(type(z))

