"""
List Comprehension en Python
Autor: José Miguel Escribano Ruiz
Fecha: 27/09/2023
Descripción: Programa que muestra el uso de List Comprehension en Python

"""

### List Comprehension ###

listaOriginal = [0,1,2,3,4,5,6,7]
print(listaOriginal)

# lista comprimida
list = [i for i in range(8)]
print(list)

list = [i + 2 for i in range(8)]
print(list)

def cuadrado(x):
    return x*x

list = [cuadrado(i) for i in range(8)]
print(list)