import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa

def UserInfo(user_id: str):
    file_path = 'data/UserData.parquet'
    table = pq.read_table(file_path)
    user_data = table.to_pandas()
    
    user_info = user_data[user_data['Usuario X'] == user_id].to_dict(orient='records')
    
    if user_info:
        return user_info[0]
    else:
        return f"No se encontraron datos para el usuario con ID: {user_id}"