from datetime import datetime  # Importar clase para manejar fechas y horas
from peewee import *  # Importar Peewee, un ORM ligero para bases de datos

# Conexión a la base de datos SQLite
database = SqliteDatabase('twitter2.db')  # Crea/abre el archivo de base de datos llamado 'twitter2.db'

# Clase base para todos los modelos
class BaseModel(Model):
    class Meta:
        database = database  # Asocia la base de datos a los modelos derivados

# Modelo para los usuarios
class User(BaseModel):
    username = CharField(unique=True)  # Campo de texto único para el nombre de usuario
    password = CharField()  # Campo de texto para la contraseña
    email = CharField()  # Campo de texto para el correo electrónico
    join_date = DateTimeField()  # Campo para la fecha de registro del usuario

# Modelo para las relaciones entre usuarios (seguimientos, amistades, etc.)
class Relationship(BaseModel):
    from_user = ForeignKeyField(User, backref='relationships')  # Usuario que inicia la relación
    to_user = ForeignKeyField(User, backref='related_to')  # Usuario que recibe la relación

    class Meta:
        # Garantiza que no se puedan duplicar relaciones entre los mismos usuarios
        indexes = ((('from_user', 'to_user'), True),)

# Modelo para los mensajes
class Message(BaseModel):
    user = ForeignKeyField(User, backref='messages')  # Usuario que crea el mensaje
    content = TextField()  # Contenido del mensaje (campo de texto)
    pub_date = DateTimeField()  # Fecha de publicación del mensaje

# Bloque principal para ejecutar el script
if __name__ == '__main__':
    # Conectar a la base de datos
    database.connect()
    # Crear las tablas en la base de datos si no existen
    # database.create_tables([User, Relationship, Message])
    # print("Creado con exito")  # Mensaje de confirmación


##########################
# CREAR USUARIOS
##########################
# Crear un usuario llamado 'lucia'
# lucia = User.create(
#     username='lucia',
#     password='lucia',
#     email='darkydam2@gmail.com',
#     join_date=datetime.today()  # Fecha y hora actuales
# )
#
# # Crear un usuario llamado 'ele'
# ele = User.create(
#     username='ele',
#     password='ele',
#     email='eletrabajos@gmail.com',
#     join_date=datetime.today()  # Fecha y hora actuales
# )
#
# # Crear una relación (lucia sigue a ele)
# relation = Relationship.create(
#     from_user=lucia,  # Usuario que inicia la relación
#     to_user=ele       # Usuario objetivo de la relación
# )
#
#
# # Crear un mensaje de 'lucia'
# message = Message.create(
#     user=lucia,  # Usuario que publica el mensaje
#     content='Hello World!',  # Contenido del mensaje
#     pub_date=datetime.today()  # Fecha y hora de publicación
# )


############################
# VISUALIZAR SEGUIDORES
######################
# Visualizar seguidores de un usuario específico (por ejemplo, 'lucia')
user = User.get(User.username == 'lucia')  # Obtén el usuario que quieres mostrar los seguidores

print(f"\nSeguidores de {user.username}:")

# Consulta para encontrar a todos los usuarios que siguen a 'user'
followers = User.select().join(Relationship, on=(User.id == Relationship.from_user)).where(Relationship.to_user == user)

# Imprimir los nombres de los seguidores encontrados
# Bloque principal para ejecutar el script
if __name__ == '__main__':
    # Conectar a la base de datos

    # Visualizar un usuario específico y sus datos (por ejemplo, 'lucia')
    try:
        user = User.get(User.username == 'lucia')  # Obtén el usuario específico

        # Mostrar datos del usuario
        print(f"\nDatos de usuario '{user.username}':")
        print(f"Correo electrónico: {user.email}")
        print(f"Fecha de registro: {user.join_date.strftime('%Y-%m-%d %H:%M:%S')}")

        # Visualizar seguidores de 'lucia'
        print(f"\nSeguidores de {user.username}:")
        followers = User.select().join(Relationship, on=(User.id == Relationship.from_user)).where(Relationship.to_user == user)

        if followers.exists():  # Verifica si hay resultados
            for follower in followers:
                print(follower.username)
        else:
            print("No se encontraron seguidores.")

        # Visualizar a quién sigue 'lucia'
        print(f"\nUsuarios que {user.username} sigue:")
        following = User.select().join(Relationship, on=(User.id == Relationship.to_user)).where(Relationship.from_user == user)

        if following.exists():
            for followed_user in following:
                print(followed_user.username)
        else:
            print("No se encontraron usuarios que {user.username} sigue.")

        # Mostrar los mensajes de 'lucia' ordenados de más reciente a más antiguo
        print(f"\nMensajes de {user.username} (ordenados de más reciente a más antiguo):")
        messages = Message.select().where(Message.user == user).order_by(Message.pub_date.desc())

        if messages.exists():
            for message in messages:
                print(f"Fecha: {message.pub_date.strftime('%Y-%m-%d %H:%M:%S')}, Contenido: {message.content}")
        else:
            print("No se encontraron mensajes.")
    except User.DoesNotExist:
        print("El usuario 'lucia' no existe en la base de datos.")