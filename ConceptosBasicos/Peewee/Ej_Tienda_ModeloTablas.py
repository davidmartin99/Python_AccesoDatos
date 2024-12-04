from peewee import (
    Model,
    MySQLDatabase,
    IntegerField,
    SmallIntegerField,
    CharField,
    FloatField,
    DateField,
    ForeignKeyField, JOIN
)
from datetime import date
from peewee import IntegrityError
# Conexión a la base de datos MySQL
db = MySQLDatabase(
    'tienda2',
    user='root',
    password='1234',
    host='localhost',
    port=3306
)

# Clase base para todos los modelos
class BaseModel(Model):
    class Meta:
        database = db

# Tabla: Clientes
class Cliente(BaseModel):
    codigo_cli = SmallIntegerField(primary_key=True)
    nombre = CharField(max_length=20)
    localidad = CharField(max_length=15)
    tlf = CharField(max_length=10, null=True)

# Tabla: Proveedores
class Proveedor(BaseModel):
    codigo_prov = SmallIntegerField(primary_key=True)
    nombre = CharField(max_length=20)
    localidad = CharField(max_length=15)
    fecha_alta = DateField(null=True)
    comision = FloatField()

# Tabla: Artículos
class Articulo(BaseModel):
    codarticulo = SmallIntegerField(primary_key=True)
    denominacion = CharField(max_length=25)
    precio = FloatField()
    stock = SmallIntegerField()
    zona = CharField(max_length=10, null=True)
    codigo_prov = ForeignKeyField(Proveedor, backref='articulos', on_delete='CASCADE', field='codigo_prov')

# Tabla: Compras
class Compra(BaseModel):
    numcompra = SmallIntegerField(primary_key=True)
    codigo_cli = ForeignKeyField(Cliente, backref='compras', on_delete='CASCADE', field='codigo_cli')
    fechacompra = DateField()

# Tabla: DetalleCompras
class DetalleCompra(BaseModel):
    numcompra = ForeignKeyField(Compra, backref='detalles', on_delete='CASCADE', field='numcompra')
    codarticulo = ForeignKeyField(Articulo, backref='detalles', on_delete='CASCADE', field='codarticulo')
    unidades = SmallIntegerField()

    class Meta:
        primary_key = False  # No se usa una clave primaria automática
        indexes = (
            (('numcompra', 'codarticulo'), True),  # Clave primaria compuesta
        )

# Crear las tablas en la base de datos
def crear_tablas():
    with db:
        db.create_tables([Cliente, Proveedor, Articulo, Compra, DetalleCompra])
def insertar_datos():
    try:
        # Insertar 3 clientes
        Cliente.insert_many([
            {'codigo_cli': 1, 'nombre': 'Juan Perez', 'localidad': 'Madrid', 'tlf': '600123456'},
            {'codigo_cli': 2, 'nombre': 'Ana López', 'localidad': 'Barcelona', 'tlf': '601987654'},
            {'codigo_cli': 3, 'nombre': 'Carlos Ruiz', 'localidad': 'Valencia', 'tlf': '602345678'}
        ]).execute()

        # Insertar 3 proveedores
        Proveedor.insert_many([
            {'codigo_prov': 1, 'nombre': 'Proveedor A', 'localidad': 'Sevilla', 'fecha_alta': date(2021, 5, 1), 'comision': 5.5},
            {'codigo_prov': 2, 'nombre': 'Proveedor B', 'localidad': 'Bilbao', 'fecha_alta': date(2022, 3, 15), 'comision': 4.0},
            {'codigo_prov': 3, 'nombre': 'Proveedor C', 'localidad': 'Granada', 'fecha_alta': date(2023, 7, 10), 'comision': 6.0}
        ]).execute()

        # Insertar 3 artículos
        Articulo.insert_many([
            {'codarticulo': 101, 'denominacion': 'Laptop', 'precio': 799.99, 'stock': 10, 'zona': 'A1', 'codigo_prov': 1},
            {'codarticulo': 102, 'denominacion': 'Mouse', 'precio': 19.99, 'stock': 100, 'zona': 'B1', 'codigo_prov': 2},
            {'codarticulo': 103, 'denominacion': 'Teclado', 'precio': 49.99, 'stock': 50, 'zona': 'C1', 'codigo_prov': 3}
        ]).execute()

        # Insertar 3 compras
        Compra.insert_many([
            {'numcompra': 1001, 'codigo_cli': 1, 'fechacompra': date(2024, 11, 15)},
            {'numcompra': 1002, 'codigo_cli': 2, 'fechacompra': date(2024, 11, 16)},
            {'numcompra': 1003, 'codigo_cli': 3, 'fechacompra': date(2024, 11, 17)}
        ]).execute()

        # Insertar 3 detalles de compra
        DetalleCompra.insert_many([
            {'numcompra': 1001, 'codarticulo': 101, 'unidades': 2},
            {'numcompra': 1002, 'codarticulo': 102, 'unidades': 5},
            {'numcompra': 1003, 'codarticulo': 103, 'unidades': 3}
        ]).execute()

        print("Datos insertados correctamente.")

    except IntegrityError as e:
        print("Error al insertar datos:", e)

    def consultas():
        query = Cliente.select().where(Cliente.codigo_cli == 1)



# Ejecutar la creación de las tablas
if __name__ == "__main__":
    crear_tablas()
    print("Se crearin las tabli perfecti")
    insertar_datos()
    print("Se insertaron correctamente los datos")



# 1. Obtener los datos de los clientes y sus compras
clientes_con_compras = (
    Cliente
    .select(
        Cliente.codigo_cli,
        Cliente.nombre,
        Cliente.localidad,
        Compra.numcompra,
        Compra.fechacompra
    )
    .join(Compra, JOIN.LEFT_OUTER, on=(Cliente.codigo_cli == Compra.codigo_cli))
)
for cliente in clientes_con_compras:
    print(f"Código Cliente: {cliente.codigo_cli}, Nombre: {cliente.nombre}, Localidad: {cliente.localidad}")
    for compra in cliente.compras:
        print(f"  Número Compra: {compra.numcompra}, Fecha Compra: {compra.fechacompra}")
