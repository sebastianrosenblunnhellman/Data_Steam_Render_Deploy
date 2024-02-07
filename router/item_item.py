import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa
import numpy as np

def item_item(item_id : str):
    # Cargar los datos desde el archivo Parquet
    file_path = 'data/recomendacion_juego.parquet'
    table = pq.read_table(file_path)
    df = table.to_pandas()

    # Cargar los datos desde el archivo Parquet
    file_path = 'data/title_finder.parquet'
    table = pq.read_table(file_path)
    title_finder = table.to_pandas()

    row = df[df['item_id'] == item_id]
    if len(row) == 0:
        return None  # Si el item_id no está en el DataFrame, retorna None
    
    top_5_ids = row['top_5_item_id'].iloc[0].split(",")[:5]  # Divide los top_5_item_id y obtiene los primeros 5
    titles = []
    for id in top_5_ids:
        id = id.strip()  # Elimina espacios en blanco alrededor del item_id
        title_row = title_finder[title_finder['item_id'] == id]['title']
        if not title_row.empty:
            titles.append((id, title_row.iloc[0]))
    return titles
