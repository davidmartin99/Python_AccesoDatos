from datetime import date
import mysql.connector as bd

# Establecemos la conexión con la base de datos
bd_conexion = bd.connect(host='localhost', port='3306',
                         user='root', password='1234', database='hospital')

# Creamos un cursor para ejecutar las consultas
cursor = bd_conexion.cursor()

# Consulta para insertar un nuevo empleado en la tabla EMP
ConsultaAlta = """
    INSERT INTO emp 
    (emp_no, apellido, oficio, dir, fecha_alt, salario, comision, dept_no)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""

# Datos del nuevo empleado a insertar
datosEmpleados = (1111, 'Benito', 'Programador', 7566, date(1976, 6, 4), 100000, 100, 20)

# Ejecutamos la consulta para insertar los datos
cursor.execute(ConsultaAlta, datosEmpleados)

# Confirmamos los cambios en la base de datos
bd_conexion.commit()

# Ejemplo de inserción en la tabla ENFERMO
ConsultaEnfermo = """
    INSERT INTO enfermo 
    (inscripcion, apellido, direccion, fecha_nac, sexo, nss)
    VALUES (%s, %s, %s, %s, %s, %s)
"""

# Datos del nuevo enfermo a insertar
datosEnfermo = (12345, 'Lopez', 'Calle Falsa 123', date(1985, 2, 25), 'M', 987654321)

# Ejecutamos la consulta para insertar los datos del enfermo
cursor.execute(ConsultaEnfermo, datosEnfermo)

# Confirmamos los cambios en la base de datos
bd_conexion.commit()

# Cerramos el cursor y la conexión
cursor.close()
bd_conexion.close()

print("Datos insertados correctamente.")
