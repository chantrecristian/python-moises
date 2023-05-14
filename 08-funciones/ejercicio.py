print("------- 1 ------")

def validar(email):
    simboloBuscado="@"
    emailValido=False
    for c in email:
        if c==simboloBuscado:
            return True
    return False


direccion=input("Tu email: ")
if validar(direccion):
    print("Bienvenido")
else:
    print("Ingreso denegado")



print("------- 2 ------")

def frecuencia(numero,digito):
   cantidad=0
   while numero!=0:
       ultDigito=numero%10
       if ultDigito==digito:
           cantidad+=1
       numero=numero//10
   return cantidad

 
num=int(input("Número: "))
un_digito=int(input("Dígito: "))

print("------- 3 ------")



def factorial(numero):
   f=1
   if numero!=0:
       for i in range(1,numero+1):
           f=f*i
   return f

 
cantidad=0
num=int(input("Número (-1 para cortar): "))
while num!=-1:
    print("Factorial:", factorial(num))
    cantidad+=1
    num=int(input("Número (-1 para cortar): "))
print("Se leyeron",cantidad,"números")