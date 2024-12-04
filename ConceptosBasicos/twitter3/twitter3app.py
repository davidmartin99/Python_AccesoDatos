from peewee import SqliteDatabase, CharField, DateTimeField, Model, ForeignKeyField, TextField, BooleanField, fn, JOIN
from datetime import datetime

# Configuración de la base de datos
DATABASE = 'twitter3.db'
database = SqliteDatabase(DATABASE)
 # pragmas={'foreign_keys':1} para que si borras on delete cascade se borre lo relacionado con las demas tablas

# Base Model para usar la base de datos
class BaseModel(Model):
    class Meta:
        database = database

# Modelos
class User(BaseModel):
    username = CharField(unique=True)
    password = CharField()
    email = CharField()
    join_date = DateTimeField()

    def following(self):
        return (User
                .select()
                .join(Relationship, on=Relationship.to_user)
                .where(Relationship.from_user == self)
                .order_by(User.username))

    def followers(self):
        return (User
                .select()
                .join(Relationship, on=Relationship.from_user)
                .where(Relationship.to_user == self)
                .order_by(User.username))


class Relationship(BaseModel):
    from_user = ForeignKeyField(User, backref='relationships')
    to_user = ForeignKeyField(User, backref='related_to')

    class Meta:
        indexes = (
            (('from_user', 'to_user'), True),
        )


class Message(BaseModel):
    user = ForeignKeyField(User, backref='messages')
    content = TextField()
    pub_date = DateTimeField()
    is_published = BooleanField(default=False)  # Nuevo campo con valor predeterminado False

# Añadimos Favorites para favoritos a los tweets
class Favorite(BaseModel):
    user = ForeignKeyField(User, backref='favorites')
    message = ForeignKeyField(Message, backref='favorites')


# Insertar datos de ejemplo
def insert_data():
    User.delete().execute()  # Eliminar todos los registros de User
    Message.delete().execute()  # Eliminar mensajes existentes

    # Crear usuarios de ejemplo
    alice = User.create(username='Alice', password='alice123', email='alice@example.com', join_date=datetime.now())
    bob = User.create(username='Bob', password='bob123', email='bob@example.com', join_date=datetime.now())

    # Crear mensajes con is_published en True y False
    msg1 = Message.create(user=alice, content="Hola, soy Alice!", pub_date=datetime(2023, 11, 25),
                          is_published=True)
    msg2 = Message.create(user=alice, content="Este es otro mensaje de Alice.", pub_date=datetime(2023, 11, 28),
                          is_published=False)
    msg3 = Message.create(user=bob, content="Hola desde la cuenta de Bob.", pub_date=datetime(2023, 11, 26),
                          is_published=True)
    msg4 = Message.create(user=bob, content="Este mensaje no está publicado aún.", pub_date=datetime(2023, 11, 27),
                          is_published=False)

    # Insertar favoritos
    Favorite.create(user=alice, message=msg3)  # Alice marca como favorito un mensaje de Bob
    Favorite.create(user=bob, message=msg1)  # Bob marca como favorito un mensaje de Alice

    print("Datos insertados con éxito.")



def delete_user_by_id(user_id):
    try:
        user = User.get(User.id == user_id)  # Buscar al usuario por ID
        rows_deleted = user.delete_instance()  # Eliminar el usuario
        print(f"Usuario con ID {user_id} eliminado. Filas afectadas: {rows_deleted}")
    except User.DoesNotExist:
        print(f"El usuario con ID {user_id} no existe.")


def create_tables():
    with database:
        database.create_tables([User, Relationship, Message, Favorite])


# Insertar datos de ejemplo
def insert_sample_data():
    user1 = User.create(username='Alice', password='alicepass', email='alice@example.com', join_date=datetime.now())
    user2 = User.create(username='Bob', password='bobpass', email='bob@example.com', join_date=datetime.now())
    user3 = User.create(username='Charlie', password='charliepass', email='charlie@example.com', join_date=datetime.now())
    user4 = User.create(username='Diana', password='dianapass', email='diana@example.com', join_date=datetime.now())

    # Crear relaciones
    Relationship.create(from_user=user1, to_user='alice')  # Alice sigue a Bob
    Relationship.create(from_user=user1, to_user=user3)  # Alice sigue a Charlie
    Relationship.create(from_user=user2, to_user=user3)  # Bob sigue a Diana
    Relationship.create(from_user=user3, to_user=user4)  # Charlie sigue a Diana

    # Crear mensajes
    Message.create(user=user1, content="Hello from Alice!", pub_date=datetime.now())
    Message.create(user=user2, content="Bob here, how are you?", pub_date=datetime.now())
    Message.create(user=user3, content="Charlie says hi!", pub_date=datetime.now())
    Message.create(user=user4, content="Diana's first message.", pub_date=datetime.now())

    return user1, user2, user3, user4


