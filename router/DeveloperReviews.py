import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa

def DeveloperReviews(desarrolladora: str):
    # Ruta de los archivos Parquet
    games_parquet = r'data\steam_games.parquet'
    reviews_parquet = r'data\user_reviews.parquet'

    # Utiliza PyArrow para leer el archivo Parquet
    tabla_games = pq.read_table(games_parquet)
    tabla_reviews = pq.read_table(reviews_parquet)

    # Leer las tablas en DataFrames de Pandas
    df_steam_games = tabla_games.to_pandas()
    df_user_reviews = tabla_reviews.to_pandas()

    # Merge de los DataFrames utilizando "item_id" como clave
    merged_df = pd.merge(df_steam_games, df_user_reviews, on='item_id', how='inner')

    # Filtrar el DataFrame para obtener solo las filas correspondientes a la desarrolladora dada
    df_dev = merged_df[merged_df['developer'] == desarrolladora]

    # Inicializar el diccionario para almacenar los resultados
    results = {desarrolladora: {"Negative": 0, "Positive": 0}}

    # Iterar sobre las filas del DataFrame y contar las reseñas positivas y negativas
    for index, row in df_dev.iterrows():
        if row['sentiment_analysis'] == 1.0:
            results[desarrolladora]["Negative"] += 1
        elif row['sentiment_analysis'] == 2.0:
            results[desarrolladora]["Positive"] += 1

    return results

