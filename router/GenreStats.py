import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa


def GenreStats(genero: str):
    # Ruta de los archivos Parquet
    games_parquet = 'data/steam_games.parquet'
    items_parquet = 'data/user_items.parquet'

    # Utiliza PyArrow para leer el archivo Parquet
    tabla_games = pq.read_table(games_parquet)
    tabla_items = pq.read_table(items_parquet)

    # Leer las tablas en DataFrames de Pandas
    df_steam_games = tabla_games.to_pandas()
    df_user_items = tabla_items.to_pandas()

    # Filtra los juegos por el género especificado
    juegos_filtrados = df_steam_games[df_steam_games['genres'].str.contains(genero, case=False, na=False)]

    # Fusiona df_user_items y df_games basándose en item_id e id
    df_fusionado = pd.merge(df_user_items, juegos_filtrados, left_on='item_id', right_on='item_id', how='inner')

    # Agrupa por año y usuario, calcula el tiempo de juego por usuario por año
    agrupado = df_fusionado.groupby(['release_year', 'user_id'])['playtime_forever'].sum().reset_index()

    if len(agrupado) > 0:
        # Encuentra al usuario con más tiempo de juego para el género dado
        usuario_max = agrupado[agrupado['playtime_forever'] == agrupado.groupby('release_year')['playtime_forever'].transform('max')]['user_id'].values[0]
    else:
        return {"error": "No hay datos disponibles para el género especificado"}

    # Filtra los datos para el usuario con más tiempo de juego
    datos_usuario = agrupado[agrupado['user_id'] == usuario_max]

    # Elimina los años con 0 tiempo de juego
    datos_usuario = datos_usuario[datos_usuario['playtime_forever'] > 0]

    # Ordena los años en orden descendente
    datos_usuario = datos_usuario.sort_values(by='release_year', ascending=False)

    # Convierte el tiempo de juego a enteros
    datos_usuario['playtime_forever'] = datos_usuario['playtime_forever'].astype(int)

    # Crea una lista de tiempo de juego acumulado por año
    horas_por_año = [{'Año': int(año), 'Horas': int(horas)} for año, horas in zip(datos_usuario['release_year'], datos_usuario['playtime_forever'])]

    resultado = {
        "Usuario con más tiempo de juego para el género " + genero: usuario_max,
        "Tiempo de juego": horas_por_año
    }

    return resultado