# Recuperar datos y mostrar ejemplos
def display_data():
    alice = User.get(User.username == 'Alice')

    # Mostrar a quién sigue Alice
    print("Alice sigue a:")
    for user in alice.following():
        print(f"- {user.username} ({user.email})")

    # Mostrar quién sigue a Alice
    print("\nAlice es seguida por:")
    for user in alice.followers():
        print(f"- {user.username} ({user.email})")

    # Mostrar mensajes de todos los usuarios
    print("\nMensajes publicados:")
    for message in Message.select():
        print(f"{message.user.username} escribió: {message.content} el {message.pub_date}")


# Recuperar mensajes en orden descendente por fecha
def mensajes_desc():
    messages = (Message
                .select(Message, User)
                .join(User)
                .order_by(Message.pub_date.desc()))
    print("\nMensajes (más recientes primero):")
    for message in messages:
        print(f"{message.user.username} escribió: {message.content} el {message.pub_date}")


# Actualizar mensajes según la fecha
def update_published_messages():
    today = datetime.today()
    query = Message.update(is_published=False).where(Message.pub_date < today)
    rows_updated = query.execute()  # Devuelve el número de filas actualizadas
    print(f"\n{rows_updated} mensajes se han marcado como publicados.")





# def populate_test_data():
#     database.create_tables([User, Message, Favorite])
#
#     data = (
#         ('huey', ('meow', 'hiss', 'purr')),
#         ('mickey', ('woof', 'whine')),
#         ('zaizee', ())
#     )
#
#     # Insert users and their tweets
#     for username, tweets in data:
#         user = User.create(username=username)
#         for tweet in tweets:
#             Message.create(user=user, content=tweet)
#
#     # Populate a few favorites for our users
#     favorite_data = (
#         ('huey', ['whine']),
#         ('mickey', ['purr']),
#         ('zaizee', ['meow', 'purr'])
#     )
#
#     for username, favorites in favorite_data:
#         user = User.get(User.username == username)
#         for content in favorites:
#             tweet = Message.get(Message.content == content)
#             Favorite.create(user=user, tweet=tweet)

def get_user_favorite_counts():
    # Consulta para contar los favoritos por usuario
    queryContar = (
        User
        .select(
            User.username,
            fn.COUNT(Favorite.id).alias('count')
        )
        .join(Message, JOIN.LEFT_OUTER)
        .join(Favorite, JOIN.LEFT_OUTER)
        .group_by(User.username)
    )

    # Iterar sobre los resultados e imprimirlos
    print("- Cuantos favoritos hay por usuario: ")
    for user in queryContar:
        print(f"Usuario: {user.username}, Favoritos: {user.count}")



def get_favorites_with_authors():
    # Alias para referenciar la tabla User dos veces
    Owner = User.alias()

    # Consulta usando Peewee
    query = (
        Favorite
        .select(
            Favorite,                 # Incluye los datos del favorito
            Message.content,            # Contenido del tweet
            User.username.alias('author'),  # Autor del tweet
            Owner.username.alias('owner')   # Propietario del favorito
        )
        .join(Owner)  # Join favorite -> user (owner of favorite)
        .switch(Favorite)
        .join(Message)  # Join favorite -> tweet
        .join(User)   # Join tweet -> user (author of the tweet)
    )

    # Iterar sobre los resultados e imprimir
    for favorite in query:
        print(f"Propietario: {favorite.user.username}, Tweet: {favorite.message.content}, Author: {favorite.message.user.username}")


# Ejecución principal
if __name__ == "__main__":
    database.connect()
    database.drop_tables([User, Relationship, Message])  # Eliminar tablas existentes
    create_tables()

    # insert_data()
    insert_sample_data()
    display_data()  # Mostrar datos
    mensajes_desc()
    update_published_messages()

    get_user_favorite_counts()
    get_favorites_with_authors()
    # Eliminar un usuario
    # delete_user_by_id(1)  # Intenta eliminar al usuario con ID 1
    display_data()  # Mostrar datos después de eliminar al usuario



