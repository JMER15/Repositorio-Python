"""
Ficheros en Python
Autor: José Miguel Escribano Ruiz
Fecha: 30/09/2023
Descripción: Ejemplos de manejo de ficheros en Python

"""

### Ficheros de texto ###
import os

# .txt
# abrir fichero
# file = open("python_medio/fichero.txt", "r+") # r+ lectura y escritura
file = open("python_medio/fichero.txt", "w+") # w+ escritura y lectura
file.write("aa\naa\naa")

#print(file.read()) # leer fichero
#print(file.read(2)) # leer 2 caracteres

# print(file.readline()) # leer linea
# print(file.readline())

for line in file.readlines():
    print(line)

# escribir fichero
file.write("\nHola mundo")
print(file.read())

file.close() # cerrar fichero
# os.remove("python_medio/fichero.txt") # borrar fichero

# .json
import json # importar libreria json
json_file = open("python_medio/fichero.json", "w+") # w+ escritura y lectura

json_test = {"nombre": "Jose", 
             "edad": 30, 
             "ciudad": "Madrid",
             "lenguajes": ["Python", "Java", "PHP"]}

json.dump(json_test, json_file, indent=4) # escribir fichero json
json_file.close()

json_dict = json.load(open("python_medio/fichero.json")) # leer fichero json
print(json_dict) 

# .csv
import csv # importar libreria csv
csv_file = open("python_medio/fichero.csv", "w+") # w+ escritura y lectura
csv_writer = csv.writer(csv_file) # crear objeto writer
csv_writer.writerow(["Nombre", "Edad", "Ciudad"]) # escribir cabecera
csv_writer.writerow(["Jose", 30, "Madrid"]) # escribir fila

csv_file.close()

with open("python_medio/fichero.csv", "r+") as csv_file:
    for line in csv_file.readlines():
        print(line)

# .xlsx
# import xlrd # importar libreria xlrd

# .xml