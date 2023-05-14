"""
Proyecto Python MYsql
-abrir asistente 
-login o registro 
-si elegimos registro, creara un usuario en la bbdd
-si elegimos login, identifica al usuario y nos preguntara
-crear nota, mostrar, borrar.
"""

#importamos las acciones 
#desde el paquete usuarios importamos el modulo acciones 
from usuarios import acciones 

#realizamos el menu de opciones 
#print con comilla triple para hacer varios prints
print("""
Acciones disponibles:
    - registro
    -login
""")
hagaEL = acciones.Acciones() # instanciando mi clase
accion = input("¿Que quieres hacer?:")
if accion == "registro":
    hagaEL.registro() #invoca el metodo registro
elif accion == "login":
    hagaEL.login()#invoca el metodo login



