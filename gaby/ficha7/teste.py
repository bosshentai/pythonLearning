ficheiro = open('mornaSodade.txt','r')

#print(ficheiro.read())


def duplicate(array):
    copy = []
    for item in array:
        #copy.append(item.replace('\n','').split(" "))
        #copy.remove(' ')
        copy.append(item.replace("\n",''))
        
    return copy

newList = duplicate(ficheiro)

print(newList)

#Implementa um programa para abrir o ficheiro chamado mornaSodade.txt e leia-o linha por linha. Para cada palavra encontrada, o número de vezes que ocorre.
