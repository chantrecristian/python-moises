#conexion a la BD
import datetime # creacion de la fecha del sistema
import hashlib #Modulo para cifrar contraseñas
import usuarios.conexion as conexion #importamos y le creamos un alias
#creamos var y llamamos al metodo conector 
connect = conexion.conectar ()
#creamos una variable database con un indice [0] que es donde tengo la BD
# que lo obtengo de connect
database = connect[0]
#creamos una variable cursor con un indice {1} que es donde tengo el cursor
cursor = connect[1]

class Usuario:
    #definimos el construcctor con sus propiedades 
    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre 
        self.apellidos = apellidos
        self.email = email
        self.password = password

        #creacion del metodo registrar 
    def registrar (self):
        fecha = datetime.datetime.now()


        #Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))
        # los %s sirvan para sustituir los datos que esten en medio de una tupla
        sql = "INSERT INTO usuarios (id, nombre, apellidos, email, password, fecha) VALUES (null, %s,%s,%s,%s,%s)"
        #creacion de tupla
        Usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha)
        try:
           #Ejecutar la consulta con la var sql que tiene la consulta y la tupla
           cursor.execute(sql,Usuario)
           database.commit() #guardamos en BD
           result = [cursor.rowcount, self] #return cambia por result
           #return para devolver algun tipo de dato en estre caso devolvernos una lista 
           #cantidad de registros que se han modificado con rowconunt y que devuelve el 
           #propio objeto con los datos que tenga self
        except:
            result = [0,self]  
        return result
        


    def identificar(self):
        #creamos la var y la consulta para comprobar si existe el usuario 
        sql = " SELECT * FROM usuarios WHERE email = %s AND password = %s"
        # se debe cifrar la contraseña para realizar la comparacion
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))
        #creamos un var usuario donde estan los daos que vamos a pasar a la consulta sql %s
        Usuario = (self.email, cifrado.hexdigest())
        #Ejecutamos la consulta
        cursor.execute(sql, Usuario)
        #guardamos lo que nos de la consulta en una var result con fetchone para un solo usuario
        result = cursor.fetchone()
        #Devolvemos con el return el resultado result
        return result 
