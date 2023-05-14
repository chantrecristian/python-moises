nombre="ADSI SENA AgroTics"

#Funciones Generales
print(type(nombre))

#Dectetar el tipado
comprobar = isinstance(nombre,str)
if comprobar:
    print("Esa variable es un String")
else:
    print("Esa variable NO es un String")
if not isinstance(nombre,float):
    print("esa variable NO es un numero con decimales")

#Limpiar espacios de un String
frase="    mi contenido     "
print(frase)
print(frase.strip())

#Eliminar variable
year=2022
print (year)
del year
#print(year)

#comprobar variable vacia
texto = " fff "
if len (texto)<= 0:
    print("la variable esta vacia")
else:
    print("la variable tiene contenido:" , len(texto))

#Encontrar caracteres en un texto
frase= "la vida es bella"
print(frase.find ("vida"))

#Reemplazar palabras en un string
nueva_frase= frase.replace ("vida", "moto")
print(nueva_frase)

#Mayusculas y Minusculas
print (frase)
print(frase.lower())
print(frase.upper())
