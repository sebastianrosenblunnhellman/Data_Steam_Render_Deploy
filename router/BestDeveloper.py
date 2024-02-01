import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa

def BestDeveloper(anio: int):
    # Ruta de los archivos Parquet
    games_parquet = 'data/steam_games.parquet'
    reviews_parquet = 'data/user_reviews.parquet'

    # Utiliza PyArrow para leer el archivo Parquet
    tabla_games = pq.read_table(games_parquet)
    tabla_reviews = pq.read_table(reviews_parquet)

    # Leer las tablas en DataFrames de Pandas
    df_steam_games = tabla_games.to_pandas()
    df_user_reviews = tabla_reviews.to_pandas()

    # Merge de los DataFrames utilizando "item_id" como clave
    merged_df = pd.merge(df_steam_games, df_user_reviews, on='item_id', how='inner')

    # Filtrar el DataFrame por el anio dado
    df_filtered = merged_df[merged_df['release_year'] == anio]

    # Filtrar por juegos recomendados y comentarios positivos
    df_filtered = df_filtered[(df_filtered['recommend'] == True) & (df_filtered['sentiment_analysis'] == 2.0)]

    # Agrupar por desrrollador y contar la cantidad de juegos recomendados
    developer_counts = df_filtered.groupby('developer')['item_id'].count()

    # Obtener los tres mejores desarrolladores
    top_developers = developer_counts.nlargest(3)
    

    # Crear el formato de salida
    output = [{"Puesto {}: ".format(i+1) + developer: count} for i, (developer, count) in enumerate(top_developers.items())]

    return output