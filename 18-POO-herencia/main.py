import clases #se importa toda la clase para tener acceso a todo el archivo

persona = clases.Persona() # se crea un objeto persona
# asignacion de valores 
persona.setNombre("Carlos")
persona.setApellidos("Sanchez Garcia")
persona.setAltura("170 cm")
persona.setEdad("40 años")

#mostar ñas diferentes propiedades
print(f"la persona es: {persona.getNombre()} {persona.getApellidos()}")
print(persona.hablar())# se accede a metodos en concreto
print("---------------------********----------------------")
# creacion del onjeto informatico
informatico = clases.Informatico() #accede a la clase informatico
informatico.setNombre("Julian Andres") # Se asignan nuevos voladores al objeto informatico
informatico.setApellidos("Perez Martinez")

print(f"El informatico es: {informatico.getNombre()} {informatico.getApellidos()}")
print(informatico.getLenguajes())
print(persona.hablar()) #herencia
print("--------------------********-------------------")

tecnico = clases.TecnicoRedes()
tecnico = clases.Informatico() #accede a la clase informatico
tecnico.setNombre("Juan Esteban") # Se asignan nuevos voladores al objeto informatico
tecnico.getLenguajes

print(f"Experto {tecnico.getNombre()} {tecnico.getLenguajes()}")



