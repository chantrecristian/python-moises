print ("######## ejercicio  1 #########")

lista1 = ["filosofia", "matematicas", "fisica", "quimica", "historia", "español"]
lista2 = ["GRADO 5A"]
for l1, l2 in zip(lista1, lista2):
    print(lista1, l2)
    

print ("######## ejercicio  2 #########")

lista1 = ["filosofia", "matematicas", "fisica", "quimica", "historia", "español"]
lista2 = ["GRADO 5A"]
for l1, l2 in zip(lista1, lista2):
    print(f"yo estudio:{lista1+lista2}")


print ("######## ejercicio 3 #########")   

lista1 = ["filosofia", "matematicas", "fisica", "quimica", "español"]
lista2 = [5.0, 4.5, 4.4, 3.0, 5.0]
for l1, l2 in zip(lista1, lista2):
   print(f"sacaste en:{l1,l2}")

print ("######## ejercicio 4 #########") 

lista = [1,2,3,4,5,6,7,8,9,10]
lista.reverse()
print(lista)


print ("######## ejercicio 5 #########")

def leer_frase():
    global txt
    txt=(input("Ingrese una texto!!:"))
def contar_letras():
    conta=0
    for i in txt :
        if(i.isalpha()):
            conta+=1
    print("la cantidad de letras:",conta)

leer_frase()
contar_letras()


