from functools import reduce 

myList = [1,2,3]

def accumulator(acc,item):
    print(acc,item)
    return acc + item 

print(reduce(accumulator,myList,0))