
class myObject():

    myValue = "I'm an object!"

myInstance = myObject()

print(myInstance.myValue)


class usefulObject():

    def printString(self, myString):
        print("I'm printing a string: ")
        print(myString)


uO = usefulObject()

u0.printString("Hello World!")

class pet():

    def __init__(self, name):
        self.name = name

myDog = pet("Spot")

print("My dog's name is : ", myDog.name)