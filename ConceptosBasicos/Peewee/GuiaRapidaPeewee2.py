from peewee import *
from datetime import date

# Conectar a la base de datos SQLite "personas.db"
db = SqliteDatabase('personas.db')

# Definir el modelo de la tabla Persona con un campo 'id' como clave primaria
class Persona(Model):
    id = AutoField()  # Clave primaria autoincremental
    nombre = CharField()  # Nombre de la persona
    fecha_nacimiento = DateField()  # Fecha de nacimiento

    class Meta:
        database = db  # Este modelo usa la base de datos "personas.db"

# Definir el modelo de la tabla Mascota con un campo 'id' como clave primaria
class Mascota(Model):
    id = AutoField()  # Clave primaria autoincremental
    propietario = ForeignKeyField(Persona, backref='mascotas')  # Clave foránea a la tabla Persona
    nombre = CharField()  # Nombre de la mascota
    tipo_animal = CharField()  # Tipo de animal (ej. 'gato', 'perro')

    class Meta:
        database = db  # Este modelo usa la base de datos "personas.db"

# Conectar a la base de datos
db.connect()

# Crear las tablas si no existen
db.create_tables([Persona, Mascota])

# Insertar datos solo si no existen (para Persona)
def crear_persona(nombre, fecha_nacimiento):
    # Verifica si la persona ya existe antes de insertar
    persona, created = Persona.get_or_create(nombre=nombre, fecha_nacimiento=fecha_nacimiento)
    return persona

# Insertar datos solo si no existen (para Mascota)
def crear_mascota(propietario, nombre, tipo_animal):
    # Verifica si la mascota ya existe antes de insertar
    mascota, created = Mascota.get_or_create(propietario=propietario, nombre=nombre, tipo_animal=tipo_animal)
    return mascota

# Crear instancias de Persona y guardar en la base de datos si no existen
juan = crear_persona('Juan', date(1980, 8, 15))
ana = crear_persona('Ana', date(1992, 5, 10))
pedro = crear_persona('Pedro', date(1970, 11, 25))

# Crear instancias de Mascota (mascotas) asociadas a personas específicas, si no existen
juan_perro = crear_mascota(juan, 'Max', 'perro')
ana_gato = crear_mascota(ana, 'Luna', 'gato')
pedro_ave = crear_mascota(pedro, 'Sky', 'ave')

# Eliminar la mascota 'Sky' de la base de datos
pedro_ave.delete_instance()

# Reasignar el dueño de 'Max' a 'ana' y guardar el cambio
juan_perro.propietario = ana
juan_perro.save()

# Consultar y mostrar todas las personas almacenadas en la base de datos
print("Todas las personas:")
for persona in Persona.select():
    print(f"{persona.id}: {persona.nombre}")  # Imprime la id y los nombres de las personas
print()  # Espacio en blanco para separar

# Consultar y mostrar todas las mascotas que son 'gatos'
print("Todas las mascotas de tipo 'gato':")
consulta = Mascota.select().where(Mascota.tipo_animal == 'gato')
for mascota in consulta:
    print(f"{mascota.nombre} - Dueño: {mascota.propietario.nombre}")  # Imprime el nombre de la mascota y su dueño
print()  # Espacio en blanco para separar

# Hacer una consulta con JOIN para obtener las mascotas con tipo_animal 'gato' y sus dueños
print("Mascotas de tipo 'gato' con JOIN:")
consulta = (Mascota
            .select(Mascota, Persona)  # Seleccionar tanto la mascota como la persona
            .join(Persona)  # Unir las tablas Mascota y Persona
            .where(Mascota.tipo_animal == 'gato'))  # Filtrar solo gatos

for mascota in consulta:
    print(f"{mascota.nombre} - Dueño: {mascota.propietario.nombre}")  # Imprime el nombre de la mascota y su dueño
print()  # Espacio en blanco para separar

# Consultar todas las mascotas que son de 'Ana' usando un JOIN
print("Mascotas de Ana:")
for mascota in Mascota.select().join(Persona).where(Persona.nombre == 'Ana'):
    print(mascota.nombre)  # Imprime los nombres de las mascotas de Ana
print()  # Espacio en blanco para separar

# Consultar las mascotas del dueño 'ana' usando la referencia ForeignKey
print("Mascotas de Ana (usando referencia ForeignKey):")
for mascota in Mascota.select().where(Mascota.propietario == ana):
    print(mascota.nombre)  # Imprime los nombres de las mascotas de Ana
