# Exercise : Check for duplicates in list:
someList = ['a', 'b', 'c','b','d','m','n','n']

duplicates = []
for value in someList:
    if someList.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)