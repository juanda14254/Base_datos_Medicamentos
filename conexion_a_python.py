import psycopg2 as pg

'''string de conexion: puerto, base_de_datos, usuario, clave, host(direccion IP o nombre de la maquina: 127.0.0.1 o localhost)'''
conexion = pg.connect(user="Proyecto_datos_py", password="1234", database="Proyecto_datos", host="localhost", port="5432")
print("Conexion correcta!!!")

cursor = conexion.cursor()
'''para ejecutar operaciones de SQL'''

cursor.execute("SELECT VERSION();")
version = cursor.fetchone()
'''para guardar los datos de la sentencia ejecutada antes'''
print("Conectado a ", version)

cursor.execute("SELECT * FROM Importador")
rows=cursor.fetchall()
for row in rows:
    print(row)

cursor.execute("SELECT * FROM Medicamento WHERE IUM='1C1004471001100'")
rows=cursor.fetchall()
for row in rows:
    print(row)
   
conexion.close()
print("conexion finalizada")
