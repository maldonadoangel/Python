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

#otra forma de hacerlo con lambda, listas y map
elementos_al_cuadrado_lambda = list(map(lambda e: e**2, range(10)))
print(elementos_al_cuadrado_lambda)
#otra forma aun mas sencillo
elementos = [x**2 for x in range(10)]
print(elementos)
#Una lista de comprensión consiste de corchetes rodeando una expresión 
# seguida de la declaración for y luego cero o más declaraciones for o if. 
# El resultado será una nueva lista que sale de evaluar la expresión en el 
# contexto de los for o if que le siguen. Por ejemplo, esta lista de comprensión 
# combina los elementos de dos listas si no son iguales:
lista_comprension = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(lista_comprension)
#lo anterior es lo mismo que esto:
combinado = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combinado.append((x,y))
print(combinado)

#crear una neuva lista donde se multiplican por dos los numeros
# de la lista original
vec = [-4, -2, 0, 2, 4]
nueva_lista = [x*2 for x in vec]
print(nueva_lista)
#de la lista original excluir los negativos
lista_sin_negativos = [elemento for elemento in vec if elemento >=0]
print(lista_sin_negativos)
#obtener los valores absolutos del vector o lista
lista_absoluta = [abs(e) for e in vec]
print(lista_absoluta)
#Limpieza del vector o lista, quitando los espacios vacios
fruta_fresca = ['  banana', '  loganberry ', 'passion fruit  ']
fruta_fresca_limpia = [fruta.strip() for fruta in fruta_fresca]
print(fruta_fresca_limpia)
#Listas por comprension anidadas
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]
#Transponer la lista de las filas a columnas
matrix_transpuesta = [[row[i] for row in matrix] for i in range(4)]
print(matrix_transpuesta)
#Lo mismo pero sin lista de compresion
transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)