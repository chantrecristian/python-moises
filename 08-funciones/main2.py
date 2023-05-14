"""
FUNCIONES:
una funcion es un conjunto de instrucciones agrupadas bajo un nombre concreto que pueden reutilizarse 
invocando a la funcion cuantas veces sea necesario. EJEMPLO de sintaxis: 

def nombreDeMiFuncion(parametros):
    #bleque de codigo / conjunto de instrucciones 
#invocar 
nombreDeMiFuncion(mi_parametro)
"""
#ejemplo 1
print("####### EJEMPLO 1 #######")
#Definir funcion 
def muestraNombre():
    print("Victor")
    print("Pedro")
    print("Juan")
    print("Juan")
    print("Felipe")
    print("Santiago")
    print("sandra")

    #invocar funcion 
muestraNombre()


#EJEMPLO 2-PARAMETROS
print("####### EJEMPLO 2 #######")

def mostrarTuNombre(nombre): #parametro
    print(f"tu nombre es: {nombre}")

nombre = input(F" instroduce tu nombre:")
mostrarTuNombre(nombre)

def mostrarTuNombre (nombre, edad): #parametro
    print (f" tu nombre es: {nombre}")
    if edad >= 18:
        print(F"y eres mayor de edad")
nombre = input ("introduce tu nombre:")        
mostrarTuNombre(nombre, 19)

#ejemplo 2 paramtros

print("############### ejemplo 3 parametros tablas de multiplicar ################")

def tabla (numero):
    print(f"tabla de multiplicar del numero:{numero}")

    for contador in range (5):
        operacion = numero*contador
        print(f"{numero} x {contador} = {operacion}")

    print("\n")  # salto de linea 
tabla (1)
tabla (2)
tabla (3)
tabla (4)
tabla (5)
tabla (6)
tabla (7)
tabla (8)
tabla (9)
tabla (10)

# ejemplo 4 - parametros operacionales 
print("############### ejemplo 4 parametros opcionales ################")

def getEmpleado(nombre, dni = None):
    print("empleado")
    print(f"nombre: {nombre}")
    if dni != None:
        print(f"DNI:{dni}")

getEmpleado("cristian chantre,1058547567")       


print("############### ejemplo 7 funcion lambda ################")

dime_el_year = lambda year : f"el año es {year}"
print(dime_el_year(2023))
