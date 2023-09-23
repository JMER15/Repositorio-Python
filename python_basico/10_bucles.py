"""
Bucles en Python
Autor: José Miguel Escribano Ruiz
Fecha: 23/09/2023
Descripción: Programa que muestra el uso de bucles en Python

"""

### Bucles ###

### while ###

# ejemplo 1
numero = 1
while numero <= 10:
    print(numero)
    numero = numero + 1

# ejemplo 2
contador = 0
while contador <= 10:
    print("Estoy en el bucle while", contador)
    contador = contador + 1
    if contador == 5:
        break # rompe el bucle cuando llega a 5

# ejemplo 3
contador = 0
while contador <= 10:
    contador = contador + 1
    if contador == 5:
        continue # salta la iteración cuando llega a 5
    print("Estoy en el bucle while", contador)

### for ###

# ejemplo 1
for numero in range(1, 11):
    print(numero)

# ejemplo 2
for numero in range(1, 11):
    print("Estoy en el bucle for", numero)

# ejemplo 3
list = ["uno", "dos", "tres", "cuatro", "cinco"]
for elemento in list:
    print(elemento)

# ejemplo 4
lenguaje = 'Python'

for letter in lenguaje:
    print(letter)

for i in range(len(lenguaje)):
    print(lenguaje[i])

# ejemplo 5
numeros = (0,1,2,3,4,5)
for number in numeros:
    print(number)
    if number == 3:
        break # rompe el bucle cuando llega a 3

# ejemplo 6
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

### do while ###
# No existe en Python

### switch ###
# No existe en Python

