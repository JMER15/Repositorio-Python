"""
Tipos de errores en Python
Autor: José Miguel Escribano Ruiz
Fecha: 28/09/2023
Descripción: Ejemplos de tipos de errores en Python

"""

### Tipos de errores en Python ###

# SyntaxError
# print "Hola comunidad" # Descomentar para Error
print("Hola comunidad")

# NameError
# print(name)  # Descomentar para Error
name = "josemi"
print(name)

# IndexError
list = [1,2,3]
# print(list[6]) # Descomentar para Error
# print(list[7])
print(list[1])
print(list[-1])

# ModuleNotFoundError
# import maths # Descomentar para Error
import math

# AtributeError
# print(math.PI) # Descomentar para Error
print(math.pi)

# KeyError
dict = {'name':'josemi', 'age': 27, 1: 'one'}
# print(dict['nameee']) # Descomentar para Error
print(dict['name'])

# TypeError
# print(list['nombre']) # Descomentar para Error
print(list[1])

# ImportError
# from math import sqrtt # Descomentar para Error
from math import sqrt as raiz

# ValueError
# int = int("10 años") # Descomentar para Error
int = int("10")
print(int)

# ZeroDivisionError
# print(10/0) # Descomentar para Error
print(10/2)