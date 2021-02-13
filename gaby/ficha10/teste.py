jogador = {
    'corda': 1,
    'tocha': 6,
    'moeda de ouro': 42,
    'punhal': 1 ,
    'fecha': 12,   
}

def displayInventory(inventario):
    
    print(f'Invetario:  {inventario.get("fecha")} fecha {inventario.get("moeda de ouro")} moeda de ouro {inventario.get("corda")} corda {inventario.get("tocha")} tocha {inventario.get("punhal")} punhal')



displayInventory(jogador)

def save()