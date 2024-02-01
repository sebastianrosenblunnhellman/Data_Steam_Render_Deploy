import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa

def UserInfo(user_id: str):
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

    # Filtrar el DataFrame para el usuario dado como argumento
    user_data = merged_df[merged_df['user_id'] == user_id]

    # Calcular dinero gastado
    total_spent = round(user_data['price'].sum(), 2)


    # Calcular el porcentaje de recomendación
    total_items = user_data['item_id'].nunique()
    recommend_percentage = (user_data['recommend'].sum() / total_items) * 100

    # Crear el diccionario de resultados
    result = {
        "Usuario X": user_id,
        "Dinero gastado": f"{total_spent} USD",
        "porcentaje de recomendación": f"{recommend_percentage:.2f}%",
        "Cantidad de items": total_items
    }

    return result