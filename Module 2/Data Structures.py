#Lists
myList = [1, 2, 3]
print(myList)
print(myList[0]) #Accessing a list
myList.append(4) # Add to the end of the list
print(myList)
myList.insert(0, 0) # Add at a certain index
print(myList)
myList.reverse() # Reverses the order of the list
print(myList)
myList.pop() # Removes the last element of the list
print(myList)
del myList[0] # Removes the element at a certain index
print(myList)
myList.sort() # Default sorting method
print(myList)

#Dictionaries
myDict = {"one": 1, "two": 2, "three": 3}

print(myDict)

print(myDict["one"])
print(myDict.get("two"))

