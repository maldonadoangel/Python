def transponer(matriz):
    try:
        return [[row[i] for row in matriz] for i in range(len(matriz[0]))]
    
    except IndexError:
        return "Error: La matriz está mal formada."
    
# Ahora solo la llamas:
mi_matriz = [
    [1, 2], 
    [3, 4]
]
print(transponer(mi_matriz))