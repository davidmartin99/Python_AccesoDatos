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
    codigo_cli = ForeignKeyField(
        Clientes,
        backref='compras',  # Enables reverse relation
        column_name='codigo_cli',
        null=True
    )
    fechacompra = DateField(null=True)
    numcompra = AutoField()

    class Meta:
        table_name = 'compras'



class Detallecompras(BaseModel):
    codarticulo = ForeignKeyField(Articulos, backref='detallecompras', column_name='codarticulo', null=True)
    numcompra = ForeignKeyField(Compras, backref='lineas', column_name='numcompra', null=True)
    unidades = IntegerField(null=True)

    class Meta:
        table_name = 'detallecompras'



###################################################################
### EJERCICIO ###
#################

# 1. Obtener los datos de los clientes y sus compras
print("1_____________Datos clientes y sus compras: ")
clientes_con_compras = (
    Clientes
    .select(Clientes, Compras)
    .join(Compras, JOIN.LEFT_OUTER, on=(Clientes.codigo_cli == Compras.codigo_cli))
    .prefetch(Compras)
)

for cliente in clientes_con_compras:
    print(f"Código Cliente: {cliente.codigo_cli}, Nombre: {cliente.nombre}, Localidad: {cliente.localidad}")
    for compra in cliente.compras:  # This works if 'compras' is pre-fetched
        print(f"  Número Compra: {compra.numcompra}, Fecha Compra: {compra.fechacompra}")

print("\n")


# 2. Obtener lo mismo que en la pregunta 1 visualizando código de cliente,
# nombre, localidad, número de compra y fecha de compra. Si el cliente no
# tiene compras se visualizará 0 en el número de compra.
print("2_____________Detalle de compras: ")
clientes_con_compras = (
    Clientes
    .select(Clientes, Compras)
    .join(Compras, JOIN.LEFT_OUTER)
    .prefetch(Compras)
)

for cliente in clientes_con_compras:
    print(f"\nCódigo Cliente: {cliente.codigo_cli}")
    print(f"Nombre: {cliente.nombre}")
    print(f"Localidad: {cliente.localidad}")
    if cliente.compras:
        for compra in cliente.compras:
            print(f"  Número Compra: {compra.numcompra}, Fecha Compra: {compra.fechacompra}")
    else:
        print("  Número Compra: 0")
print("\n")


# 3. Obtener por cada cliente el detalle de compras que ha realizado,
# visualizando el código de cliente, nombre, localidad, número de compra,
# código del artículo, unidades compradas, precio de artículo e importe
# (precio del artículo por las unidades compradas)
print("3_____________Detalle de compras por cliente: ")

clientes_con_detalle = (
    Clientes
    .select(Clientes, Compras, Detallecompras, Articulos)
    .join(Compras, JOIN.LEFT_OUTER)
    .join(Detallecompras, JOIN.LEFT_OUTER, on=(Detallecompras.numcompra == Compras.numcompra))
    .join(Articulos, JOIN.LEFT_OUTER, on=(Detallecompras.codarticulo == Articulos.codarticulo))
)

for cliente in clientes_con_detalle:
    print(f"\nCódigo Cliente: {cliente.codigo_cli}")
    print(f"Nombre: {cliente.nombre}")
    print(f"Localidad: {cliente.localidad}")

    # Recupera todas las compras de este cliente
    compras_cliente = Compras.select().where(Compras.codigo_cli == cliente.codigo_cli)

    for compra in compras_cliente:
        print(f"  Número Compra: {compra.numcompra}")

        # Recupera las líneas de detalle para esta compra
        for linea in Detallecompras.select().where(Detallecompras.numcompra == compra.numcompra):
            articulo = linea.codarticulo
            importe = linea.unidades * articulo.precio if articulo.precio else 0  # Maneja precios nulos
            print(f"    Artículo: {articulo.denominacion}")
            print(f"    Unidades: {linea.unidades}, Precio: {articulo.precio}, Importe: {importe}")
print("\n")


# 4. Obtener el total de compra de cada cliente. Visualizar el código de
# cliente, nombre, localidad, número de compra e importe de la compra.
print("4_____________Total de compra por cliente: ")

clientes_totales = (
    Clientes
    .select(Clientes, Compras, Detallecompras)
    .join(Compras, JOIN.LEFT_OUTER)
    .join(Detallecompras, JOIN.LEFT_OUTER)
)

for cliente in clientes_totales:
    total = sum(linea.unidades * linea.precio_articulo for compra in cliente.compras for linea in compra.lineas)
    print(f"\nCódigo Cliente: {cliente.codigo_cli}")
    print(f"Nombre: {cliente.nombre}")
    print(f"Localidad: {cliente.localidad}")
    print(f"Total Importe: {total}")
print("\n")


