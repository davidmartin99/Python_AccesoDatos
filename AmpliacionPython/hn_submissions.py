from operator import itemgetter
import requests

# Hace una llamada a la API de Hacker News para obtener los IDs de los artículos más populares
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Procesa la lista de IDs de los artículos principales
submission_ids = r.json()
submission_dicts = []

# Itera sobre los primeros 30 artículos
for submission_id in submission_ids[:30]:
    # Hace una nueva llamada a la API para obtener detalles de cada artículo
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")

    # Verifica si la solicitud fue exitosa
    if r.status_code == 200:
        response_dict = r.json()
        # Crea un diccionario para cada artículo
        submission_dict = {
            'title': response_dict.get('title', 'N/A'),
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict.get('descendants', 0),
        }
        submission_dicts.append(submission_dict)

# Ordena los artículos por número de comentarios en orden descendente
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# Imprime los datos de cada artículo
for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion Link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")
