def msg (): #Function definition
    print ("This is the first message")  #body
    print ("This is another message")
msg() #funtion call 
msg()

def ope (a,b,c): #(Pasing parameters to the function)
    resultado = ((a+b)*c)
    return (resultado) #we are returning the result 
storeResult = ope(10,20,30) #storing the arguments from the function ope in a variable 
print (storeResult) #we can print this variable in any place of the code 


def ope2 (a,b,c): 
    resultado = ((a+b)*c)
    return (resultado) 
print(ope2(10,30,5))
print(ope2(30,40,80))
