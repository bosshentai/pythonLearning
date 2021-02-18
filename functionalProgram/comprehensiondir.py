simpleDict ={
    'a':1,
    'b':2
}

##
# k = key
# v = value
##
myDict = { k: v ** 2 for k,v in simpleDict.items()
if v%2 == 0}

myDict2 = {num: num*2 for num in [1,2,3]}

print(myDict)
print(myDict2)