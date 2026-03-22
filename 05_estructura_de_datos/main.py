#Estructura de datos
#Listas
frutas = ['naranja', 'manzana', 'pera', 'banana', 'kiwi', 'manzana', 'banana']
print(frutas)
#Según la documentación oficial de Python, el método .count() 
# sirve para un propósito muy específico y sencillo: 
# contar cuántas veces aparece un elemento determinado dentro de 
# una lista.
print(frutas.count('kiwi')) #muestra el valor de 1
#Según la documentación oficial de Python, el método .count() 
# sirve para un propósito muy específico y sencillo: 
# contar cuántas veces aparece un elemento determinado dentro de una lista.
print(frutas.index('kiwi'))
#Como buscar la proxima fruta a partir de la posicion 4 osea el kiwi
print(frutas.index('banana', 4)) #Nos devuelve la posicion 6
#invertir la lista, lo que hace es modificar la lista original
#si intentamos imprimir frutas.reverse() nos regresara none
frutas.reverse()
print(frutas)
#Agregar elementos al final de la lista
frutas.append('uvas')
frutas.append('arandano')
print(frutas)
#Sorted Por defecto, .sort() ordena de forma ascendente (de menor a mayor o alfabéticamente).
frutas.sort()
print(frutas)
#pop, se utiliza para eliminar el ultimo elemento
frutas.pop()
print(frutas)