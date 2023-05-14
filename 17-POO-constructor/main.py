from carro import Carro

carro = Carro("azul","renault","clio",150,200,4)
carro1 = Carro("amarillo","chebroley","corsa",250,200,4)
carro2 = Carro("rojo","citroen","xara",350,200,4)
carro3 = Carro("negro","volkwagen","virtus",400,200,4)
#print(carro.getcolor())

print(carro.getInfo())
print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())

#DETECTAR TIPADO
carro3 = "Aleatorio"
if type(carro3) == Carro:
    print("Es un objeto correcto")
else: 
    print("No es un obtejo!!")    

#visibilidad 
print(carro.soy_publico)
#print(carro.__soy_privado)
print(carro.getPrivado())