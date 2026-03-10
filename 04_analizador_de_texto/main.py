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