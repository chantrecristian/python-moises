#importat el modulo SQLite
import sqlite3
#Conexion
#creamos una variable y utilizamos  el metodo connect
conexion = sqlite3.connect('pruebas.db') #creamos el fichero
#creacion de tablas
#cerramos la conecion para que se guarden los datos en el fichero
#creacion de cursor
cursor = conexion.cursor()
#ahora si se crea la consulta para creacion de tabla
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
"id INTEGER PRIMARY KEY AUTOINCREMENT,"+
"titulo VARCHAR(255), "+
"descripcion TEXT,"+
"precio int(255)"+
")")

#para guardar cambios 
conexion.commit()
"""
#insertar datos
cursor.execute("INSERT INTO productos VALUES (null, 'Primer producto','Descripcion de mi producto', 1200)")
#para guardar cambios
conexion.commit()
"""
#borrar resgistros de una tabla
cursor.execute("DELETE FROM productos")
conexion.commit()
#Insertar muchos resgistros a la vez
productos = [
    ("Portatil","Marca Lenovo", 1200000),
    ("Portatil","Marca Asus", 150000),
    ("Telefono","Samnsung", 2200000),
    ("Televisor","Marca SONY", 900000),
    ("Mouse","Marca HP", 120000),
]
cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)
conexion.commit()
#listar datos
#Actualizacion UPDATE
cursor.execute("UPDATE productos SET precio=100000 WHERE precio=120000")
conexion.commit()

cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()

#"listar datos con condicion WHERE
cursor.execute("SELECT * FROM productos WHERE precio <= 1000000")
productos = cursor.fetchall()
#print(productos)
#como ver los productos uno a uno 
for producto in productos:
    #print(producto)#todos los productos 
    print("Titulo:", producto[1])#los productos uno a uno 
    print("Descripcion:", producto[2])
    print("Precio:", producto[3])
    print("\n")
#sacar el primer registro de producto
cursor.execute("SELECT titulo FROM productos")
producto = cursor.fetchone()
print(producto)
 #cerramos la conexion para que se guarden los dats en el fichero
conexion.close()
