# Importacion de FastAPI
from fastapi import FastAPI

# Importaciones de las funciones de enrutamiento desde diferentes módulos
from router.DeveloperContent import DeveloperContent
from router.UserInfo import UserInfo
from router.GenreStats import GenreStats
from router.BestDeveloper import BestDeveloper
from router.DeveloperReviews import DeveloperReviews

# Creación de una instancia de la aplicación FastAPI
app = FastAPI()

# Definición de una ruta para el punto de entrada principal
@app.get("/")
async def root():
    return {"HOME": "HOME"}

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

