#HERENCIA: es la posibilidad de compartir atributos y metodos 
# entre clases. Y que diferentes clases hereden de otras
class Persona: # Definimos la clave PADRE el molde
# Metodos: Getters and Setters
# con los get se obtienen las propiedades cuando se cree el objeto 
   def getNombre(self): #obtener el nombre 
      return self.nombre
   
   def getApellidos(self):
      return self.apellidos 
   
   def getAltura(self):
      return self.altura 
   
   def getEdad(self):
      return self.edad 
   
   def setNombre(self,nombre):
      self.nombre = nombre 
      
    # con los set se asignan los diferentes a las propiedades del objeto
   def setApellidos(self, apellidos):
      self.apellidos = apellidos

   def setAltura(self, altura):
      self.altura = altura

   def setEdad(self, edad)  :
      self.edad = edad 
    
    #otras propiedades de los objetos de la clase 

   def hablar(self):
        return"estoy hablando"
   def caminar(self):
      return"estoy caminando"
   #************** HERENCIA *********************
class Informatico(Persona): # se crea una clase informatico que hereda de la clase PADRE -> persona
    """
    lenguajes
    experiencia
    """
    def __init__(self): #propiedaddes por defecto
        self.lenguajes = "HTML, CDD, JavaScript, PHP"
        self.experiencia = 5

    def getLenguajes(self): # get
        return self.lenguajes
   
    def aprender(self, lenguajes):
        self.lenguajes=lenguajes
        return self.lenguajes
   
    def programar(self):
     return "Estoy programando"
   
    def repararPC(self):
       return "He reparado la PC"
   
      

    def repararPC(self):
       return "He reparado el PC"
class TecnicoRedes(Informatico): # Herencia de informatico y a su vez de perosna
    
    def __init__(self): #constructor
       super().__init__() #Funciones super para traer el constructor
       self.auditarRedes = "Experto"
       self.experiencia = 10

    def auditoria(self):
       return "estoy auditando una red"
    
 