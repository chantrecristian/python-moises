"""
Variables locales: se definen dentro de la funcion y no 
se puede usar fuera de ella,solo estan disponebles dentro.

Variables globales :so las que se declaran fuera de una funcion 
y estan disponibles dentro y fuera de ellas.
"""
#variables Global
frase = "Ni los genios son tan genios, ni los mediocres tan mediocres"
print(frase)

def holamundo():
    #frase=  "Hola Mundo!!"
    print(frase)
holamundo()