import cx_Oracle

# Configuración de la conexión
host = "localhost"                # Dirección o IP del servidor Oracle
port = "1521"               # Puerto de la base de datos Oracle (por lo general, 1521)
service_name = "xe"     # Nombre del servicio o SID de la base de datos
username = "SYSTEM"          # Nombre de usuario de la base de datos
password = "1234"       # Contraseña de la base de datos

# Cadena de conexión
dsn = cx_Oracle.makedsn(host, port, service_name=service_name)

# Conectar a la base de datos
try:
    connection = cx_Oracle.connect(user=username, password=password, dsn=dsn)
    print("Conexión exitosa a la base de datos Oracle")

    # Crear un cursor para ejecutar consultas
    cursor = connection.cursor()

    # Verificar las tablas disponibles en el esquema del usuario
    cursor.execute("SELECT table_name FROM all_tables WHERE owner = UPPER(:username)", [username])
    tables = cursor.fetchall()
    print("Tablas disponibles en el esquema:")
    for table in tables:
        print(table[0])  # Muestra los nombres de las tablas

    # Verificar si la tabla 'dept' existe y tiene datos
    cursor.execute("SELECT COUNT(*) FROM dept")
    count = cursor.fetchone()
    print(f"Total de filas en 'dept': {count[0]}")

    if count[0] > 0:  # Si hay filas en la tabla
        # Ejecutar la consulta para obtener los resultados
        cursor.execute("SELECT * FROM dept")
        rows = cursor.fetchall()

        print("\nContenido de la tabla 'dept':")
        for row in rows:
            print(row)

except cx_Oracle.DatabaseError as e:
    print(f"Error en la conexión: {e}")

finally:
    # Cerrar la conexión
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()
        print("Conexión cerrada")