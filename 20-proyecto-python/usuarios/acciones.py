#Ahora para probar vamos a acciones.py e importamos el modelo de usuario
#le creamos un alias en este caso as modelo
import usuarios.usuario as modelo

#para poder usar las acciones de las notas se importa mi
# modulo de acciones.py de notas dentro del modulo de acciones.py
# en usuario porque se encadenan la llamada al otro metodo
import notas.acciones 

class Acciones:
    def registro(self):
        print("\nOK!! vamos a registrarte en el sistema...\n")
        #preguntas al usuario
        nombre = input("¿Cual es tu nombre?:")
        apellidos = input("Cuales son tus apellidos?:")
        email = input("Introduce tu email:")
        password = input("Introduce tu contraseña:")

        #para poder registrarlo se debe crear el objeto 
        usuario = modelo.Usuario(nombre, apellidos, email, password)
        #ahora se debe crear este objeto en la base de datos creamos la var registro
        registro = usuario.registrar()

        #Realizamos algunas comprobaciones
        #si registro en usuarios.py linea 37 return [cursor.rowconunt, self] es mayor o igual a 1
        #significa que si ha registrado el usuario
        if registro[0]>= 1:
            print(f"Perfecto{registro[1].nombre} te has registrado con el imail {registro[1].email}")
        else:
            print("--------------------No se ha registrado correctamente---------------")    
    def login (self):
        print("Vale!! Identificate como usuario en el Sistema...")
        try:
            #preguntas al usuario 
            email = input("Introduce tu email:")
            password = input("Introduce tu contraseña:")

            #creamos el objero usuario que pertenece a la clase Usuario 
            #solo pasamos email y password que son los que necesitamos, 
            #para la comprobacion del login, los demas vacios
            usuario = modelo.Usuario('','',email,password)
            login = usuario.identificar()
            #comprobamos que el login es correcto
            if email == login[3]:
                print(f"\nBienvenido{login[1]}, gracias por usar el sistema hoy {login[5]}")
        except Exception as e: #para capturar la excepcion en e
            print(type(e))
            print(type(e).__name__)
            print(f"\nLogin incorrecto!! Intentalo mas tarde")
            #creamo la funcion  proximas acciones 
            def proximasAcciones(self, usuario):
                print("""
                ******** Acciones Disponibles ********
                -Crear nora (crear)
                -Mostrar tus notas(mostrar)
                -Eliminar nota(eliminar)
                -Salir (salir)
                """)
                accion = input("\n¿Que quieres hacer?...")
                # Se crea una var que se llame hasEl (crear,mostrar...)
                hasEl = notas.acciones.Acciones()
                
                if accion == "crear":
                   hasEl.crear(usuario)
                   self.proximasAciones(usuario)
                elif accion =="mostrar":
                    hasEl.mostrar(usuario)
                    self.proximasAcciones(usuario)
                elif accion == "eliminar":
                    hasEl.borrar (usuario)
                    self.proximasAcciones(usuario)
                elif accion == "salir":
                     exit()
























