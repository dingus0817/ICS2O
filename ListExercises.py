print("please enter five marks")
mark = 0
marks = []
for count in range(5):
    mark = input("enter a mark: ")
    marks.append(mark)
print("the best mark out of the five is:", max(marks))



import random
rand = []
cap = 15
for count in range(cap):
    number = random.randint(1,101)
    rand.append(number)
print("the average of the random numbers is:", sum(rand)//cap)



sandwich_dict = {
    "monday":"roasted chicken",
    "tuesday":"roast beef",
    "wednesday":"spicy italian",
    "thursday":"steak'n'cheese",
    "friday":"tuna"
    }

day = input("enter the day of the week today: ").lower()

if day in sandwich_dict:
    print("the sandwich that is on discount today is:",sandwich_dict[day])
else:
    print("sorry, there is no sandwich on discount today; try again another day")
