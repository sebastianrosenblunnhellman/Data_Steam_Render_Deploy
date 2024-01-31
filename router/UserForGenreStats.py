import pandas as pd


def UserForGenreStats(genero: str):
    # Ruta de los archivos Parquet
    games_parquet = r'data\steam_games.parquet'
    items_parquet = r'data\users_items.parquet'

    # Leer los archivos Parquet en DataFrames de Pandas
    df_steam_games = pd.read_parquet(games_parquet)
    df_users_items = pd.read_parquet(items_parquet)

    # Unir los DataFrames utilizando la columna "item_id" como clave común
    merged_df = pd.merge(df_steam_games, df_users_items, on='item_id', how='inner')

    # Filtrar por género
    genre_data = merged_df[merged_df['genres'].apply(lambda x: genero in x)]

    # Agrupar por usuario y año, sumar las horas jugadas
    user_hours_by_year = genre_data.groupby(['user_id', 'year'])['playtime_forever'].sum().reset_index()

    # Encontrar al usuario con más horas jugadas
    max_hours_user = user_hours_by_year.groupby('user_id')['playtime_forever'].sum().idxmax()

    # Filtrar los datos del usuario con más horas jugadas
    max_hours_user_data = user_hours_by_year[user_hours_by_year['user_id'] == max_hours_user]

    # Convertir los resultados a formato JSON
    result = {
        "Usuario con más horas jugadas para " + genero: max_hours_user,
        "Horas jugadas": max_hours_user_data[['year', 'playtime_forever']].to_dict(orient='records')
    }

    return result
