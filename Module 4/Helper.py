#Program

def getMyData():
    data = []
    base = str(2 ** 128)
    for i in range(len(base)):
        data.append(int(base[i]))
    return data

def myOperation( x, y ):
    return abs(x - y)

if __name__ == "__main__":#Main method
    data = getMyData()
    i = 1
    while i < len(data):
        data[i] = myOperation(data[i], data[i - 1])
        i = i + 1
    for d in data:
        print(d)
        
