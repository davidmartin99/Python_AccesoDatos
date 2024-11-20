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

# Insertar datos solo si no existen
def create_person(name, birthday):
    # Verifica si la persona ya existe antes de insertar
    person, created = Person.get_or_create(name=name, birthday=birthday)
    return person

def create_pet(owner, name, animal_type):
    # Verifica si la mascota ya existe antes de insertar
    pet, created = Pet.get_or_create(owner=owner, name=name, animal_type=animal_type)
    return pet

# Crear instancias de Person y guardar en la base de datos si no existen
uncle_bob = create_person('Bob', date(1960, 1, 15))
grandma = create_person('Grandma', date(1935, 3, 1))
grandma.name = 'Grandma L.'  # Actualizamos el nombre
grandma.save()  # Guarda la actualización
herb = create_person('Herb', date(1950, 5, 5))

# Crear instancias de Pet (mascotas) asociadas a personas específicas, si no existen
bob_kitty = create_pet(uncle_bob, 'Kitty', 'cat')
herb_fido = create_pet(herb, 'Fido', 'dog')
herb_mittens = create_pet(herb, 'Mittens', 'cat')
herb_mittens_jr = create_pet(herb, 'Mittens Jr', 'cat')

# Eliminar la mascota 'Mittens' de la base de datos
herb_mittens.delete_instance()

# Reasignar el dueño de 'Fido' a 'uncle_bob' y guardar el cambio
herb_fido.owner = uncle_bob
herb_fido.save()

# Consultar y mostrar todas las personas almacenadas en la base de datos
print("Todas las personas:")
for person in Person.select():
    print(person.name)  # Imprime los nombres de las personas
print()  # Espacio en blanco para separar

# Consultar y mostrar todas las mascotas que son 'gatos'
print("Todas las mascotas de tipo 'gato':")
query = Pet.select().where(Pet.animal_type == 'cat')
for pet in query:
    print(f"{pet.name} - Dueño: {pet.owner.name}")  # Imprime el nombre de la mascota y su dueño
print()  # Espacio en blanco para separar

# Hacer una consulta con JOIN para obtener las mascotas con animal_type 'cat' y sus dueños
print("Mascotas de tipo 'gato' con JOIN:")
query = (Pet
         .select(Pet, Person)  # Seleccionar tanto la mascota como la persona
         .join(Person)  # Unir las tablas Pet y Person
         .where(Pet.animal_type == 'cat'))  # Filtrar solo gatos

for pet in query:
    print(f"{pet.name} - Dueño: {pet.owner.name}")  # Imprime el nombre de la mascota y su dueño
print()  # Espacio en blanco para separar

# Consultar todas las mascotas que son de 'Bob' usando un JOIN
print("Mascotas de Bob:")
for pet in Pet.select().join(Person).where(Person.name == 'Bob'):
    print(pet.name)  # Imprime los nombres de las mascotas de Bob
print()  # Espacio en blanco para separar

# Consultar las mascotas del dueño 'uncle_bob' usando la referencia ForeignKey
print("Mascotas de Uncle Bob (usando referencia ForeignKey):")
for pet in Pet.select().where(Pet.owner == uncle_bob):
    print(pet.name)  # Imprime los nombres de las mascotas de Uncle Bob
