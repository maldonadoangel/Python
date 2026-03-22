from collections import deque
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

#Usar listas como pilas
stack = [1,2,3,4]
stack.append(5)
#Se agrega el elemento en la cima de la lista
print(stack)
#Sacamos el ultimo elemento agregado, tal y como
#funciona el stack
print(stack.pop())
print(stack)
#Utilizar listas como una cola es posible
#pero no es lo mas eficiente para este propocito.
#Ya que hay que agregar y sacar del final de la lista.
#pero insertar o sacar del comienzo
#se recomienda utilizar from collections import deque
queue = deque(['Angel', 'Hernan', 'Morales', 'Maldonado'])
queue.append('Jose')
queue.append('Genesis')
print(queue)
#Quitamos al primero de la lista ya que fue el primero en entrar
#Sera el primero en salir
print(f"El primero en salir en la cola: {queue.popleft()}")
print(f"El segundo en salir en la cola: {queue.popleft()}")
print(f"Los que quedan en la lista: {queue}")
#comprension de listas
#Los elementos agregados a la lista se elevaran al cuadrado
elementos_al_cuadrado = []
for elemento in range(10):
    elementos_al_cuadrado.append(elemento**2)
print(f"Los elementos fueron elevados al cuadrado: {elementos_al_cuadrado}")

