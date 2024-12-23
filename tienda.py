from peewee import *

database = MySQLDatabase('tienda', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'user': 'root', 'password': '1234'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Proveedor(BaseModel):
    codigo_prov = AutoField()
    comision = FloatField()
    fecha_alta = DateField(null=True)
    localidad = CharField()
    nombre = CharField()

    class Meta:
        table_name = 'proveedor'

class Articulo(BaseModel):
    codarticulo = AutoField()
    codigo_prov = ForeignKeyField(column_name='codigo_prov_id', field='codigo_prov', model=Proveedor)
    denominacion = CharField()
    precio = FloatField()
    stock = IntegerField()
    zona = CharField(null=True)

    class Meta:
        table_name = 'articulo'

class Proveedores(BaseModel):
    codigo_prov = AutoField()
    comision = FloatField(null=True)
    fecha_alta = DateField(null=True)
    localidad = CharField(null=True)
    nombre = CharField()

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

class Cliente(BaseModel):
    codigo_cli = AutoField()
    localidad = CharField()
    nombre = CharField()
    tlf = CharField(null=True)

    class Meta:
        table_name = 'cliente'

class Clientes(BaseModel):
    codigo_cli = AutoField()
    localidad = CharField(null=True)
    nombre = CharField()
    tlf = CharField(null=True)

    class Meta:
        table_name = 'clientes'

class Compra(BaseModel):
    codigo_cli = ForeignKeyField(column_name='codigo_cli_id', field='codigo_cli', model=Cliente)
    fechacompra = DateField()
    numcompra = AutoField()

    class Meta:
        table_name = 'compra'

class Compras(BaseModel):
    codigo_cli = ForeignKeyField(column_name='codigo_cli', field='codigo_cli', model=Clientes, null=True)
    fechacompra = DateField(null=True)
    numcompra = AutoField()

    class Meta:
        table_name = 'compras'

class Detallecompra(BaseModel):
    codarticulo = ForeignKeyField(column_name='codarticulo_id', field='codarticulo', model=Articulo)
    numcompra = ForeignKeyField(column_name='numcompra_id', field='numcompra', model=Compra)
    unidades = IntegerField()

    class Meta:
        table_name = 'detallecompra'
        indexes = (
            (('numcompra', 'codarticulo'), True),
        )
        primary_key = False

class Detallecompras(BaseModel):
    codarticulo = ForeignKeyField(column_name='codarticulo', field='codarticulo', model=Articulos)
    numcompra = ForeignKeyField(column_name='numcompra', field='numcompra', model=Compras)
    unidades = IntegerField(null=True)

    class Meta:
        table_name = 'detallecompras'
        indexes = (
            (('numcompra', 'codarticulo'), True),
        )
        primary_key = CompositeKey('codarticulo', 'numcompra')


