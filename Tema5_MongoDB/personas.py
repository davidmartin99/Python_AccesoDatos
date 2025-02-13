from pymongo import MongoClient

# Conectar a MongoDB (asegúrate de que el servicio está en ejecución)
cliente = MongoClient("mongodb://localhost:27017/")

# Seleccionar la base de datos (si no existe, MongoDB la crea automáticamente)
from pymongo import MongoClient

# Conectar a MongoDB
cliente = MongoClient("mongodb://localhost:27017/")

# Crear o seleccionar la base de datos "prueba"
db = cliente["prueba"]

# Crear o seleccionar la colección "persona"
col = db["persona"]

# Documento a insertar
persona = {
    "edad": 28,
    "nombre": "David",
    "intereses": ["programación", "tecnología", "música"]
}

# Insertar el documento en la colección
resultado = col.insert_one(persona)

# Mostrar el ID del documento insertado
print("Base de datos:", db.name)
print("Colección:", col.name)
print("Documento insertado con ID:", resultado.inserted_id)

################################################################################
################ Insertar varios documentos con insertMany
# Lista de documentos a insertar
personas = [
    {"edad": 25, "nombre": "Ana", "intereses": ["lectura", "viajes"]},
    {"edad": 30, "nombre": "Carlos", "intereses": ["deporte", "videojuegos"]},
    {"edad": 22, "nombre": "Elena", "intereses": ["fotografía", "cine"]},
    {"edad": 27, "nombre": "Luis", "intereses": ["programación", "música"]},
    {"edad": 35, "nombre": "María", "intereses": ["arte", "cocina"]}
]

# Insertar múltiples documentos en la colección
resultado = col.insert_many(personas)

# Mostrar el ID del documento insertado
print("Documento insertado con ID:", resultado.inserted_ids)


################ Mostrar las personas ordenadas por edad
print("\nPersonas ordenadas por edad:")
for doc in col.find().sort("edad", 1):  # Ordenar en orden ascendente por edad
    print(doc)

################################################################################
################ Eliminar un documento (nombre = "Luis")
print("\nEliminando a Luis...")
col.delete_one({"nombre": "Luis"})  # Eliminar solo el primer documento que coincida con el nombre "Luis"

# Mostrar los documentos después de la eliminación
print("\nPersonas después de eliminar a Luis:")
for doc in col.find().sort("edad", 1):
    print(doc)

################# Eliminar múltiples documentos (edad > 29)
print("\nEliminando personas con edad mayor a 29...")
col.delete_many({"edad": {"$gt": 29}})  # Eliminar documentos con edad mayor a 29

# Mostrar los documentos después de la eliminación
print("\nPersonas después de eliminar a los mayores de 29:")
for doc in col.find().sort("edad", 1):
    print(doc)

################# Eliminar todos los documentos de la colección
# print("\nEliminando todos los documentos...")
# col.delete_many({})  # Eliminar todos los documentos de la colección