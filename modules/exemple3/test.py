import random as rd

print(rd.choice([1,2,3,4,5]))
print(rd.randint(1,10))
myList = [1,2,3,4,5,6]
random.shuffle(myList)
print(myList)