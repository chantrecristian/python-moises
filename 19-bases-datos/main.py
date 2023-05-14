import mysql.connector #importamos el conector

# Conexion a la base de datos
database = mysql.connector.connect(
    #creamos variables
    host = "localhost",
    user = "root",
    passwd = "",
    db = "adso_python"

)
# crear la base de datos desde editor de codigo 
cursor = database.cursor(buffered=True)
"""
cursor.execute("CREATE DATABASE IF NOT EXISTS adso_python")
#Comprobar si la BD existe
cursor.execute("SHOW DATABASES")
for bd in cursor:
    print(bd)
"""

#crear tablas 
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
id int(10) auto_increment not null,
marca varchar(40) not null,
modelo varchar(40) not null,
precio float(10,2) not null,
CONSTRAINT pk_vehiculo PRIMARY KEY (id)
)
""")
#mostrar la tabla 
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)
#insertat datos en la tabla 
carros = [
    ("Chevrolet","Corsa",20000000),
    ("Renault","4",4550000),
    ("Mazda","Cinco",7220000),
    ("Mercedes","Beanz",1009000)
]

#cursor.executemany("INSERT INTO vehiculos VALUES (null,%s,%s,%s)", carros)
database.commit()
#listar datos con condicion WHERE
cursor.execute("SELECT * FROM vehiculos")
result = cursor.fetchall()
for carro in result:
    print(carro[1], carro[3])
# aliminar datos 
cursor.execute("DELETE FROM vehiculos WHERE marca = 'Renault'")
database.commit()
#para saber cuantos registro borrados
print(cursor.rowcount, "borrados!!")

#Actualizacion de datos 
cursor.execute("UPDATE vehiculos SET modelo= 'Tres' WHERE marca = 'Mazda'")
database.commit()
print(cursor.rowcount, "Actualizados!!")

"Listar datos con condicion WHERE"
cursor.execute("SELECT * FROM vehiculos")
result = cursor.fetchall()
for carro in result:
    print(carro[1],carro[2],carro[3])

















