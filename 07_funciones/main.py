def transponer(matriz):
    try:
        #tomamos el ancho de la matriz
        ancho_matriz = len(matriz[0])
        return [[row[i] for row in matriz] for i in range(ancho_matriz)]
    
    except IndexError:
        return "Error: La matriz está mal formada."
    
# Ahora solo la llamas:
mi_matriz = [
    [1, 2], 
    [3, 4]
]
print(transponer(mi_matriz))


#Ejercicio limpiar y transponer una matriz

def limpiar_y_transponer(lista_de_listas):
    try:
        # Calcularemos la cantidad de columnas que tiene nuestra fila
        ancho = len(lista_de_listas[0])
        # aplicamos la logica 
        resultado = [[fila[i] for fila in lista_de_listas] for i in range(ancho)]
        return resultado
    except IndexError:
        return "Error: La matriz es irregular (algunas filas son más cortas)."
    except Exception as e:
        return f"Ocurrió un error inesperado: {e}"
    

matriz_buena = [[1, 2], [3, 4], [5, 6]]
matriz_mala = [[1, 2, 3], [4, 5]] # Le falta un número a la segunda fila

print("Matriz 1:")
print(limpiar_y_transponer(matriz_buena))

print("\nMatriz 2 (con error):")
print(limpiar_y_transponer(matriz_mala))