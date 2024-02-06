import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa
import ast

def BestDeveloper(anio: int):
    # Cargar los datos desde el archivo Parquet
    file_path = 'data/Best_Developer_Year.parquet'
    table = pq.read_table(file_path)
    tabla_Best_Developer_Year = table.to_pandas()

    # Filtrar por anio
    data_anio = tabla_Best_Developer_Year[tabla_Best_Developer_Year['Anio'] == anio]

    # Obtener los desarrolladores para el anio dado
    if not data_anio.empty:
        desarrolladores = data_anio['Desarrolladores'].iloc[0]
        # Convertir la matriz numpy a lista de diccionarios
        desarrolladores = desarrolladores.tolist()
        desarrolladores = ast.literal_eval(str(desarrolladores))
        return [{"Puesto " + str(i+1): list(d.keys())[0]} for i, d in enumerate(desarrolladores)]
    else:
        return "No se encontraron datos para el anio especificado."