"""
Clases en Python
Autor: José Miguel Escribano Ruiz
Fecha: 25/09/2023
Descripción: Programa que muestra el uso de clases en Python

"""

### Clases ###

class PersonaVacia:
    pass

print(PersonaVacia)
print(type(PersonaVacia))
print(PersonaVacia())

class Persona:
    # self es el this de Javascript
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def caminar(self):
        print(self.nombre, "Está caminando")

miPersona = Persona("Jose", 30)
print(miPersona.edad)
print(f"{miPersona.nombre} tiene {miPersona.edad} años")
miPersona.caminar()

# Herencia
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def trabajar(self):
        print(self.nombre, "Está trabajando")

miEmpleado = Empleado("Jose", 30, 1000)
print(miEmpleado.sueldo)
miEmpleado.trabajar()

# Privacidad con getters y setters
class PersonaPrivada:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad

miPersonaPrivada = PersonaPrivada("Jose", 30)
print(miPersonaPrivada.get_nombre())
print(miPersonaPrivada.get_edad())
miPersonaPrivada.set_nombre("Juan")
miPersonaPrivada.set_edad(40)
print(miPersonaPrivada.get_nombre())
print(miPersonaPrivada.get_edad())





