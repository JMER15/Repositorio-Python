"""
Funciones de orden superior en Python
Autor: José Miguel Escribano Ruiz
Fecha: 28/09/2023
Descripción: Ejemplos de funciones de orden superior en Python

"""

### Funciones orden superior en python ###
# Funciones que reciben funciones como parámetros

from functools import reduce

def sumaUno(num):
    return num + 1

def sumarValores(num1, num2, f_sum): # f_sum es una función de orden superior
    return f_sum(num1+num2)

print(sumarValores(5,2, sumaUno))

### Clousures ###
# Funciones que devuelven funciones

def sumaDiez(value):
    def suma(num):
        return num + 10 + value
    return suma

clousure = sumaDiez(5)
print(clousure(5))

# otra forma de llamar a la función clousure
print(sumaDiez(5)(1))

### Funciones de orden superior predefinidas en Python ###
# map
# Aplica una función a cada uno de los elementos de una lista iterable

numeros = [2,5,10,23,50,33]

def multiplicarDos(num):
    return num * 2

print(list(map(multiplicarDos,numeros)))
print(list(map(lambda numero: numero * 2, numeros))) # mejor usar lambda para evitar crear la función multiplicarDos

# filter
# Filtra los elementos de una lista iterable que cumplan una condición

def filtrarPares(numero):
    return numero % 2 == 0

print(list(filter(filtrarPares, numeros)))
print(list(filter(lambda numero: numero % 2 == 0, numeros)))

# reduce
# Aplica una función a todos los elementos de una lista iterable

def sumaDos(num1,num2):
    print(num1)
    print(num2)
    return num1 + num2

print(reduce(sumaDos, numeros))