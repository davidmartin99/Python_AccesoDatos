from peewee import MySQLDatabase

# Cambia estas credenciales según tu configuración
db = MySQLDatabase(
    'tienda2',  # Nombre de la base de datos
    user='david',  # Usuario
    password='1234',  # Contraseña
    host='localhost',  # Servidor
    port=3306  # Puerto de MySQL
)

try:
    db.connect()
    print("Conexión exitosa.")
except Exception as e:
    print("Error al conectar:", e)
finally:
    db.close()
