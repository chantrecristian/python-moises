class Carro:
    #atributos  propiedades
    #caracteristicas del carro
    color="rojo"
    marca="ferrari"
    modelo="aventador"
    velocidad=300
    caballaje=500
    plazas=2


    soy_publico = "Hola soy un atributo publico"
    __soy_privado = "Hola soy un atributo privado"
#definir constructor
    def __init__(self, color,marca,modelo,velocidad,caballaje,plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas
    #metodos, son acciones que hace el objeto (cohe) (funciones)
    def getPrivado(self):
        return self.__soy_privado
    
    def setColor (self, color):
        self.color = color

    def getColor (self):
        return self.color
    
    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo (self):
        return self.modelo    

    def setMarca (self, marca):
        self.marca = marca

    def getMarca (self):
        return self.marca    

    def acelerar (self):
        self.velocidad +=1

    def frenar (self) :
        self.velocidad -= 1

    def getVelocidad (self):
        return self.velocidad

    def getInfo(self):
        info = "------ Informacion del carro ---------------"
        info += "\n Color: " + self.getColor()
        info += "\n Marca: " + self.getMarca()
        info += "\n Modelo: " + self.getModelo()
        info += "\n Velocidad: " + str(self.getVelocidad())

        return info


#fin definicion de clase