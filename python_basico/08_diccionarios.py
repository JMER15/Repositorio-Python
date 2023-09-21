"""
Diccionarios
Autor: José Miguel Escribano Ruiz
Fecha: 21/09/2023
Descripción: Programa que muestra el uso de los diccionarios

"""

### Diccionarios ###
# Los diccionarios son colecciones desordenadas, mutables e indexadas. No permiten duplicados
diccionario = dict() # Creamos un diccionario vacío
diccionario2 = {} # Creamos un diccionario vacío

print(diccionario)
print(type(diccionario))

diccionario = {'marca':'seat','modelo':'ibiza','año':2000} # Creamos un diccionario con valores
print(diccionario)

diccionario2 = {
    'marca':'Opel',
    'modelo':'Corsa',
    'año':2007,
    'colores':['rojo','verde','azul'] # Los valores pueden ser de cualquier tipo
}

print(diccionario2)
print(len(diccionario2)) # Número de elementos del diccionario

# Acceso a los elementos del diccionario
print(diccionario2['marca']) # Accedemos al valor de la clave marca
print(diccionario2.get('marca')) # Accedemos al valor de la clave marca

# Modificar valores
diccionario2['marca'] = 'Renault'
print(diccionario2['marca'])

# Borrado de elementos
diccionario2.pop('marca') # Eliminamos la clave marca
print(diccionario2)

del(diccionario2['modelo']) # Eliminamos la clave modelo
print(diccionario2)

# ver si existe una clave
print('año' in diccionario2) # Devuelve True si existe la clave año en el diccionario

print(diccionario2.items()) # Devuelve las claves y los valores del diccionario
print(diccionario2.keys()) # Devuelve las claves del diccionario
print(diccionario2.values()) # Devuelve los valores del diccionario
print(diccionario2.fromkeys(( 'año', 2007))) # Crea un diccionario con las claves y valores indicados
