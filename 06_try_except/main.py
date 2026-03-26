#Imagina que el try es una red de seguridad. 
# Tú lanzas un código y, si algo sale mal, el except lo atrapa
try:
    # Aquí pones el código que podría fallar
    numero = int(input("Dime un número: "))
    resultado = 10 / numero
    print(f"El resultado es {resultado}")
except:
    # Aquí pones lo que debe pasar si hay un error
    print("¡Ups! Algo salió mal. No puedes dividir por cero o escribir letras.")


# Falla porque la segunda fila es más corta
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7],        # <--- ¡Faltan elementos!
    [9, 10, 11, 12]
]
try:
    matrix_transpuesta = [[row[i] for row in matrix] for i in range(4)]
except IndexError:
    print("Error: Una de las filas es demasiado corta para completar la transposición.")