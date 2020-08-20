studentCalification=input("Enters the student calification: ")#WE ASIGN A INPUT VALUE AS VARIABLE,PYTHON ASUMES THAT IS AN STR

def result(studentCalification): #FUNCTION DEFINITION
    status = "Aproved" #NEW VATIABLE STATUS STARTS AS APROVED
    if studentCalification < 4:  #CONDITION
        status ="Reprobate" #ACTION AFTER THE CONDITION
    return(status) #RETURNS THE STATUS WITH THE JOINED 

print (result(int(studentCalification))) #CONVERTING THE VARIABLE IN INT 

enAge =input("How old are you: ")
def adult (enAge):
    if enAge > 105 or enAge <=0:
        print ("Please enter a correct age")
    elif enAge == 17:
        print ("You only have one year left to join")
    else: #The else evaluates the last if, that why we have to add an elif
        print ("Yu are and adult, please join")
adult(int(enAge))

#We can evaluate more tan one variable concatenated
age= 37
if 0 < age <100: #Concatenating one variable with 2 operators
    print ("Correct")
else:
    print("incorrect")


