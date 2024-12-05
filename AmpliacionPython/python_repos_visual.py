import requests
import plotly.express as px

# Paso 1: Obtener datos de la API de GitHub
# URL base de la API para obtener los repositorios más populares de Python
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {"Accept": "application/vnd.github.v3+json"}

response = requests.get(url, headers=headers)
if response.status_code != 200:
    print("Error al obtener los datos de la API de GitHub")
    exit()

# Procesar los datos obtenidos
repo_dicts = response.json()['items']
repo_links = []  # Lista para almacenar los nombres de los repositorios como enlaces
stars = []       # Lista para almacenar el número de estrellas
hover_texts = [] # Lista para almacenar los mensajes emergentes personalizados

for repo_dict in repo_dicts:
    # Obtener el nombre del repositorio y crear un enlace HTML para él
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    # Obtener el número de estrellas del repositorio
    stars.append(repo_dict['stargazers_count'])

    # Crear un mensaje emergente personalizado con propietario y descripción
    owner = repo_dict['owner']['login']
    description = repo_dict['description'] or "Sin descripción"
    hover_text = f"Propietario: {owner}<br />{description}"
    hover_texts.append(hover_text)

# Paso 2: Crear la visualización con Plotly Express
fig = px.bar(
    x=repo_links,  # Los nombres de los repositorios (como enlaces activos)
    y=stars,       # El número de estrellas
    title="Proyectos Python más populares en GitHub",  # Título del gráfico
    labels={"x": "Repositorio", "y": "Estrellas"},  # Etiquetas de los ejes
    hover_name=hover_texts  # Mensajes emergentes personalizados
)

# Paso 3: Personalizar el diseño del gráfico
fig.update_layout(
    title_font_size=28,  # Tamaño de la fuente del título
    xaxis_title_font_size=20,  # Tamaño de la fuente del título del eje X
    yaxis_title_font_size=20   # Tamaño de la fuente del título del eje Y
)

# Paso 4: Personalizar los colores de las barras
fig.update_traces(
    marker_color='Purple',  # Color de las barras
    marker_opacity=0.5
    # Opacidad de las barras
)

# Mostrar el gráfico
fig.show()

# Notas adicionales:
# - Para usar este código, necesitas instalar las librerías `requests` y `plotly`.
#   Puedes hacerlo ejecutando: `pip install requests plotly`
# - Asegúrate de estar conectado a Internet, ya que el código realiza llamadas a la API de GitHub.
# - Este gráfico incluye enlaces activos en los nombres de los repositorios para que los usuarios puedan visitar sus páginas en GitHub.
