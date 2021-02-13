def leia(ficheiro):
    texto = open(ficheiro, "r")
    duplicado = dict()

    for linha in texto:
        linha = linha.strip()
        linha = linha.lower()
        
        palavras = linha.split(" ")

        for pala in palavras:
            if pala in duplicado:
                duplicado[pala] = duplicado[pala] + 1
            else :
                duplicado[pala] = 1 
    
    for key in list(duplicado.keys()):
        if key != "":
            print(key,":", duplicado[key])            

leia('mornaSodade.txt')

#Implementa um programa para abrir o ficheiro chamado mornaSodade.txt e leia-o linha por linha. 
# Para cada palavra encontrada, o número de vezes que ocorre.
