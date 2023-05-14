"""
Diccionario es un tipo que almacena un conjunto de datos.
en forma clave > valor  
Es parecedio a un array asociativo a un conjunto o un objeto json.
"""
persona = {
    "nombre": "carlos",
    "apellido": "sanchez",
    "email": "carlossanchez@gmail.com"
}

print(persona)
print(persona["email"])

print("########## Lista con diccionario ###########")
contactos = [
   {
    "nombre": "carlos",
    "apellido": "sanchez",
    "email": "carlossanchez@gmail.com"
   },
   {
    "nombre": "juan",
    "apellido": "Perez",
    "email": "juanperez@gmail.com"

   },
   {
    "nombre": "pedro ",
    "apellido": "gomez",
    "email": "pedrogomez@gmail.com"
   }

]

print(contactos)
print(contactos[0]['nombre'])
contactos[0]['nombre'] = "sandra"
print(contactos)
print(contactos[0]['nombre'])

print("\n lista de contactos:")
for contactos in contactos:
    print("---------------------------------------")
    print(f"Nombre del contacto: {contactos['nombre']}")
    print(f"Email del contacto {contactos['email']}")
    print("---------------------------------------")





d1 = {
"Nombre": "Sara",
"Edad": 27,
"Documento": 1003882                  # En el siguiente ejemplo tenemos tres keys que son el nombre, la edad y el documento.
}
print(d1)
#{'Nombre': 'Sara', 'Edad': 27, 'Documento': 1003882}



d2 = dict([
('Nombre', 'Sara'),
('Edad', 27),                          #Otra forma equivalente de crear un diccionario en Python es usando dict() e introduciendo los pares key: value entre paréntesis.
('Documento', 1003882),
])
print(d2)
#{'Nombre': 'Sara', 'Edad': '27', 'Documento': '1003882'}


d3 = dict(Nombre='Sara',
Edad=27,
Documento=1003882)                     #También es posible usar el constructor dict() para crear un diccionario.
print(d3)
#{'Nombre': 'Sara', 'Edad': 27, 'Documento': 1003882}


print(d1['Nombre']) #Sara
print(d1.get('Nombre')) #Sara           #Se puede acceder a sus elementos con [] o también con la función get()


d1['Nombre'] = "Laura"
print(d1)                              #Para modificar un elemento basta con usar [] con el nombre del key y asignar el valor que queremos.
#{'Nombre': Laura', 'Edad': 27, 'Documento': 1003882}


d1['Direccion'] = "Calle 123"
print(d1)                               #Si el key al que accedemos no existe, se añade automáticamente.
#{'Nombre': 'Laura', 'Edad': 27, 'Documento': 1003882, 'Direccion': 'Calle 123'}


# Imprime los key del diccionario
for x in d1: 
   print(x)                            #Los diccionarios se pueden iterar de manera muy similar a las listas u otras estructuras de datos. Para imprimir los key.   
#Nombre
#Edad
#Documento
#Direccion


# Impre los value del diccionario
for x in d1: 
   print(d1[x])
#Laura
#27                                   #Se puede imprimir también solo el value .
#1003882
#Calle 123


# Imprime los key y value del diccionario
for x, y in d1.items():
    print(x, y)
#Nombre Laura                         #O si queremos imprimir el key y el value a la vez.   
#Edad 27
#Documento 1003882
#Direccion Calle 123



anidado1 = {"a": 1, "b": 2}
anidado2 = {"a": 1, "b": 2}
d = {
"anidado1" : anidado1,               #Los diccionarios en Python pueden contener uno dentro de otro. Podemos ver como los valores anidados uno y dos del 
 "anidado2" : anidado2                                     #diccionario d contienen a su vez otro diccionario.
}
print(d)
#{'anidado1': {'a': 1, 'b': 2}, 'anidado2': {'a': 1, 'b': 2}}



d = {'a': 1, 'b': 2}
d.clear()                            #El método clear() elimina todo el contenido del diccionario.
print(d) #{}



d = {'a': 1, 'b': 2}
print(d.get('a')) #1                 #El método get() nos permite consultar el value para un key determinado. El segundo parámetro es opcional, y en el
                                     #caso de proporcionarlo es el valor a devolver si no se encuentra la key .
print(d.get('z', 'No encontrado')) #No encontrado



d = {'a': 1, 'b': 2}
it = d.items()
print(it) #dict_items([('a', 1), ('b', 2)])   # El método items() devuelve una lista con los keys y values del diccionario. Si se convierte en list se puede
print(list(it)) #[('a', 1), ('b', 2)]         # indexar como si de una lista normal se tratase, siendo los primeros elementos las key y los segundos los value .
print(list(it)[0][0]) #a



d = {'a': 1, 'b': 2}
k = d.keys()
print(k) #dict_keys(['a', 'b'])             #El método keys() devuelve una lista con todas las keys del diccionario. 
print(list(k)) #['a', 'b']



d = {'a': 1, 'b': 2}
print(list(d.values())) #[1, 2]             #El método values() devuelve una lista con todos los values o valores del diccionario.


d = {'a': 1, 'b': 2}
d.pop('a')                                  #El método pop() busca y elimina la key que se pasa como parámetro y devuelve su valor asociado. Daría un error si se
print(d) #{'b': 2}                          # intenta eliminar una key que no existe.



d = {'a': 1, 'b': 2}
d.pop('c', -1)                              #También se puede pasar un segundo parámetro que es el valor a devolver si la key no se ha encontrado. En este caso si
print(d) #{'a': 1, 'b': 2}                   no se encuentra no habría error.



d = {'a': 1, 'b': 2}
d.popitem()
print(d)                                    #El método popitem() elimina de manera aleatoria un elemento del diccionario.
#{'a': 1}


d1 = {'a': 1, 'b': 2}
d2 = {'a': 0, 'd': 400}
d1.update(d2)                               #El método update() se llama sobre un diccionario y tiene como entrada otro diccionario. Los value son actualizados y
print(d1)                                   #si alguna key del nuevo diccionario no está, es añadida.
#{'a': 0, 'b': 2, 'd': 400}
                       






















