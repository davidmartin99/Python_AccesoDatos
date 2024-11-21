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
##
# !!!!!!! Más rápido, cuando haya varias consultas relacionadas con claves ajenas, hacemos un JOIN
#
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


#
# CLASIFICACION
#
# Consultar y mostrar todas las mascotas ordenadas alfabéticamente por nombre
print("Mascotas ordenadas por nombre:")
for mascota in Mascota.select().order_by(Mascota.nombre):
    print(f"{mascota.nombre} - Dueño: {mascota.propietario.nombre}")
print()

# Consultar y mostrar todas las personas ordenadas de la más joven a la más vieja
print("Personas ordenadas por fecha de nacimiento (de joven a vieja):")
for persona in Persona.select().order_by(Persona.fecha_nacimiento.desc()):
    print(f"{persona.nombre} - Fecha de nacimiento: {persona.fecha_nacimiento}")
# Muestra las personas más jovenes primero ya que por ejemplo 2004 es mayor a 1997


#########################################
# Combinación de expresiones de filtro
#
# Filtrar personas nacidas antes de 1940 o después de 1959
d1940 = date(1940, 1, 1)
d1960 = date(1960, 1, 1)
query = (Persona
         .select()
         .where((Persona.fecha_nacimiento < d1940) | (Persona.fecha_nacimiento > d1960)))

print("Personas nacidas antes de 1940 o después de 1959:")
for persona in query:
    print(f"{persona.nombre} - Fecha de nacimiento: {persona.fecha_nacimiento}")
print()

# Filtrar personas nacidas entre 1940 y 1960 (ambos años incluidos)
query = (Persona
         .select()
         .where(Persona.fecha_nacimiento.between(d1940, d1960)))

print("Personas nacidas entre 1940 y 1960:")
for persona in query:
    print(f"{persona.nombre} - Fecha de nacimiento: {persona.fecha_nacimiento}")

##########################
# Agregados y precarga
#
# Enumerar todas las personas y cuántas mascotas tienen
print("Personas y número de mascotas:")
for persona in Persona.select():
    print(persona.nombre, persona.mascotas.count(), 'mascotas')

# Optimizar la consulta utilizando JOIN y agregados
print("\nPersonas y número de mascotas (optimizado):")
from peewee import fn

query = (Persona
         .select(Persona, fn.COUNT(Mascota.id).alias('cantidad_mascotas'))
         .join(Mascota, JOIN.LEFT_OUTER)  # Incluir personas sin mascotas
         .group_by(Persona)
         .order_by(Persona.nombre))

for persona in query:
    print(persona.nombre, persona.cantidad_mascotas, 'mascotas')

# Enumerar todas las personas y los nombres de sus mascotas
print("\nPersonas y nombres de sus mascotas:")
query = (Persona
         .select(Persona, Mascota)
         .join(Mascota, JOIN.LEFT_OUTER)
         .order_by(Persona.nombre, Mascota.nombre))
for persona in query:
    if hasattr(persona, 'mascota'):
        print(persona.nombre, persona.mascota.nombre)
    else:
        print(persona.nombre, 'sin mascotas')

# Optimizar la consulta utilizando prefetch
print("\nPersonas y nombres de sus mascotas (optimizado con prefetch):")
query = Persona.select().order_by(Persona.nombre).prefetch(Mascota)
for persona in query:
    print(persona.nombre)
    for mascota in persona.mascotas:
        print('  *', mascota.nombre)


#############################
# Funciones SQL
#
print("\nPersonas cuyos nombres comienzan con G o P (mayúscula o minúscula):")
from peewee import fn

# Crear dos expresiones: una para nombres que empiezan con 'g' y otra para 'p'
expression = (fn.Lower(fn.Substr(Persona.nombre, 1, 1)) == 'g') | \
             (fn.Lower(fn.Substr(Persona.nombre, 1, 1)) == 'p')

# Consultar las personas que cumplen con alguna de las dos condiciones
for persona in Persona.select().where(expression):
    print(persona.nombre)


#######################
# Database
#
db.close()


##########################
# Usamos PWIZ
#
