"""
Excepciones en Python
Autor: José Miguel Escribano Ruiz
Fecha: 25/09/2023
Descripción: Programa que muestra el uso de excepciones en Python

"""

### Excepciones ###

try:
    print(2/0)
except:
    print("Error al dividir por cero.")
else:
    print("No hay error.")
finally:
    print("Fin del programa.")

### Excepciones con nombre ###
try:
    print(2/0)
except ZeroDivisionError:
    print("Error al dividir por cero.")
else:
    print("No hay error.")
finally:
    print("Fin del programa.")

### Excepciones con nombre y mensaje ###
try:
    print(2/0)
except ZeroDivisionError as error:
    print("Error al dividir por cero:", error)
else:
    print("No hay error.")
finally:
    print("Fin del programa.")

