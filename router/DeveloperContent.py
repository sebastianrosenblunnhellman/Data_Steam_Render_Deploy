import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa

def DeveloperContent(desarrollador: str):
    # Cargar los datos desde el archivo Parquet
    file_path = 'data/Developer.parquet'
    table = pq.read_table(file_path)
    df = table.to_pandas()
    
    # Filtrar el DataFrame por el desarrollador especificado
    filtered_df = df[df['Desarrollador'] == desarrollador]
    
    # Calcular la cantidad total de items por año y el porcentaje de contenido gratuito
    result = filtered_df.groupby('Año').agg({'Cantidad de Items': 'sum', 'Contenido Free': 'mean'}).reset_index()
    
    # Convertir los resultados a un diccionario en el formato deseado
    output = {
        'Año': result['Año'].tolist(),
        'Cantidad de Items': result['Cantidad de Items'].tolist(),
        'Contenido Free': result['Contenido Free'].tolist()
    }
    
    return output
