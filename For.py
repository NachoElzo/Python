#WE HAVE 2 TYPES OF CYCLES DETERMINED AND INDETERMINATE 
#DETERMINATED CYCLE WE KNOW HOW MANY TIMES THE BUCKLE WILL BE EXECUTED
#WE DONT KNOW WHEN THE CYCLE END, UNTIL THE CODITIONS GETS FULLFILLED (FOR)

#DETERMINATED BUCLE EXAMPLE

for i in ["one","two","Three"]: #declaration of the bucle
#i its the variable name) in (can be variables, list, tuples,dictionaries)
    print (i, end=" ") #body of the bucle, with the type "end" we can add to the print the option to end the value with the character tha we want
print ("\r")
print ("*****"*17)

#IN RANGE 
cont=0
for i in range(5,20,3): #(in range)We passed 3 arguments, the bucle, start on 5, until 19 (0 to 19 = 20 values) in steps of 3
    print (f"Value variable {i}") #f special funtion that allows you to concatenate string and variables f "str {int}"
    cont =+1


email = False
myEmail =input("Introduce your email: ")
for i in range(len(myEmail)):
    if myEmail[i] == "@":
        email=True
if email:    
    print ("Thanks")
else:
    print("Plase enters a valid email")