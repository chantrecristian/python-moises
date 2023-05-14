"""
Modulos : son funcionaliddes ya hechas para reutilizar
"""

#Importar Modulo Propio
import mimodulo

print(mimodulo.holamundo("carlos gomez"))
print(mimodulo.calculadora(3,5,True))
print("-----------------------------------")
#Otra froma de llamar modulo
from mimodulo import holamundo
print(holamundo("juan perez"))
print("-------------------------")

#Llamar todas las funciones de mi modulo 
from mimodulo import *
print(holamundo("sandra sanchez"))
print(calculadora(8,4,True))

#modulo fechas
print("modulo fechas")
print("-------------------------")
import datetime
print(datetime.date.today())

#fecha completa con tiempo
print("fecha completa con tiempo")
print("----------------------")
fecha_completa = datetime.datetime.now()
print(fecha_completa)

print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%D/%M/y,%H:%M:%S")
print(f" mi fecha personalizada: {fecha_personalizada}")

print("----------------------")
#modulo matematicas
print("modudlo matematicas")
import math
print("raiz cuadra de 10:", math.sqrt(10))
print("numero pi:", math.pi)
print("redondear:", math.ceil(5.34562))
print("redonder:", math.floor(5.34562))

#modulo random
import random
print("numero aleatorio entre 15 y 67:", random.randint(15,67))

