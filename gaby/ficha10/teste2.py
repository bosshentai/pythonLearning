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
    guardar = open("texto.txt","a")
    for key in list(duplicado.keys()):
        guardar.write(f'{key} : {duplicado[key]} \n')
        
    guardar.close()

leia('words.txt')