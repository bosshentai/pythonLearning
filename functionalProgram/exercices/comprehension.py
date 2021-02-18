someList = ['a', 'b','c','b', 'd','m','n','n']

duplicates = list(set([ x for x in someList if someList.count(x) > 1]))

print(duplicates)