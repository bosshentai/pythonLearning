# list and set

myList = [char for char in 'hello']
myList2 = {num for num in range(0,100)}
myList3 = [ num*2 for num in range(0,100)]
myList4 = [ num**2 for num in range(0,100) if num % 2 == 0] # even numbers


print(myList)
print(myList4)