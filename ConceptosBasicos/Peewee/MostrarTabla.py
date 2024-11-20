import peewee

# Conexión a la base de datos MySQL
database = peewee.MySQLDatabase('hospital', user='root', password='1234', host='localhost', port=3306)

# Definición del modelo Dept
class Dept(peewee.Model):
    dept_no = peewee.IntegerField(primary_key=True)  # Campo INT como clave primaria
    dnombre = peewee.CharField(null=True)  # Campo VARCHAR(40) para el nombre del departamento
    loc = peewee.CharField(null=True)  # Campo VARCHAR(50) para la ubicación

    class Meta:
        database = database
        db_table = 'DEPT'  # Especificar el nombre de la tabla

# Función para mostrar los datos de la tabla 'DEPT'
class DepartmentViewer:
    @staticmethod
    def show_departments():
        database.connect()  # Conectar a la base de datos
        try:
            print("Datos de la tabla 'DEPT':\n")
            # Consultar todos los departamentos
            departments = Dept.select()
            for dept in departments:
                print(f"Dept No: {dept.dept_no}, Nombre: {dept.dnombre}, Ubicación: {dept.loc}")
        except peewee.DatabaseError as e:
            print(f"Error al consultar la base de datos: {e}")
        finally:
            database.close()  # Cerrar la conexión a la base de datos

# Ejecutar la función
if __name__ == '__main__':
    viewer = DepartmentViewer()
    viewer.show_departments()
