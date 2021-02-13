# Convert a telephone number into corresponding name, if on list.
# (If not on list, just return the number itself.)
def telToName(tel, telList, nameList):

    try:
        pos = telList.index(tel)
        name = nameList[pos]
    except ValueError:
        name = tel

    # For the tel is not in the list return
    if tel not in telList:
        return tel

    return name


# Return list of telephone numbers corresponding to names containing partName.
def nameToTels(partName, telList, nameList):
    # your code here
    foundName = []

    tels = []
    #pos = nameList.index(partName);
    for value in nameList:
        foundName.append(value.startswith(partName))

    # for value in telList:
    #     if foundName.keys == True:
    #         teste = ''
    #         tels.append(value)

    print(foundName)
    print(tels)
    return tels


# Lists of telephone numbers and names
telList = ['975318642', '234000111', '777888333', '911911911']
nameList = ['Angelina', 'Brad',      'Claudia',   'Bruna']

# Test telToName:
#tel = input("Tel number? ")
#tel = '975318642'
#print( telToName(tel, telList, nameList) )
#print( telToName('234000111', telList, nameList) == "Brad" )
#print( telToName('222333444', telList, nameList) == "222333444" )

# Test nameToTels:
#name = input("Name? ")
#print( nameToTels(name, telList, nameList) )
print(nameToTels('Clau', telList, nameList) == ['777888333'])
print(nameToTels('Br', telList, nameList) == ['234000111', '911911911'])
