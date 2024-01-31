import pandas as pd

def DeveloperFreeContent(desarrollador: str):
    # Ruta del archivo Parquet
    archivo_parquet = r'data/steam_games.parquet'

    # Leer el archivo Parquet en un DataFrame de Pandas
    df_steam_games = pd.read_parquet(archivo_parquet)

    df_developer_games = df_steam_games[df_steam_games["developer"] == desarrollador]
    df_free_developer_games = df_developer_games[df_developer_games["price"] == 0.00]

    grouped_data = df_developer_games.groupby("year")
    total_items = grouped_data["item_id"].nunique()
    free_items = df_free_developer_games.groupby("year")["item_id"].nunique()
    free_percentage = (free_items / total_items * 100).round(2)
    free_percentage = free_percentage.fillna(0)

    result_dict = {
        "Año": free_percentage.index.tolist(),
        "Cantidad de Items": total_items.tolist(),
        "Contenido Free": free_percentage.tolist()
    }

    return result_dict
