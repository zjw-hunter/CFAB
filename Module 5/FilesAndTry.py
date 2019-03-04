try:
    print( 1 / 0 )
except Exception as e:
    print(e)



try: 
    with open('myFile.txt', 'r') as myFile:
        contents = myFile.read()
        print(contents)
except Exception as error:
    print(error)


myMessage = "Secret message: ....."

try:
    with open('secretMessage.txt', 'w') as writeFile:
        writeFile.write(myMessage)
except Exception as error:
    print(error)

try:
    with open('secretMessage.txt', 'a') as appendFile:
        appendFile.write('The secret message is : Hello World!')
except Exception as error:
    print(error)

try:
    with open('secretMessage.txt', 'x') as newFile:
        newFile.write("New Message")
except Exception as error:
    print(error)

    


