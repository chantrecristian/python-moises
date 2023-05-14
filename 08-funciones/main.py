"""
# funciones sin parametros o retorno de valores 
def dihola():
    print("hello")

dihola( ) #llamada la funcion, 'hello' se muestra en la consola 


# funciones de parametro 
def holaConNombre (name):
    print("hello" + name + "!")

holaConNombre("ada")   # llamada la funcion, "hello ada" se muestra en la consola 
#consola  con multiples parametros con una sentencia de retorno 

def multiplica (val1, val2): 
    return val1 * val2

multiplica(3,5)  # se muestra 15 en consola 

# esta es una funcion basica de suma 
def suma(a,  b=3):
 return a + b 
 
result = suma ( 1)
# result = 4

result = suma(b=2, a=2)
# result = 4

result = suma  (3, b=2)
# result  = 5 

result = suma( b=2, 3)
# lanzara sintaxError


s = suma
result = s( 1, 2)
# result = 3

print(multiplica (3)) #typeError: multiplica () utiliza exactamente 2 argumentos (0 proporcionados )
print( multiplica ('a', 5)) # 'aaaaa' ,ostrado en la consola 
print(multiplica ('a', 'b')) # typeError: python no puede multiplicar dos strings

def Mifuncion():
    print('this will print')
    print('so will this')

x = 7 
# la asginacion de x no es parte de la funcion ya que no esta identada

def duplica (num) :
    x = num * 2
    return x
print(x) # error - x no esta definida 
print(duplica ( 4)) #  muestra 8 


"""



