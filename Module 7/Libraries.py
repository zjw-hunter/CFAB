import copy
import math #https://docs.python.org/3/library/math.html#module-math
import statistics #https://docs.python.org/3/library/statistics.html#module-statistics
import random
import myLibrary

class original:
    def __init__(self, val, sub):
        self.val = val
        self.sub = sub


internal = original("I'm an object in an object", None)

external = original("I'm an object that contains an object", internal)

assignedCopy = external
shallowCopy = copy.copy(external)
deepCopy = copy.deepcopy(external)

external.val = "I've been changed!"
internal.val = "I've been changed!"

print("Internal val is ", internal.val)
print("External val is ", external.val)
print("assignedCopy vals are " + assignedCopy.val + " " + assignedCopy.sub.val)
print("shallowCopy val are " + shallowCopy.val + " " + shallowCopy.sub.val)
print("deepCopy val are " + deepCopy.val + " " + deepCopy.sub.val)
print("\n\n\n")




print("Here are some exapmles of functions you can do with the math library")

print( "10! = ", math.factorial(10))

print( "The greatest common divisor of 99 and 121 is" , math.gcd(99, 121))

print( "You can also do Logs for example:  Log(e) = ", math.log(math.e) ,
       "\nYou can also do base 2 or 10 easily: log10(0.0001) = ", math.log10(0.0001)
       , " log2(2048) = ", math.log2(2048))

print("You can also do trig functions: sin, cos, tan, asin, acos, atan, conversion to/from radians/degrees",
        "\n as well as other simple functions like vector length")

print( "tan(pi/4) = ", math.tan(math.pi/4))
print( "atan(1) * 4 = ", math.atan(1) * 4)
print( "pi radians to degrees => ", math.degrees(math.pi) )
print( "180 degrees to radians => ", math.radians(180) )
print( "the length of a line from (0,0) to (3,4) is: ", math.hypot(3,4) ) # note that it measures from the origin

print("\n\n\n Another useful default library is statistics here are some examples:\n")

myData =[]
for i in range(100):
    myData.append(random.randint(0, 100)) #Random, this is sometimes useful 
    
print("Here is a list of random numbers 1 - 100\n", myData)
print("Average: ", statistics.mean(myData))
print("Median: ", statistics.median(myData))
print("Variance: ", statistics.variance(myData))
print("Standard Deviation: ", statistics.stdev(myData))


print("\nCustom modules (ones that you make) are also available")

myLibrary.performOperation(" It also takes arguments")

classFromMyLibrary = myLibrary.myClass()

classFromMyLibrary.classOperation()