mySet = {1,2,3,4,5,5}
#mySet.add(100)
#mySet.add(2)
print(mySet)

# return a list only have unique 
myList = [1,2,3,4,5,5]
#print(set(myList))

yourSet = {4,5,6,7,8,9,10}

# .difference()
# print(mySet.difference(yourSet))

# .discard()
# print(mySet.discard(5))
# print(mySet)

# .difference_update()
# print(mySet.difference_update(yourSet))
# print(mySet)

# .intersection()
#print(mySet.intersection(yourSet))

# .isdistjoint()
#print(mySet.isdisjoint(yourSet))

# .issubset()
#print(mySet.issubset(yourSet))

# .issuperset()
print(mySet.issuperset(yourSet))

# .union()
#print(mySet.union(yourSet))
#print(mySet | yourSet)