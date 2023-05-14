"""
#BUCLE WHILE
 estrucctura de control que intera o repite la ejecucion de una serie de instrucciones
 tantas veces como sea necesario, hasta que deje se cumplirse la condicion.

contador 
while condicion: 
    bloque de instrucciones 
    actualizacion de control    


contador = 1
while contador <= 100:
    print(f"estoy en el numero. {contador}")
    contador += 1

print("------------------------------------------------------")
contador = 1
muestrame = str(0)
while contador <= 100:
    muestrame = muestrame + ", " + str(contador)
    contador += 1
    print(muestrame)
"""
#EJEMPLO 

print("#### ejemplo ###")

numero_usuario = int(input("¿de que numero quieres la tabla?:")) #creacion de vaiable con parseo int 
if numero_usuario < 1: #comprobar si numero de usuario es menor a 1
    numero_usuario = 1 #le damos un valor de usuario que sera 1
print(f"### tabla del {numero_usuario}###") #se muestra la tabla de multiplicar 
contador = 1 #se define el contador 
while contador <= 10 : # mientras el contador sea menor o igual a 10 sigue entrando el bucle
    print(f"{numero_usuario}x{contador}={numero_usuario*contador}") #y muestra la multiplicacion
    contador += 1 #actualizamos el contador para uno de factores 
else: # si no 
    print("tabala terminada.") #termina    