# lambda expressions 
#lambda param: action(param)

myList = [1,2,3]

def multiplyBy2(item):
    return item*2

def onlyOdd(item):
    return item % 2 != 0

def accumulator(acc,item):
    print(acc,item)
    return acc + item 

print(list(map()))
