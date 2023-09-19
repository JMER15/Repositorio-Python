"""
Listas
Autor: José Miguel Escribano Ruiz
Fecha: 18/09/2023
Descripción: Programa que muestra el uso de listas

"""

### Listas ###
lista = list() # Lista vacía
lista2 = [] # Lista vacía otra forma

### ver longitud de una lista ###
print(len(lista))
print(len(lista2))

lista = [35,2,3,4,35,6,7,8,9,10] # Lista con valores
print(lista)

lista2 = [1,2,3,4,5,6,7,8,9,10,"hola",3.14] # Lista con valores de diferentes tipos
print(lista2)

### Acceder a un elemento de la lista ###
print(lista[0]) # Primer elemento de la lista
print(lista[1]) # Segundo elemento de la lista
print(lista[-1]) # Último elemento de la lista
# print(lista[-12]) IndexError: list index out of range
print(lista.count(35)) # Número de veces que aparece el 35 en la lista

### Destructuring ###
primero, segundo, tercero, *resto = lista # Asignación múltiple
print(primero)
print(segundo)

### concatenar listas ###
print(lista + lista2)

### añadir elementos a una lista ###
lista.append(11)
print(lista)
lista.insert(0,0) # Añadir un elemento en una posición concreta
print(lista)

### eliminar elementos de una lista ###
lista.pop() # Elimina el último elemento de la lista
print(lista)
lista.pop(0) # Elimina el elemento de la posición 0
print(lista)
lista.remove(35) # Elimina el elemento 35 de la lista
print(lista)

del lista[0] # Elimina el elemento de la posición 0
print(lista)

### borrar lista ###
lista.clear()
print(lista)

### copiar la lista ###
lista4 = lista.copy()
print(lista4)

### ordenar lista ###
lista5 = [1,5,3,2,6,8,4,7,9]
lista5.sort() # Ordena la lista
print(lista5)

### revertir lista ###
lista5.reverse() # Invierte la lista
print(lista5)

### sublistas ###
lista6 = [1,2,3,4,5,6,7,8,9,10]
sublista = lista6[0:5] # Sublista desde la posición 0 a la 5
print(sublista)