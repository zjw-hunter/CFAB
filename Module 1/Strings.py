#Strings

firstHalf = "Hello"
secondHalf = "World!"
print( firstHalf + " " + secondHalf) #Concatenation

x = 2

print( "The value of x is: " + str(x) ) #Casting a non string to a string

print( "The value of x is: %s" % x ) #String Formatting

print( "The value of x is: {}".format(x))

message = firstHalf + " " + secondHalf 

print( message ) #Concat to a variable

print( len(message) ) #len() function
print( message[3] ) # All about [:]
print( message[:3] )
print( message[3:] )
print( message[2:6] )
