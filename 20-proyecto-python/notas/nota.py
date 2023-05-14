#importamos  la conexion 
import usuarios.conexion as conexion
connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

# aqui creamos nuestro objeto de notas 
class Nota:
    #propiedades que tengo en la entidad 
    def __init__(self, usuario_id, titulo, descripcion):
        #se le dan los valores
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion


    #para guardar en la BD
    def guardar(self):
        sql= "INSERT INTO notas VALUES(null, %s, %s, %s, NOW())"
        nota = (self.usuario_id, self.titulo, self.descripcion)

        cursor.execute(sql,nota)
        database.commit()
        return[cursor.rowcount, self]   
# creacion del metodo listar para mostrar las notas
    def listar (self):
        sql = f"SELECT * FROM notas WHERE usuario_id = {self.usuario_id}"
        #ejecutamos la consulta
        cursor.execute(sql)
        result = cursor.fetchall()

        return result
        
        #creamos el metodo de eliminar nota 
        def eliminar (self):
            #borra las notas del usuario que esta logueado y cuando el titulo usando comodines LIKE
            #donde '%{titulo}%' quiere decir que lo contenga el titulo 
            sql=f"DELETE FROM notas WHERE usuario_id = {self.usuario_id} AND titulo LIKE'%{self.titulo}%'"
            cursor.execute(sql)
            database.commit()
            return[cursor.rowcount, self]