"""
Strings
Autor: José Miguel Escribano Ruiz
Fecha: 18/09/2023
Descripción: Programa que muestra el uso de strings

"""

### Strings ###
string = "Hola Python ¿Qué tal?"
string2 = 'Hola Python ¿Qué tal estás?'

### longitud de un string método len()###
print(len(string))
print(len(string2))

### concatenación de strings ###
print(string + " " + string2)

# Formateo
name, surname, age = "Josemi", "Escribano Ruiz", 27

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaqueado de caracteres
language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

# División
languajeSlice = language[1:3] #[1,3)
print(languajeSlice)

languajeSlice = language[1:] #[1,fin)
print(languajeSlice)

languajeSlice = language[-2] 
print(languajeSlice)

languajeSlice = language[0:6:2] 
print(languajeSlice)

# Reverse
languajeReverse = language[::-1] 
print(languajeReverse)

# Funciones del lenguaje
print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.lower().isupper())
print(language.startswith("Py"))
print("Py" == "py")  # No es lo mismo

