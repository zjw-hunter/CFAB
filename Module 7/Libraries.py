import datetime #https://docs.python.org/3/library/datetime.html#module-datetime
import math #https://docs.python.org/3/library/math.html#module-math
import statistics #https://docs.python.org/3/library/statistics.html#module-statistics
import random

print(datetime.date.today())

print("There are ", datetime.date(2020,1,1) - datetime.date.today(), "Days left in 2019")

whatTimeIsItRightNow = datetime.datetime.now()

print( whatTimeIsItRightNow )


print("Here are some exapmles of functions you can do with the math library")

print( "10! = ", math.factorial(10))

print( "The greatest common divisor of 99 and 121 is" , math.gcd(99, 121))

print( "You can also do Logs for example:  Log(e) = ", math.log(math.e) ,"\nYou can also do base 2 or 10 easily: log10(0.0001) = ", math.log10(0.0001))

print("You can also do trig functions: sin, cos, tan, asin, acos, atan, conversion to/from radians/degrees",
        "\n as well as other simple functions like vector length")

print( "tan(pi/4) = ", math.tan(math.pi/4))
print( "atan(1) * 4 = ", math.atan(1) * 4)
print( "pi radians to degrees => ", math.degrees(math.pi) )
print( "180 degrees to radians => ", math.radians(180) )
print( "the length of a line from (0,0) to (3,4) is: ", math.hypot(3,4) ) # note that it measures from the origin

print("\n Another useful default library is statistics here are some examples:\n")


myData =[]

for i in range(100):
    myData.append(random.randint(0, 10)) #Random, this is sometimes useful 
    
print("Here is a pseudorandom list of numbers 1 - 10\n", myData)
print("Average: ", statistics.mean(myData))
print("Median: ", statistics.median(myData))
print("Variance: ", statistics.variance(myData))
print("Standard Deviation: ", statistics.stdev(myData))










