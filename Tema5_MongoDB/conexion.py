from pymongo import MongoClient

# Conectar a MongoDB (localhost por defecto)
cliente = MongoClient("mongodb://localhost:27017/")
print("Conexión exitosa a MongoDB")
