#filter 
myList = [1,2,3]

def checkOdd(item):
    return item % 2 != 0

print(list(filter(checkOdd,myList)))