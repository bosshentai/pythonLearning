t = [1,2,3,10]

def cumulativa(array):
    count = 0 
    newArray = []
    for index in array:
        newArray.append(index + count);
        count += index

    return newArray

print(cumulativa(t))