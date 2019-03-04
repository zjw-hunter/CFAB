# Lots of booleans
x = 0
y = 1
print("X = 0, Y = 1")
print("x == 0 evaluates to ", x == 0) #True
print("x < y evaluates to ", x < y ) #True
print("x > y evaluates to ", x > y ) #False
print("x <= y evaluates to ", x <= y) #True
print("x >= y evaluates to ", x >= y) #False
print("x != y evaluates to ", x != y) #True
print("True and False evaluates to ", True and False) 
print("True or False evaluates to ", True or False)
print("True or (any statement) evaluates to ", True or False or False or False) #...
print("not (true) evaluates to ", not (True))
#print( x == 0 and y != 1)

if( True):
    print("I'm in an if block")

x = 0

if( x != 0):
    print("x != 0")
elif( x == 0 ):
    print("x = 0")

if( False ):
    #This will never happen
    x = 1 / 0
else:
    print("We made it to the end of the conditional statement!")
