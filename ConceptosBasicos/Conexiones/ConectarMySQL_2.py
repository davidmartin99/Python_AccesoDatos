
import mysql.connector as bd

bd_conexion = bd.connect(host='localhost', port='3306',
                                   user='root', password='', database='prueba1')

# Devuelve FALSO si hay un error en la conexión
cursor = bd_conexion.cursor()
try:
    cursor.execute("SELECT Nombre FROM alumno")

    # Itera sobre los resultados y muestra el nombre
    for (Nombre,) in cursor:
        print("Nombre Alumno: " + Nombre) #eee

except bd.Error as error:
    print("Error:", error)

finally:
    # Cierra la conexión
    cursor.close()
    bd_conexion.close()