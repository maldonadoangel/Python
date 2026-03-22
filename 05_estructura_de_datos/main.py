#Estructura de datos
#Listas
frutas = ['Naranja', 'Manzana', 'Pera', 'banana', 'Kiwi', 'Manzana', 'banana']
print(frutas)
#Según la documentación oficial de Python, el método .count() 
# sirve para un propósito muy específico y sencillo: 
# contar cuántas veces aparece un elemento determinado dentro de 
# una lista.
print(frutas.count('Kiwi')) #muestra el valor de 1
#Según la documentación oficial de Python, el método .count() 
# sirve para un propósito muy específico y sencillo: 
# contar cuántas veces aparece un elemento determinado dentro de una lista.
print(frutas.index('Kiwi'))
#Como buscar la proxima fruta a partir de la posicion 4 osea el kiwi
print(frutas.index('banana', 4)) #Nos devuelve la posicion 6
#invertir la lista, lo que hace es modificar la lista original
#si intentamos imprimir frutas.reverse() nos regresara none
frutas.reverse()
print(frutas)
