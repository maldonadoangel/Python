
def obtener_ancho(matriz):
    try:
        return len(matriz[0])
    except(IndexError, TypeError):
        return 0
    
def transponer_matriz(matriz):
    ancho = obtener_ancho(matriz)

    if ancho == 0:
        return "Error: Datos invalidos"
    
    try:
        return [[fila[i] for fila in matriz] for i in range(ancho)]
    except Exception as e:
        return f"Error en proceso: {e}"
    

    # --- USO PROFESIONAL ---
mi_data = [[1, 2, 3], [4, 5, 6]]
resultado = transponer_matriz(mi_data)

if isinstance(resultado, list):
    print("Transposición exitosa:", resultado)
else:
    print("Hubo un fallo:", resultado)