#OR
avalue = int(input("Introduce the Ammount of the apartment: "))
print ("The ammount of money of the apartment is: $" + str(avalue))
savings = int(input("Introduce the ammount of you savings: "))
print ("The ammount of money of your savings are: $" + str(savings))
fee = avalue *0.10
print ("The ammount of the fee is: $"+ (str(fee)))

if  savings == avalue or savings >= fee or savings > avalue :
    print ("!!Congratulation, you can buy a new apartment!!")
else:
    mLeft = fee-savings
    print("Sorry but you have to keep saving, you have left: $" + (str(mLeft)))

print("****"*20)


#AND
print("Program to recive a COVID bond")
salary = int(input("How much is your regular salary: $"))
salaryDecrease= int(input("How much you salary decrease after pandemic? $"))
perDecrease = salary*0.5 
if salary <= 800000 and perDecrease <= salaryDecrease:
    print("Congratulations you are going to recive the CODVID bond")
else:
    print("Sorry but you dont qualify for the bonus")



print("****"*20)
#IN
print("Hi new student; please, choose and optional academic class")
clss = str(input("Software Enginner student, please choose between: JAVA, PYTHON OR JAVASCRIPT: "))
chosenClass = clss.lower() #With the function .lower we can change CAPS INTO lowerCase
if chosenClass in ("java", "python", "javascript"):
    print("Your optional class is: " + chosenClass + " Your class is on saturdays 8 AM")
else:
    print("You choose an invalid class")
