import mysql.connector #libreria mysql

def conectar():
    #configuracion de la conexion al servidor y BD
    database = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "proyecto_python",
        prot = 3306
    )


    #creamos   el cursor para realizar las consultas
    cursor = database.cursor(Buffered=True)#para hacer diferentes consultas usando el mismo cursor 
    return[database, cursor]