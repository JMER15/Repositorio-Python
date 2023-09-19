"""
Tuplas
Autor: José Miguel Escribano Ruiz
Fecha: 19/09/2023
Descripción: Programa que muestra el uso de tuplas

"""

### Tuplas ###
# Las tuplas son inmutables, es decir, no se pueden modificar 
tupla = tuple() # Creamos una tupla vacía
tupla2 = () # otra forma de crear una tupla

miTupla = (10,24,'josemi',3.14,10) # Tupla con valores
miTupla2 = (60,40,20) # Tupla con valores otra forma

print(miTupla)
print(type(miTupla))

### Acceder a un elemento de la tupla ###
print(miTupla[0]) # Primer elemento de la tupla
print(miTupla[1]) # Segundo elemento de la tupla
print(miTupla[-1]) # Último elemento de la tupla

print(miTupla.count(10)) # Número de veces que aparece el 10 en la tupla
print(miTupla.index('josemi')) # Posición en la que se encuentra 'josemi'

# miTupla[0] = 11  TypeError: la tupla es un objeto inmutable

### sumar tuplas ###
miTupla3 = miTupla + miTupla2
print(miTupla3)

### buscar elementos ###
print(miTupla3[3:6]) # Buscar elementos desde la posición 3 a la 6

### Destructuring ###
primero, segundo, tercero, *resto = miTupla3 # Asignación múltiple
print(primero)
print(segundo)