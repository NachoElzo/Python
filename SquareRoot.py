import math
print ("Executable program to get the square root of a number")
number = int(input("Please, Introduce a positive number: "))

chances=0
while number < 0:
    print ("Please enter a positive number")

    number = int(input("Please, Introduce a positive number: "))
    if number < 0:
        chances +=1

    if chances == 2:
        print("You dont have more chances")
        break

if chances<2:
    result=math.sqrt(number) #class math, function sqrt (square root)
    print(f"The square root of: {number} is {result}")
