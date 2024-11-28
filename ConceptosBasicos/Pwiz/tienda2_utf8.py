from peewee import *

database = MySQLDatabase('tienda2', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'user': 'root', 'password': '1234'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Proveedores(BaseModel):
    codigo_prov = AutoField()
    comision = FloatField(null=True)
    fecha_alta = DateField(null=True)
    localidad = CharField(null=True)
    nombre = CharField(null=True)

    class Meta:
        table_name = 'proveedores'

class Articulos(BaseModel):
    codarticulo = AutoField()
    codigo_prov = ForeignKeyField(column_name='codigo_prov', field='codigo_prov', model=Proveedores, null=True)
    denominacion = CharField(null=True)
    precio = FloatField(null=True)
    stock = IntegerField(null=True)
    zona = CharField(null=True)

    class Meta:
        table_name = 'articulos'

class Clientes(BaseModel):
    codigo_cli = AutoField()
    localidad = CharField(null=True)
    nombre = CharField(null=True)
    tlf = CharField(null=True)

    class Meta:
        table_name = 'clientes'

class Compras(BaseModel):
    codigo_cli = ForeignKeyField(column_name='codigo_cli', field='codigo_cli', model=Clientes, null=True)
    fechacompra = DateField(null=True)
    numcompra = AutoField()

    class Meta:
        table_name = 'compras'

class Detallecompras(BaseModel):
    codarticulo = AutoField()
    numcompra = ForeignKeyField(column_name='numcompra', field='numcompra', model=Compras, null=True)
    unidades = IntegerField(null=True)

    class Meta:
        table_name = 'detallecompras'


###################################################################
### EJERCICIO ###
#################

# 1. Obtener los datos de los clientes y sus compras
clientes_con_compras = (
    Clientes
    .select(
        Clientes.codigo_cli,
        Clientes.nombre,
        Clientes.localidad,
        Compras.numcompra,
        Compras.fechacompra
    )
    .join(Compras, JOIN.LEFT_OUTER, on=(Clientes.codigo_cli == Compras.codigo_cli))
)
for cliente in clientes_con_compras:
    print(f"Código Cliente: {cliente.codigo_cli}, Nombre: {cliente.nombre}, Localidad: {cliente.localidad}")
    for compra in cliente.compras:
        print(f"  Número Compra: {compra.numcompra}, Fecha Compra: {compra.fechacompra}")

# 2. Obtener lo mismo que en la pregunta 1 visualizando código de cliente,
# nombre, localidad, número de compra y fecha de compra. Si el cliente no
# tiene compras se visualizará 0 en el número de compra.


# 3. Obtener por cada cliente el detalle de compras que ha realizado,
# visualizando el código de cliente, nombre, localidad, número de compra,
# código del artículo, unidades compradas, precio de artículo e importe
# (precio del artículo por las unidades compradas)


# 4. Obtener el total de compra de cada cliente. Visualizar el código de
# cliente, nombre, localidad, número de compra e importe de la compra.


# 5. Obtener el total de las compras de cada cliente y el número de compras
# realizadas. Visualizar el código del cliente, nombre, localidad, teléfono,
# número de compras que ha realizado y el importe total de las compras.


# 6. Obtener para cada artículo las unidades compradas por los clientes, el
# importe y el nombre de su proveedor. Se deben visualizar los artículos sin
# compras. Visualizar código de artículo, denominación, stock, precio,
# unidades compradas, importe de las compras y nombre del proveedor.


# 7. Obtener para cada proveedor los artículos que suministra. Visualizar
# código de proveedor, nombre, código del artículo y denominación del
# artículo.


# 8. Visualizar por cada proveedor el número de artículos que suministra.


# 9. Visualizar el código de cliente, nombre y localidad de los clientes de
# Talavera que compraron artículos de la zona Centro.


# 10. Visualizar código, nombre y localidad de los proveedores que
# suministran artículos de la zona centro.
