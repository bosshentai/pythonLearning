# Square
myList = [5,4,3]

newList = list(map(lambda item: item**2, myList))
print(newList)

# List Sorting

a = [(0,2),(4,3),(10,-1),(9,9)]
a.sort(key=lambda x: x[1])
print(a)
