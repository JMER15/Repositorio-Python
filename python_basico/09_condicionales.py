"""
Condicionales en Python
Autor: José Miguel Escribano Ruiz
Fecha: 22/09/2023
Descripción: Programa que muestra el uso de condicionales en Python

"""

### Condicionales ###

# if
# if-else
# if-elif-else

# ejemplo 1
numero = 6
if numero == 5:
    print("El número es igual a 5")
elif numero > 5:
    print("El número es mayor que 5")
else:
    print("El número es menor que 5")

# ejemplo 2
if numero > 0:
    print("El número es positivo")
else:
    print("El número es negativo")

# ejemplo 3
cadena = "Hola"
if len(cadena) > 0:
    print("La cadena no está vacía")
else:
    print("La cadena está vacía")

# ejemplo 4 mayor de edad
edad = 18
if edad >= 18:
    print("Es mayor de edad")
elif edad < 0:
    print("Edad incorrecta")
else:
    print("Es menor de edad")