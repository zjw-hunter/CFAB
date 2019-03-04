
myBool = True

while( myBool ):
    print( "In the loop ")
    myBool = False


counter = 0
print("\n\n\nStarting while loop")
while( counter < 10):
    print("At count: ", counter)
    counter += 1
print("End while Loop \n\n\n")

print("Starting for Loop")
for i in range(0, 10):
    print("At value: ", i)
print( "End for loop \n\n\n") 
myArray = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Starting enhanced for loop")
for element in myArray:
    print("At Value: ", element)
print("End of enhanced for loop")


myDict = { 0 : 'zero', 1 : 'one', 2: 'two' }

print("\n\n\nStarting dictonary loop")
for key in myDict:
    print("The Key: ", key, " corresponds to value: ", myDict[key])
    

