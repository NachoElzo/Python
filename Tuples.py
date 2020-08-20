#Tuples cant be modified, insert, delete 
#Tupleas can be a key for diccionaries
#You can print elements
#you can slice over the tuple
#Are faster than list and diccionaries
#You can transform tuples in a list with the function list()

tupl = ("one","two","three","four","five","five")
lit = list(tupl) #you can transform a tuple into a list
print (lit)
print (tupl [0:-2]) #we can slice over the tuple with index and value
print (tupl [0:1])
print ("five" in tupl) #we can search a value in the tuple
print(tupl.count("five")) #with the function.count we can count how many times is present a value in a tuple
print(len(tupl))#with the function len we can display the lenght of the tuple
unituple = (1,)#In order to create a unit tuple you should add a coma "," after the element 
print (len(unituple))

tuplVarible = (1985, 37, "male")
dateOfBirth, age, gender =tuplVarible # we can assign variables to the tuple (should be in the same order) this is known as unpacked tuples
print (dateOfBirth)
print (age)
print (gender)