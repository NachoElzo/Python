name = "Jose ignacio elzo"
counter =0
for i in name:
    if i == " ":
        continue #skipt the iteration when the condition it's true
    counter +=1
print (f"The amount of characters with out spaces are: {counter}")

#With the pass instruction we can pass a class = null class or a function in order to stopt an infinite loop
#Example
def expass (self):
    pass

#else out of the iff 

email = input("Introdce your email: ") 
for i in email:
    if i == "@":
        arroba=True
        break
else:
    arroba=False
print (f"Your emails is: {arroba}")


  

