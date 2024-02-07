import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa
import numpy as np

def user_item(user_id): 
    # Cargar los datos desde el archivo Parquet
    file_path = 'data/recomendacion_usuario.parquet'
    table = pq.read_table(file_path)
    predictions_df = table.to_pandas()

    # Cargar los datos desde el archivo Parquet
    file_path = 'data/title_finder.parquet'
    table = pq.read_table(file_path)
    title_finder = table.to_pandas()

    row = predictions_df[predictions_df['user_id'] == user_id]
    if not row.empty:
        top_5_ids = row['top_5_item_id'].iloc[0][:5]  # Obtenemos los primeros 5 elementos de la lista
        titles = []
        for id in top_5_ids:
            id = id.strip()  # Elimina espacios en blanco alrededor del item_id
            title_row = title_finder[title_finder['item_id'] == id]['title']
            if not title_row.empty:
                titles.append(title_row.iloc[0])
        return titles
    else:
        return "User ID not found"