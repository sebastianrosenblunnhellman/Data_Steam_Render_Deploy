import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa
import numpy as np

def GenreStats(genero: str):
    # Cargar los datos desde el archivo Parquet
    file_path = 'data/UserForGenre.parquet'
    table = pq.read_table(file_path)
    genre_data = table.to_pandas()

    # Filtrar los datos por género
    genre_data = genre_data[genre_data['genero'] == genero]

    if genre_data.empty:
        return {"error": "No hay datos para el género especificado"}

    # Obtener el usuario con más horas jugadas para el género dado
    max_hours_user = genre_data.loc[genre_data['Horas jugadas'].idxmax(), 'usuario con mas horas jugadas']

    # Obtener las horas jugadas por año
    horas_por_año = {}
    for index, row in genre_data.iterrows():
        for entry in row['Horas jugadas']:
            año = entry['Año']
            horas = entry['Horas']
            if año in horas_por_año:
                horas_por_año[año] += horas
            else:
                horas_por_año[año] = horas

    # Formatear el resultado
    result = {
        "Usuario con más horas jugadas para {}".format(genero): max_hours_user,
        "Horas jugadas por año": horas_por_año
    }
    return result
