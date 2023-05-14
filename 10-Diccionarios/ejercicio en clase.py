"""
Hacer un programa que haga una lista de 8 numeros enteros, y haga lo siguientes:
- recorrer la lista y mostrarla
- Hacer una funcion que recorra la lista de numeros  y devuelva un string
-Ordenarla y mostrarla
-Mostrar su longitud
-Buscar un elemento que el usuario pida por teclado
"""

print("------- 1 ------------")
numero=[13,64,67,45,43,21,91]
for numero in numero:
    print(numero)

print("------- 2 ------------")

numero=[13,64,67,45,43,21,91]
print(numero) 
print(type(numero)) 

print("------- 3 ------------")
numero = [13,64,67,45,43,21,91]
numero.sort()
print(numero) 

print("------- 4 ------------")
numero = [13,64,67,45,43,21,91]
for i in range(0, len(numero)):
    print(numero[i])


print("------- 5 ------------")
numero = ["13","64","67","45","43","21","91"]
lista = input('Digite el numero a buscar ')
if numero.count(lista) > 0:
    print("numero encontrado")
else:
    print("Numero no resgistrado")

