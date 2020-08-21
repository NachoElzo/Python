count = 0
while count <= 5:
    print(f"The bucle is {count}")
    count +=1
print("End of the bucle execution")


#While age validation
age = int(input("How old are you: "))
while age <=0 or age >= 106:
    print ("Please, Introduce a valid Age")
    age = int(input("How old are you: "))
if age>=18:
    print (f"You are an adult, with: {age} years old")
elif age == 17:
    print (f"You have only one year left to be an adult, with: {age} years old")
else:
    print(f"You are a kid, with: {age} years old")



