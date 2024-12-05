import requests  # Librería para realizar solicitudes HTTP

# URL de la API de GitHub para buscar repositorios
url = "https://api.github.com/search/repositories"

# Se agregan parámetros a la URL para filtrar los resultados
# Busca repositorios escritos en Python, ordenados por estrellas y con más de 10,000 estrellas
url += "?q=language:python+sort:stars+stars:>10000"

# Cabeceras para especificar la versión de la API de GitHub
headers = {"Accept": "application/vnd.github.v3+json"}

# Realiza la solicitud GET a la API de GitHub
response = requests.get(url, headers=headers)

# Imprime el código de estado de la respuesta
print(f"Status code: {response.status_code}")  # 200 indica éxito

# Convierte la respuesta en un diccionario JSON si la solicitud fue exitosa
if response.status_code == 200:
    response_dict = response.json()  # La respuesta se transforma en un diccionario

    # Imprime las claves principales del diccionario para explorar su estructura
    print("Claves en la respuesta:", response_dict.keys())

    # Imprime el número total de repositorios encontrados y si los resultados están completos
    print(f"Total repositories: {response_dict['total_count']}")
    print(f"Complete results: {not response_dict['incomplete_results']}")

    # Lista de los primeros repositorios encontrados
    repo_dicts = response_dict['items']
    print(f"Repositories returned: {len(repo_dicts)}")

    # Examina el primer repositorio
    repo_dict = repo_dicts[0]
    print(f"\nKeys in first repository: {len(repo_dict)}")
    for key in sorted(repo_dict.keys()):
        print(key)

    # Extrae información seleccionada del primer repositorio
    print("\nSelected information about first repository:")
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")
else:
    print("Error en la solicitud.")