# 5. Obtener el total de las compras de cada cliente y el número de compras
# realizadas. Visualizar el código del cliente, nombre, localidad, teléfono,
# número de compras que ha realizado y el importe total de las compras.
print("5_____________Total y número de compras por cliente: ")

clientes_con_resumen = (
    Clientes
    .select(Clientes, Compras)
    .join(Compras, JOIN.LEFT_OUTER)
    .prefetch(Compras)
)

for cliente in clientes_con_resumen:
    num_compras = len(cliente.compras)
    total_importe = sum(
        sum(linea.unidades * linea.precio_articulo for linea in compra.lineas)
        for compra in cliente.compras
    )
    print(f"\nCódigo Cliente: {cliente.codigo_cli}")
    print(f"Nombre: {cliente.nombre}")
    print(f"Localidad: {cliente.localidad}")
    print(f"Teléfono: {cliente.telefono}")
    print(f"Número de Compras: {num_compras}, Importe Total: {total_importe}")
print("\n")


# 6. Obtener para cada artículo las unidades compradas por los clientes, el
# importe y el nombre de su proveedor. Se deben visualizar los artículos sin
# compras. Visualizar código de artículo, denominación, stock, precio,
# unidades compradas, importe de las compras y nombre del proveedor.
print("6_____________Unidades compradas y proveedor por artículo: ")

articulos_con_compras = (
    Articulos
    .select(Articulos, Detallecompras, Proveedores)
    .join(Detallecompras, JOIN.LEFT_OUTER)
    .join(Proveedores, JOIN.LEFT_OUTER)
)

for articulo in articulos_con_compras:
    total_unidades = sum(linea.unidades for linea in articulo.lineas)
    total_importe = sum(linea.unidades * articulo.precio for linea in articulo.lineas)
    print(f"\nCódigo Artículo: {articulo.codigo_art}")
    print(f"Denominación: {articulo.denominacion}")
    print(f"Stock: {articulo.stock}, Precio: {articulo.precio}")
    print(f"Unidades Compradas: {total_unidades}, Importe Total: {total_importe}")
    if articulo.proveedor:
        print(f"Proveedor: {articulo.proveedor.nombre}")
    else:
        print("Proveedor: Sin asignar.")
print("\n")


# 7. Obtener para cada proveedor los artículos que suministra. Visualizar
# código de proveedor, nombre, código del artículo y denominación del
# artículo.
print("7_____________Artículos por proveedor: ")

proveedores_con_articulos = (
    Proveedores
    .select(Proveedores, Articulos)
    .join(Articulos, JOIN.LEFT_OUTER)
)

for proveedor in proveedores_con_articulos:
    print(f"\nCódigo Proveedor: {proveedor.codigo_prov}")
    print(f"Nombre: {proveedor.nombre}")
    if proveedor.articulos:
        for articulo in proveedor.articulos:
            print(f"  - Código Artículo: {articulo.codigo_art}")
            print(f"    Denominación: {articulo.denominacion}")
    else:
        print("Artículos: No suministra artículos.")
print("\n")


# 8. Visualizar por cada proveedor el número de artículos que suministra.
print("8_____________Número de artículos por proveedor: ")

for proveedor in proveedores_con_articulos:
    num_articulos = len(proveedor.articulos)
    print(f"\nCódigo Proveedor: {proveedor.codigo_prov}")
    print(f"Nombre: {proveedor.nombre}")
    print(f"Número de Artículos: {num_articulos}")
print("\n")


# 9. Visualizar el código de cliente, nombre y localidad de los clientes de
# Talavera que compraron artículos de la zona Centro.
print("9_____________Clientes de Talavera con compras de la zona Centro: ")

clientes_talavera_centro = (
    Clientes
    .select(Clientes, Compras, Detallecompras, Articulos)
    .join(Compras, JOIN.INNER)
    .join(Detallecompras, JOIN.INNER)
    .join(Articulos, JOIN.INNER)
    .where(
        (Clientes.localidad == "Talavera") &
        (Articulos.zona == "Centro")
    )
    .distinct()
)

for cliente in clientes_talavera_centro:
    print(f"Código Cliente: {cliente.codigo_cli}, Nombre: {cliente.nombre}, Localidad: {cliente.localidad}")

print("\n")


# 10. Visualizar código, nombre y localidad de los proveedores que
# suministran artículos de la zona centro.
print("10_____________Proveedores de la zona Centro: ")

proveedores_zona_centro = (
    Proveedores
    .select(Proveedores, Articulos)
    .join(Articulos, JOIN.INNER)
    .where(Articulos.zona == "Centro")
    .distinct()
)

for proveedor in proveedores_zona_centro:
    print(f"Código Proveedor: {proveedor.codigo_prov}, Nombre: {proveedor.nombre}, Localidad: {proveedor.localidad}")

print("\n")
