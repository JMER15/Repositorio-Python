"""
Retos de programación en Python
Autor: José Miguel Escribano Ruiz
Fecha: 27/09/2023
Descripción: Retos de programación en Python

"""

### Challenges ###

"""
EL FAMOSO "FIZZ BUZZ”:
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

def fizzbuzz():

    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0: # es la condición más restrictiva, por eso va primero
            i="fizzbuzz"
        elif i % 3 == 0:
            i="fizz"
        elif i % 5 == 0:
            i="buzz"
        print(i)

fizzbuzz()

"""
¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""

def anagrama(string1, string2):
    
    if string1.lower() == string2.lower():
        return False
    return sorted(string1.lower()) == sorted(string2.lower())
    
print(anagrama("roma", "amor"))
print(anagrama("roma", "amorr"))

"""
Crea una función que encuentre todos los triples pitagóricos
(ternas) menores o iguales a un número dado.
 - Debes buscar información sobre qué es un triple pitagórico.
 - La función únicamente recibe el número máximo que puede
   aparecer en el triple.
 - Ejemplo: Los triples menores o iguales a 10 están
   formados por (3, 4, 5) y (6, 8, 10).
"""

def triples_pitagoricos(number):
    for a in range(1,number+1): # el +1 es para que incluya el número que le pasamos
        for b in range(a,number+1):
            for c in range(b,number+1):
                if a**2 + b**2 == c**2:
                    print(a,b,c)

### otra solucion quitando el bucle de c
def triples_pitagoricos1(number):
    triples = []
    for a in range(1, number+1):
        for b in range(a,number+1):
            c_cuadrado = a**2+b**2
            c = int(c_cuadrado**0.5)
            if c <= number and a**2 + b**2 == c**2: # c tiene que ser menor e igual a number 
                triples.append((a,b,c))
    return triples

triples_pitagoricos(20)
result = triples_pitagoricos1(20)

for triple in result:
    print(triple)

