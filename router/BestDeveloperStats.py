import pandas as pd

def BestDeveloperStats(anio: int):
    # Ruta de los archivos Parquet
    games_parquet = r'data\steam_games.parquet'
    reviews_parquet = r'data\user_reviews.parquet'

    # Leer los archivos Parquet en DataFrames de Pandas
    df_steam_games = pd.read_parquet(games_parquet)
    df_user_reviews = pd.read_parquet(reviews_parquet)

    # Merge de los DataFrames utilizando "item_id" como clave
    merged_df = pd.merge(df_steam_games, df_user_reviews, on='item_id', how='inner')

    # Filtrar el DataFrame por el anio dado
    df_filtered = merged_df[merged_df['year'] == anio]

    # Filtrar por juegos recomendados y comentarios positivos
    df_filtered = df_filtered[(df_filtered['recommend'] == True) & (df_filtered['sentiment_analysis'] == 2.0)]

    # Agrupar por desrrollador y contar la cantidad de juegos recomendados
    developer_counts = df_filtered.groupby('developer')['item_id'].count()

    # Obtener los tres mejores desarrolladores
    top_developers = developer_counts.nlargest(3)
    

    # Crear el formato de salida
    output = [{"Puesto {}: ".format(i+1) + developer: count} for i, (developer, count) in enumerate(top_developers.items())]

    return output