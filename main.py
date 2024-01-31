# Importacion de FastAPI
from fastapi import FastAPI

# Importaciones de las funciones de enrutamiento desde diferentes módulos
from router.DeveloperFreeContent import DeveloperFreeContent
from router.UserDataStats import UserDataStats
from router.UserForGenreStats import UserForGenreStats
from router.BestDeveloperStats import BestDeveloperStats
from router.DeveloperReviewsStats import DeveloperReviewsStats

# Creación de una instancia de la aplicación FastAPI
app = FastAPI()

# Definición de una ruta para el punto de entrada principal
@app.get("/")
async def root():
    return {"HOME": "HOME"}

# Definición de una ruta para obtener funcionn developer
@app.get("/api/developer/{desarrollador}")
def Developer(desarrollador: str):
    return DeveloperFreeContent(desarrollador)

@app.get("/api/user_data/{user_id}")
async def User_Data(user_id: str):
    return UserDataStats(user_id)

@app.get("/api/user_for_genre/{genero}")
async def User_For_Genre(genero: str):
    return UserForGenreStats(genero)

@app.get("/api/best_developer_year/{anio}")
async def Best_Developer_Year(anio: int):
    return BestDeveloperStats(anio)

@app.get("/api/developer_review_stats/{desarrolladora}")
async def Developer_Reviews_Analysis(desarrolladora: str):
    return DeveloperReviewsStats(desarrolladora)

