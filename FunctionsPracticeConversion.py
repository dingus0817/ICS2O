#File name: FunctionsPracticeConversion.py
#Author: Jamie Zhang

def inToMm(inch):
    conversion = inch * 25.4
    return conversion
def mmToIn(mm):
    conversion = mm/25.4
    return conversion
def lbToKg(pounds):
    conversion = lb/2.205
    return conversion
def kgToLb(kg):
    conversion = kg*2.205
    return conversion
def LToGal(L):
    conversion = L/3.785
    return conversion
def galToL(gallons):
    conversion = gallons*3.785
    return conversion

initValue = int(input("enter a value: "))
initUnit = input("enter the unit you want it to be converted from (in,mm,lb,kg,L,gal): ")
if initUnit == "in":
    convertedUnit = "mm"
    convertedValue = inToMm(initValue)
elif initUnit == "mm":
    convertedUnit = "in"
    convertedValue = mmToIn(initValue)
elif initUnit == "lbs":
    convertedUnit = "kg"
    convertedValue = lbToKg(initValue)
elif initUnit == "kg":
    convertedUnit = "lb"
    convertedValue = kgToLb(initValue)
elif initUnit == "L":
    convertedUnit = "gal"
    convertedValue = LToGal(initValue)
elif initUnit == "gal":
    convertedUnit = "L"
    convertedValue = galToL(initValue)
else:
    print("... nevermind")
print(initValue, initUnit, "converted to", convertedUnit + ":", convertedValue)

