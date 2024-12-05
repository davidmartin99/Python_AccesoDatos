# hn_article.py
import requests
import json

# URL del artículo específico en Hacker News.
url = "https://hacker-news.firebaseio.com/v0/item/31353677.json"

# Hace una llamada a la API y guarda la respuesta.
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Convierte la respuesta JSON a un diccionario.
response_dict = r.json()

# Formatea el diccionario en una cadena JSON con sangría.
response_string = json.dumps(response_dict, indent=4)
print(response_string)
