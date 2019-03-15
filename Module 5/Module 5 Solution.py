filename = "outfile.txt"


def aot( x1, y1, x2, y2, x3, y3):
    area = abs(0.5* ((x1 * (y2 - y3)) + (x2 * (y3 - y1)) + (x3 * (y1 - y2))))
    if( area == 0.0 ):
        raise Exception
    return area

if __name__ == "__main__":
    try:
        x1 = int(input("Enter x1:"))
        y1 = int(input("Enter y1:"))
        x2 = int(input("Enter x2:"))
        y2 = int(input("Enter y2:"))
        x3 = int(input("Enter x3:"))
        y3 = int(input("Enter y3:"))
        area = aot(x1,y1,x2,y2,x3,y3)
        print("The area of your triangle is: ", area)
        with open(filename, 'x') as newFile:
            newFile.write("Calculated that triangle: (" + str(x1) + "," + str(y1) + "), " +
                          "("+ str(x2) +"," + str(y2) + "), " +
                          "("+ str(x3) +"," + str(y3) + ")" +
                          " Has an area of: " + str(area))
            
    except Exception as e:
        print(e)
        print("Invalid input or not a triangle.")
        
    
    