#vamos a entender como se compone los strings, como podemos analizarlos, recorrer las cadenas de texto y buscar
mi_texto = "Esto es una prueba de para buscar"
resultado = mi_texto[9]
#Mostrara el primer caracter de nuestro texto
print(resultado)
#metodo index, es case sensitivity por lo que si escribimos mal una palabra o una letra no lo encontrara
#arrojara un error al no encontrar nada
resultado = mi_texto.index('a', 5, 11)
print(resultado)
#Practica 1
#Encuentra y muestra en pantalla qué caracter ocupa la quinta posición dentro de la siguiente palabra: "ordenador"
palabra = "ordenador"
print(palabra[4])
#Practica 2
#Encuentra y muestra en pantalla el índice de la primera aparición de la palabra "práctica" en la siguiente frase:
#"En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."

print(frase.index("práctica"))
#Practica 3
#Encuentra y muestra en pantalla el índice de la última aparición de la palabra "práctica"
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
print(frase.rindex("práctica"))