"""
Fechas en Python
Autor: José Miguel Escribano Ruiz
Fecha: 27/09/2023
Descripción: Programa que muestra el uso de fechas en Python

"""

### Dates ###

# Importamos el módulo datetime
from datetime import datetime

# Creamos una fecha
now = datetime.now()

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(now)

# creamos uan fecha 
newYear = datetime(2023, 1, 1)
print_date(newYear)

# Creamos una fecha con formato
now = datetime.now()
print(now.strftime('%d/%m/%Y %H:%M:%S'))
print(now.strftime('%d/%m/%y %H:%M:%S'))

# importamos el módulo time hay que rellenar los campos sino es 0,0,0 por defecto
from datetime import time

currentTime = time(21, 30, 0)
print(currentTime.hour)
print(currentTime.minute)
print(currentTime.second)

# importamos el módulo date
from datetime import date

currentDate = date.today()
print(currentDate.year)
print(currentDate.month)
print(currentDate.day)

currentDate = date(2023, 1, 1)
print(currentDate.year)
print(currentDate.month)
print(currentDate.day)

# modificamos la fecha
currentDate = date(currentDate.year + 1, currentDate.month + 1, currentDate.day + 1)
print(currentDate.year)
print(currentDate.month)

# restamos fechas del mismo tipo
diff = newYear - now
print(diff)
diff = newYear.date() - currentDate
print(diff)

from datetime import timedelta
timeDelta1 = timedelta(days=365, hours=8, minutes=15)
timeDelta2 = timedelta(days=365)
print(timeDelta1-timeDelta2)
print(timeDelta1+timeDelta2)



