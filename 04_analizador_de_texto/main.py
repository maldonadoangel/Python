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

#SubString
palabras = "ABCDEFGHIJKLMN"

fragmento = palabras[2:5]
print(fragmento)

print(palabras[2:])

print(palabras[2:10:2])

#Ejercicio 1
#Extrae la primera palabra de la siguiente frase utilizando slicing, y muéstrala en pantalla
#"Controlar la complejidad es la esencia de la programación"
frase = "Controlar la complejidad es la esencia de la programación"

print(frase[0:9])

#Ejercicio 2
#Toma cada tercer caracter empezando desde el noveno hasta el final de la frase, e imprime el resultado.
#"Nunca confíes en un ordenador que no puedas lanzar por una ventana"
frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"

print(frase[8:66:3])
#Ejercicio 3
#Invierte la posición de todos los caracteres de la siguiente frase y muestra el resultado en pantalla.
#"Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
print(frase[::-1])
#Metodos String
texto = "Este es el texto de Angel"
print(texto.upper())
#Metodo lower para quizar la mayuscular y transformarlo
texto_mayuscula = "SOY UN TEXTO EN MAYUSCULA"
print(texto_mayuscula.lower())
#metodo split para cortar el texto en varias partes y mostrarlo en un arreglo
print(texto.split())
#Practica 1
frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."

print(frase.upper())
#practica 2
#Une la siguiente lista en un string, separando cada elemento con un espacio. Utiliza el método apropiado de listas/strings, y muestra en pantalla el resultado.
lista_palabras = ["La","legibilidad","cuenta."]
frase = " ".join(lista_palabras)
print(frase)
#practica 3
#Reemplaza en la siguiente frase: "Si la implementación es difícil de explicar, puede que sea una mala idea."
#los siguientes pares de palabras:
#"difícil" --> "fácil" "mala" --> "buena" y muestra en pantalla la frase con ambas palabras modificadas.

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."

resultado = frase.replace("difícil","fácil").replace("mala","buena")
print(resultado)