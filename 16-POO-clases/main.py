# Programacion orientada a objetos (POO o OOP)
#Definir una clase (molde para crear mas objetos de ese tipo
#en nuestro caso (carro) con caracteristicas similares)

class Carro:
    #atributos  propiedades
    #caracteristicas del carro
    color="rojo"
    marca="ferrari"
    modelo="aventador"
    velocidad=300
    caballaje=500
    plazas=2

    #metodos, son acciones que hace el objeto (cohe) (funciones)
    def acelerar (self):
        self.velocidad +=1

    def frenar (self) :
        self.velocidad -= 1

    def getvelocidad (self):
        return self.velocidad



    def setcolor (self, color):
        self.color = color

    def getcolor (self):
        return self.color

    def setmodelo(self, modelo):
        self.modelo = modelo
    
    def getmodelo (self):
        return self.modelo
#fin definicion de clase

# crear objeto / instanciar la clase
print ("----------------------- CARRO 1 :---------------------------")
carro = Carro()   
print(carro.marca, carro.color)
print("velocidad actual: ", carro.velocidad)
carro.acelerar()
carro.acelerar()
carro.acelerar()
carro.acelerar()
carro.frenar()
print("velocidad nueva", carro.getvelocidad())


carro = Carro()
carro.setcolor("amarillo")
carro.setmodelo("murcielago")
print(carro.marca, carro.getmodelo(), carro.getcolor())

print ("----------------------- CARRO 2 :---------------------------")
print("CARRO 2:")
#crear ,mas objetos
carro2 = Carro()

carro2.setcolor("verde")
carro2.setmodelo("gallardo")
print(carro2.marca, carro2.getmodelo(), carro2.getcolor())

