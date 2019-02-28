
def recursiveFibb(nth):
    if( nth == 0):
        return 0
    elif( nth == 1):
        return 1
    else:
        return(recursiveFibb(nth-1) + recursiveFibb(nth - 2))

for x in range(10):
    print(recursiveFibb(x))