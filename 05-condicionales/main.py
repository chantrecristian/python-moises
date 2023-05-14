"""
#estructura de control que me permite controlar el flujo del programa condicional IF


SI se_cumple_esta_condicion:
   ejecutar grupo de instrucciones 
SI NO : se ejecutan otro grupo de instrucciones 

en python 

if condiciones:
   instrucciones
else: 
    otras instrucciones

"""
#ejemplo 1 
"""
print("######## EJEMPLO 1 ########")

#color = "rojo"
# operador de comparacion ==
color = input("adivina cual es mi color favorito:")
if color == "rojo":
     print("el color es ROJO")
else:
    print("Color incorrecto!!")

print("\n ########## EJEMPLO 2 #############")

year = 2021 #  variable que me compare el año 

if year >= 2022:
    print("Estamos de 2022 en adelante!!")
else: 
    print("Es un año anterior al 2022")  

print("\n ########## EJEMPLO 3 #############") 

nombre = "cristian"
cuidad = "Popayan"
continente= "America"
edad = "40"
mayoria_edad = "18"

if edad >= mayoria_edad:
    #instrucciones 
    print(f"{nombre} es mayor de edad!!")
    if continente != "America":
        print("El usuario no es americano")
    else :
        print(f"Es americano y de cuidad:{cuidad}")    
else :
        print(f"{nombre} No es mayor de edad")     


print("\n ########## EJEMPLO 4 #############") 

dia =  int ( input("introduce el numero del dia de la semana"))     

if dia == 1:
    print("Es lunes")
else: 
    if dia == 2:
        print("Es Martes")
    else: 
        if dia == 3:
            print("Es Miercoles")
        else: 
            if dia == 4:
               print("Es Jueves")
            else: 
                if dia == 5:
                   print("Es Viernes")
                else: 
                    if dia == 6:
                        print("Es Sabado")
                    else: 
                        if dia == 7:
                            print("Es Domingo")


if dia == 1: 
    print("Es lunes") 
elif dia == 2 :
     print("Es Martes")   
elif dia == 3 :
     print("Es Miercoles")      
elif dia == 4 :
     print("Es Jueves")
elif dia == 5 :
     print("Es Viernes")
elif dia == 6 :
     print("Es Sabado")
elif dia == 7 :
     print("Es Domingo")  
"""
print("\n ########## EJEMPLO 5 #############") 

edad_minima = 18 
edad_maxima = 65 
edad_oficial = int(input("tienes edad de trabajar?, digite su edad!!"))

if edad_oficial >= 18 and edad_oficial <=65: 
    print("Esta en edad de trabajar !!")
else: 
    print("NO esta en edad de trabajr !!")  

print("\n ########## EJEMPLO 6 #############") 

pais= "Alemania"

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} es una pais de habla hispana !!")
else : 
    print(f"{pais} NO es un pais de habla hispana !!")    


print("\n ########## EJEMPLO 7 #############") 

pais = "Colombia"

if not(pais == "Mexico" or pais == "España" or pais == "Colombia"):

    print(f"{pais} NO es un pais de habla hispana!!")
else : 
    print(f"{pais} Si es un pais de habla hispana !!") 

print("\n ########## EJEMPLO 8 #############")  
pais = "España"
 
if  pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} NO es un pais de habla hispana !!")
else: 
    print (f"{pais} SI es un pais de habla hispana !!")
    





