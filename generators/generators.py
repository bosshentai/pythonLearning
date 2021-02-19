
# # interable 
# def makeList(num):
#     result = []
#     for i in range(num):
#         result.append(i*2)
#     return result 


# myList = makeList(1000000)
# print(myList)

def generatorFunction(num):
    for i in range(num):
        yield i
    
g = generatorFunction(1)
print(next(g))
print(next(g))
print(next(g))

print(next(g))
# for item  in generatorFunction():
#     print(item)
