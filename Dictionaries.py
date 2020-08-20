#To create dicctionaries should have a key and value
#We can add and modify dicctionaries
#You can add more than one value in a key
#We can create more than one dictionary in one dictionary

dic = {"chile":56, "usa":840, "italia": 79}
dic["Alemania"]=800 #We can add element to a dictionary (first the key and the the value of the key)
dic["Alemania"]=900 #Replacing the value of alemania
print (dic)
print (dic["chile"])#We can access to a value through his key
del dic["italia"]#we delete the element key and value of the dicctionary
print (dic)

tupla= ["bmw", "opel","corsa"]
dictio ={tupla[0]:2018,tupla[1]:2019,tupla[2]:2020} #We can create a tuple of index and then asing the value with the psistion 
print (dictio)
print(dictio["opel"]) #this is the way to display a value with his key

devices = {"tv":["Samsung",40], "SmarthPhone":["Samsung","s10"], "Laptop":["ASUS",10,30,40,50]}#adding more than one value in a key
print (devices) 
print (devices["Laptop"])#printing the value of the key laptop

doubledic = {"casa":"6000 uf", "depto":"4200 uf", "pie":{"casa":"1200uf", "depto":"800uf"}} #creating a dictionary inside a dictionary
print(doubledic)
print(doubledic["pie"])#printing the second dictinary
print(doubledic.keys())#printing the keys of the dictionary
print(doubledic.values())#printing the values of the dictionary
print(len(doubledic)) #printing the lenght of the dictionary (kesys+values, extra dictionary are considered as one value)