"""
#FOR, esructura interactiva que se repite 
for variable en elemento_iterable (lista, rango , etc)
 Bloque  de instrucciones 
"""
"""
contador = 0
resultado = 0

for contador  in range (0,10):
    print("Voy por el "+ str(contador))
    resultado = resultado + contador

    print(f"El resultado es:{resultado}")

    """

    #EJEMPLO TABLAS DE MULTIPLICAR 
print("\n############## EJEMPLO 1 ###############")

numero_usuario = int (input("¿de que numero quiere la tabla?:"))

if numero_usuario <= 1:
    numero_usuario = 1

print (f" ### tabla de multiplicadar del numero {numero_usuario} ###")

for numero_tabla in range (0,10):
    if numero_usuario>= 10:
        print("solo se admiten numeros del 1 al 9")
        break
    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}")
else: 
    print(f"tabal {numero_usuario} finalizada")    

