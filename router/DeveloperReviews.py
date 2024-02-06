import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa

def DeveloperReviews(desarrolladora: str):
    # Cargar los datos desde el archivo Parquet
    file_path = 'data/Developer_Reviews.parquet'
    table = pq.read_table(file_path)
    df = table.to_pandas()
    
    # Filtrar el DataFrame para obtener las filas correspondientes a la desarrolladora proporcionada
    filtered_df = df[df['developer'] == desarrolladora]
    
    # Calcular la suma de las reseñas positivas y negativas
    total_negative = int(filtered_df['Negative'].sum())
    total_positive = int(filtered_df['Positive'].sum())
    
    # Crear el diccionario de retorno
    result = {
        desarrolladora: {
            "Negative": total_negative,
            "Positive": total_positive
        }
    }
    
    return result