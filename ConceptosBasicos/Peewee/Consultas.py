import mysql.connector

# Conexión a la base de datos Hospital
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="Hospital"
)

# Crear un cursor
cursor = db_connection.cursor()


# Función para mostrar todos los datos de una tabla
def show_data(table_name):
    query = f"SELECT * FROM {table_name};"
    cursor.execute(query)
    results = cursor.fetchall()

    print(f"Datos de la tabla {table_name}:")
    for row in results:
        print(row)


# Función para insertar un nuevo registro en la tabla
def insert_data(table_name, **kwargs):
    columns = ', '.join(kwargs.keys())
    values = ', '.join(['%s'] * len(kwargs))

    query = f"INSERT INTO {table_name} ({columns}) VALUES ({values});"
    cursor.execute(query, tuple(kwargs.values()))
    db_connection.commit()

    print(" ")
    print(f"Datos insertados correctamente en la tabla {table_name}")


# Función para eliminar un registro de la tabla
def delete_data(table_name, column, value):
    query = f"DELETE FROM {table_name} WHERE {column} = %s;"
    cursor.execute(query, (value,))
    db_connection.commit()

    print(" ")
    print(f"Registro con {column} = {value} eliminado de la tabla {table_name}")


# Programa principal
if __name__ == "__main__":
    # Mostrar datos de la tabla HOSPITAL
    show_data('HOSPITAL')

    # Insertar un nuevo hospital
    insert_data('HOSPITAL', HOSPITAL_COD=50, NOMBRE='nuevo hospital', DIRECCION='calle nueva', TELEFONO='555-1234',
                NUM_CAMA=100)

    # Mostrar datos de la tabla HOSPITAL después de la inserción
    show_data('HOSPITAL')

    # Eliminar un hospital por su HOSPITAL_COD
    delete_data('HOSPITAL', 'HOSPITAL_COD', 50)

    # Mostrar los datos de la tabla HOSPITAL después de la eliminación
    show_data('HOSPITAL')

    # Cerrar la conexión
    cursor.close()
    db_connection.close()
