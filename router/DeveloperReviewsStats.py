import pandas as pd

def DeveloperReviewsStats(desarrolladora: str):
    # Ruta de los archivos Parquet
    games_parquet = r'data\steam_games.parquet'
    reviews_parquet = r'data\user_reviews.parquet'

    # Leer los archivos Parquet en DataFrames de Pandas
    df_steam_games = pd.read_parquet(games_parquet)
    df_user_reviews = pd.read_parquet(reviews_parquet)

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

