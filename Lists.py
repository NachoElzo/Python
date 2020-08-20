#list or array in where we can access, modify, operations and prints values
lista = ["one","two","three","four","five","six"]
#printing all the list
print(lista)
#Slicing, the index start from 0   
print(lista[0:2]) #index 0, pisition1
print(lista[0:-1]) #-1 is the last position of the list 
print(lista[:-2]) # if you dont add an index python add the first index 0 
print(lista[2:])#we can print from the second index to the last position

lista.append("seven") #with the function append we add an element to the last position of the list
print(lista)

lista.insert(0,"cero") #adding a parameter index and elament we can add elements to that index
print(lista)

lista.extend(["eight", 9])#with the function extend we extend the list adding more values (can be differents types (str,int...etc))
print(lista)

print(lista.index("four"))#with the function index, we can print the index of the element 

print("ten" in lista)#with the fun in we can print if the element exist in the list (boolean type)

lista.remove("cero")#removes an element from the list
print(lista)

lista.pop()#removes the las element from the list
print(lista)

lista2 = [True, 9,128,128]*3#we can multiply lists
lista3 = lista + lista2
print (lista3[:-1]) #we can sume 2 lists in one new variable

tpl = tuple(lista2)#We can transform list into a tuple in a new variable with the function tuple()
print (tpl)
print (lista2.count(128))#with the function.count We can count how many times is a value in the list
print(len(lista2))#with the function len we can display the lenght of the list

