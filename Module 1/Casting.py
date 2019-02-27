#Casting & operators

num1 = 10
num2 = 4
print( str(num1) + " is a: " + str(type(num1) )) #Casting to string
print( str(num2) + " is a: " + str(type(num2) )) 
num3 = num1 / num2
print( str(num3) + " is a: " + str(type(num3) )) #Gives a float
num4 = num1 / 5
print( str(num4) + " is a: " + str(type(num4))) #Still a float

print( int(num3) ) #Rounds down
