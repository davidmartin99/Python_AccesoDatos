from peewee import *
from datetime import date

# Conectar a la base de datos SQLite "people.db"
db = SqliteDatabase('people.db')

# Definir el modelo de la tabla Person
class Person(Model):
    name = CharField()  # Nombre de la persona
    birthday = DateField()  # Fecha de nacimiento

    class Meta:
        database = db  # Este modelo usa la base de datos "people.db"

# Definir el modelo de la tabla Pet (Mascota)
class Pet(Model):
    owner = ForeignKeyField(Person, backref='pets')  # Llave foránea a la tabla Person
    name = CharField()  # Nombre de la mascota
    animal_type = CharField()  # Tipo de animal (ej. 'cat', 'dog')

    class Meta:
        database = db  # Este modelo usa la base de datos "people.db"

# Conectar a la base de datos
db.connect()

# Crear las tablas si no existen
db.create_tables([Person, Pet])

# Crear instancias de Person y guardar en la base de datos
uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15))
uncle_bob.save()  # Guarda la persona 'Bob'

# Insertar más registros de Person
grandma = Person.create(name='Grandma', birthday=date(1935, 3, 1))
herb = Person.create(name='Herb', birthday=date(1950, 5, 5))

# Actualizar el nombre de 'Grandma' y guardar el cambio
grandma.name = 'Grandma L.'
grandma.save()  # Guarda la actualización

# Crear instancias de Pet (mascotas) asociadas a personas específicas
bob_kitty = Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
herb_fido = Pet.create(owner=herb, name='Fido', animal_type='dog')
herb_mittens = Pet.create(owner=herb, name='Mittens', animal_type='cat')
herb_mittens_jr = Pet.create(owner=herb, name='Mittens Jr', animal_type='cat')

# Eliminar la mascota 'Mittens' de la base de datos
herb_mittens.delete_instance()

# Reasignar el dueño de 'Fido' a 'uncle_bob' y guardar el cambio
herb_fido.owner = uncle_bob
herb_fido.save()

# Obtener a la persona 'Grandma L.' mediante una consulta
grandma = Person.select().where(Person.name == 'Grandma L.').get()

# Otra forma de obtener a 'Grandma L.'
grandma = Person.get(Person.name == 'Grandma L.')

# Imprimir los nombres de todas las personas almacenadas en la base de datos
for person in Person.select():
    print(person.name)  # Salida: Bob, Grandma L., Herb

# Consultar y mostrar todas las mascotas que son 'gatos'
query = Pet.select().where(Pet.animal_type == 'cat')
for pet in query:
    print(pet.name, pet.owner.name)  # Salida: Kitty Bob, Mittens Jr Herb

# Hacer una consulta con JOIN para obtener las mascotas con animal_type 'cat' y sus dueños
query = (Pet
         .select(Pet, Person)  # Seleccionar tanto la mascota como la persona
         .join(Person)  # Unir las tablas Pet y Person
         .where(Pet.animal_type == 'cat'))  # Filtrar solo gatos

# Imprimir los nombres de las mascotas y sus dueños
for pet in query:
    print(pet.name, pet.owner.name)  # Salida: Kitty Bob, Mittens Jr Herb

# Consultar todas las mascotas que son de 'Bob' usando un JOIN
for pet in Pet.select().join(Person).where(Person.name == 'Bob'):
    print(pet.name)  # Salida: Kitty, Fido

# Consultar las mascotas del dueño 'uncle_bob' usando la referencia ForeignKey
for pet in Pet.select().where(Pet.owner == uncle_bob):
    print(pet.name)  # Salida: Kitty, Fido
