nombre_asociado = "Jesse Pikman"
numero_asociado = 399058
puntos_nuevos = 350
puntos_totales = 1225
puntos_anteriores = 875
puntos_nuevos = 350
numerador = 456
denominador = 33

print('Estimado/a {}, su número de asociado es: {}'.format(nombre_asociado, numero_asociado))
print('Has ganado {} puntos! En total, acumulas {} puntos'.format(puntos_nuevos, puntos_totales))
print('Has ganado {} puntos! En total, acumulas {} puntos'.format(puntos_nuevos, puntos_nuevos + puntos_anteriores))

#sacar el mod entre  y 33
print(numerador%denominador)
#sacar raiz cuadrada de 783
print(783**0.5)



#proyecto 2
#Crear una app que solicite al usuario su nombre completo y sus ventas totales y que al final regrese el % de las ventas o
#comisiones los cuales son el 13%

nombre_empleado = input("Ingresa tu nombre completo: ")
venta_empleado = float(input("Ingrese el total de sus ventas: "))

calculo_comision = venta_empleado * 0.13

print(f"{nombre_empleado}, tu comisión es de: Q{calculo_comision:.2f}")