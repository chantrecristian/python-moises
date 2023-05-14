class Acciones:
    def crear (self, usuario): #le pasamos el usuario para saber quien crea la nota
        print (f"\nok {usuario[1]}!! Vamos a crear una nueva nota...")

        titulo = input("Introduce el titulo de la nota: ")  
        descripcion = input("Digite el contenido de su nota..")
        

        #cuando ya se llamo al modelo y creo el objeto nota
        nota = modelo.Nota(usuario[0],titulo, descripcion)
        guardar = nota.guardar()# invocar el metodo guardar para que guarde en la BD

        if guardar[0] >= 1:
            print(f"\nPerfecto has guardado la nota: {nota.titulo}")
        else:
            print(f"\nNo se guardo la nota: {usuario[1]}")
            
            #creamos el objeto y sacamos todo el listado
            nota = modelo.Nota(usuario[0])
            #creamos la var notas donde se guardan todas las notas que tenga el usuario en la BD
            notas = nota.listar()

            #recorrer todo el array de notas 
            for nota in notas:
                print("************************************") 
                print(nota[2])
                print(nota[3])

            #creamos el metodo borrar 
            def borrar (self,usuario):
                print(f"\nOK {usuario[1]} Vamos a borrar notas...")
                #se digita por teclado el titulo de la nota que el usuario quiere borrar
                titulo = input("Digite el titulo de la nota")    
                
                nota = modelo.Nota(usuario[0], titulo)
                eliminar = nota.eliminar()

                #comprobamos
                if eliminar[0] >=1:
                    print(f"Se ha borrado la nota: {nota.titulo}") 
                else:
                    print(f"No se ha borrado la nota, prueba luego..")    


            #Ahora para probar vamos a acciones.py e importamos el modelo de usuario
            #le creamos un alias en este caso as modelo
            import usuarios.usuario as modelo

       
