# Importacion de FastAPI
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

# Importaciones de las funciones de enrutamiento desde diferentes módulos
from router.DeveloperContent import DeveloperContent
from router.UserInfo import UserInfo
from router.GenreStats import GenreStats
from router.BestDeveloper import BestDeveloper
from router.DeveloperReviews import DeveloperReviews
from router.item_item import item_item
from router.user_item import user_item


app = FastAPI()

@app.get("/", response_class=HTMLResponse)  # Esta ruta devuelve un HTML 
async def root():
    html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Proyecto Steam</title>
    <style>
        body {
            background: linear-gradient(to bottom, #5880E5, #57ACE6);
            color: white;
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .content {
            text-align: center;
        }
        h1 {
            margin-top: 0;
        }
    </style>
</head>
<body>
    <div class="content">
        <h1>¡Bienvenido al API de Machine Learning del Conjunto de Datos de Steam!</h1>
        <p>Para comenzar a explorar nuestros endpoints de consulta y de machine learning, simplemente sigue este enlace: <a href="https://steam-data-project.onrender.com/docs">https://steam-data-project.onrender.com/docs</a> 🚀</p>
        <p>¡Esperamos que disfrutes explorando los datos!</p>
    </div>
</body>
</html>
"""
    return html_content

# Definición de una ruta para obtener funcionn developer
@app.get("/api/desarrollador/{desarrollador}")
async def Developer(desarrollador: str):
    return DeveloperContent(desarrollador)

@app.get("/api/datos_usuario/{user_id}")
async def User_Data(user_id: str):
    return UserInfo(user_id)

@app.get("/api/usuario_por_genero/{genero}")
async def User_For_Genre(genero: str):
    return GenreStats(genero)

@app.get("/api/mejor_desarrollador/{anio}")
async def Best_Developer_Year(anio: int):
    return BestDeveloper(anio)

@app.get("/api/reviews_por_desarrolladora/{desarrolladora}")
async def Developer_Reviews_Analysis(desarrolladora: str):
    return DeveloperReviews(desarrolladora)

@app.get("/api/recomendacion_item/{item_id}")
async def recomendacion_juego(item_id: str):
    return item_item(item_id)

@app.get("/api/recomendacion_usuario/{user_id}")
async def recomendacion_usuario(user_id: str):
    return user_item(user_id)