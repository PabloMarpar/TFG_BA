import requests
import pandas as pd
import time
import os

input_file = r"C:\Users\pablo\OneDrive - UFV\Cuarto Año\TFG\dana\Coordenadas.xlsx"
output_file = r"C:\Users\pablo\OneDrive - UFV\Cuarto Año\TFG\dana\Coordenadas_categorizadas.xlsx"
df = pd.read_excel(input_file)

# Dividir los datos en partes para evitar el bloqueo
chunk_size = 50  
chunks = [df[i:i + chunk_size] for i in range(0, df.shape[0], chunk_size)]

def get_autonomous_community(latitude, longitude):
    url = f"https://nominatim.openstreetmap.org/reverse?lat={latitude}&lon={longitude}&format=json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        address = data.get('address', {})
        
        if 'ocean' in address or 'sea' in address:
            return 'MAR'
        elif 'state' in address:
            return address['state']
        else:
            return 'DESCONOCIDO'
    else:
        return 'ERROR'
results = []

for idx, chunk in enumerate(chunks):
    print(f"Procesando lote {idx + 1}/{len(chunks)}...")

    #función de geocodificación
    chunk['location_type'] = chunk.apply(
        lambda row: get_autonomous_community(row['latitude'], row['longitude']), axis=1
    )
    results.append(chunk)
    time.sleep(1)

# Concatenar los resultados y guardar en un archivo Excel
final_df = pd.concat(results, ignore_index=True)
final_df.to_excel(output_file, index=False)

print("Proceso completado. Resultados guardados en:", output_file)
