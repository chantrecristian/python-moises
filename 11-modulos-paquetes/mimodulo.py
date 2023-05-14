def holamundo(nombre):
    return f"hola como estas, {nombre}"

def calculadora(numero1, numero2, basicas = False):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2
    cadena=""

    if basicas != False:
        cadena += "suma:"+ str(suma)
        cadena += "\n"
        cadena += "resta:" + str(resta)
        cadena += "\n"
    else:
        cadena +="multiplicacion:" + str(multiplicacion)
        cadena +="\n"
        cadena +="division:" + str(division) 
        cadena +="\n"
    return cadena

        


        

