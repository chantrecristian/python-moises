s = set([5, 4, 6, 8, 8, 1])
print(s) #{1, 4, 5, 6, 8}               Se puede ver como a pesar de pasar elementos duplicados como dos 8 y en un orden determinado, al imprimirel
print(type(s)) #<class 'set'>            #set no conserva ese orden y los duplicados se han eliminado.



s = {5, 4, 6, 8, 8, 1}
print(s) #{1, 4, 5, 6, 8}              #Se puede hacer lo mismo haciendo uso de {} y sin usar la palabra set() como se muestra a continuación.
print(type(s)) #<class 'set'>


s = set([5, 6, 7, 8])                  # A diferencia de las listas, en los set no podemos modificar un elemento a través de su índice. Si lo intentamos, tendremos un TypeError   
#s[0] = 3 #Error! TypeError



lista = ["Perú", "Argentina"]                                #  Los elementos de un set deben ser inmutables, por lo que un elemento de un set no puede ser ni un diccionario ni una lista. 
#s = set(["México", "España", lista]) #Error! TypeError         Si lo intentamos tendremos un TypeError


s = set([5, 6, 7, 8])
for ss in s:                            # Los sets se pueden iterar de la misma forma que las listas.
    print(ss) #8, 5, 6, 7


s = set([1, 2, 2, 3, 4])                #Con la función len() podemos saber la longitud total del set . Como ya hemos indicado, los duplicados son eliminados.
print(len(s)) #4


s = set(["Guitarra", "Bajo"])
print("Guitarra" in s) #True            #También podemos saber si un elemento está presente en un set con el operador in . Se el valor existe en el set, se devolverá True .



s1 = set([1, 2, 3])
s2 = set([3, 4, 5])                     # Los sets tienen además diferentes funcionalidades, que se pueden aplicar en forma de operador o de método. Por
print(s1 | s2) #{1, 2, 3, 4, 5}         # ejemplo, el operador | nos permite realizar la unión de dos sets, lo que equivale a juntarlos. El equivalente es el
                                         #método union() que vemos a continuación.
 


l = set([1, 2])
l.add(3)                           # El método add() permite añadir un elemento al set .
print(l) #{1, 2, 3}


s = set([1, 2])
s.remove(2)                        #El método remove() elimina el elemento que se pasa como parámetro. Si no se encuentra, se lanza la excepción KeyError .
print(s) #{1}                       


s = set([1, 2])
s.discard(3)                       #El método discard() es muy parecido al remove() , borra el elemento que se pasa como parámetro, y si no se encuentra no hace nada.
print(s) #{1, 2}


s = set([1, 2])
s.pop()                            #El método pop() elimina un elemento aleatorio del set .
print(s) #{2}


s = set([1, 2])
s.clear()                          #El método clear() elimina todos los elementos de set .   
print(s) #set()


s1 = {1, 2, 3} 
s2 = {3, 4, 5}                          #Podemos calcular la unión entre dos sets usando el método union() . Esta operación representa la “mezcla” de ambos
print(s1.union(s2)) #{1, 2, 3, 4, 5}    # sets. Nótese que el método puede ser llamado con más parámetros de entrada, y su resultado será la unión de todos los sets.



s1 = {1, 2, 3}
s2 = {3, 4, 5}                          #También podemos calcular la intersección entre dos o más set. Su resultado serán aquellos elementos que pertenecen a ambos sets.
print(s1.intersection(s2)) #{3}



