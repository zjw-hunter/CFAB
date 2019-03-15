def addAll( array ):
    total = 0
    for item in array:
        total += item
    return total

def median( array ):
    if(len(array)%2 == 0):
        return (array[int(len(array)/2)] + array[int((len(array)/2)) - 1]) / 2
    else:
        return array[int((len(array)/2))]

if __name__ == "__main__":
    myData = [0,1,2,3,4,5,6,7,8,9,10]
    myAverage = addAll(myData) / len(myData) # Should be 5
    print(myAverage)
    print(median(myData))
    myData.pop(0)
    print(median(myData))