"""
Módulos en Python
Autor: José Miguel Escribano Ruiz
Fecha: 25/09/2023
Descripción: Programa que muestra el uso de módulos en Python

"""

### Módulos ###

# Un módulo es un fichero que contiene código Python. Puede contener funciones, clases, variables, etc.
# Para usar un módulo en un programa Python es necesario importarlo.

import modulo  #si queremos importar todo el módulo
modulo.sum(3,4)

# from modulo import sum si queremos importar solo una función
from modulo import sum, res
sum(3,4)
res(3,4)

# modulos de terceros
import math #modulo de matematicas

print(math.pi)
print(math.e)
print(math.sin(30))

# alias
import math as m
print(m.pi)