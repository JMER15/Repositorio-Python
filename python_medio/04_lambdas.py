"""
Lambdas en Python
Autor: José Miguel Escribano Ruiz
Fecha: 28/09/2023
Descripción: Ejemplos de lambdas en Python

"""

### Lambdas ###

# equivalente a una función anónima en JS
sum = lambda num1, num2: num1 + num2
print(sum(5, 5))

multiply = lambda num1, num2: num1 * num2 - 3
print(multiply(5, 5))

def sumarTresNumeros(value):
    return lambda num1, num2: num1 + num2 + value

print(sumarTresNumeros(5)(5, 5))
