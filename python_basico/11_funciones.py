"""
Funciones en Python
Autor: José Miguel Escribano Ruiz
Fecha: 23/09/2023
Descripción: Programa que muestra el uso de funciones en Python

"""

### Funciones ###

#ejemplo 1
def funcion():
    print('Esto es una función')

funcion()

#ejemplo 2
def suma(a, b):
    return a + b

print(suma(2, 3))

resultado = suma(2, 3)
print(resultado)

#ejemplo 3
def saludo(name, surname):
    print(f"{name} {surname}")

saludo(surname="Escribano Ruiz", name="José Miguel")

#ejemplo 4
def letrasMayusculas(*texts):
    print(type(texts))
    for text in texts:
        print(text.upper())

letrasMayusculas("Hola", "Python", "Josemi")
letrasMayusculas("Hola")

# ejemplo 5
def mostrarElementos():
    elementos = ['uno','dos']
    for element in elementos:
        print(element)

mostrarElementos()