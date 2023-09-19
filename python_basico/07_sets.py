"""
Sets
Autor: José Miguel Escribano Ruiz
Fecha: 19/09/2023
Descripción: Programa que muestra el uso de los sets

"""

### Sets ###
# Los sets son colecciones desordenadas y sin indice, no permite duplicados
set = set() # Creamos un set vacío
set2 = {} # Esto no es un set, es un diccionario

print(set)
print(type(set))
print(type(set2))

set = {1,'josemi',3.14} # Set con valores
print(set)
print(type(set))

### operaciones con sets ###
print(len(set)) # Número de elementos del set
print(1 in set) # Buscar un elemento en el set

set.add(10) # Añadir un elemento al set
print(set) # no es una estructura ordenada

set.remove(1) # Eliminar un elemento del set
print(set)

set.clear() # Vaciar el set
print(set)

# del set Eliminar el set
# print(set) NameError: name 'set' is not defined

set = {'a','b','c'}
set3 = set.union({1,2,3}) # Unir dos sets
print(set3)

print(set3.difference({1,2,3})) # Diferencia entre dos sets