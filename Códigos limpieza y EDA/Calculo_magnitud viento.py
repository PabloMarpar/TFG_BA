import os
import pandas as pd
import numpy as np

# Directorios de entrada y salida
input_dir = r"C:\Users\pablo\OneDrive - UFV\Cuarto Año\TFG\dana\datos_transformados_pt1_COORDENADAS"
output_dir = r"C:\Users\pablo\OneDrive - UFV\Cuarto Año\TFG\dana\DATOS_NUEVAS_MAGINTUDES"
os.makedirs(output_dir, exist_ok=True)

# Función para calcular las nuevas magnitudes
def calculate_magnitudes(df):
    # Calcular la magnitud del viento
    if 'u10' in df.columns and 'v10' in df.columns:
        df['Wind Magnitude'] = np.sqrt(df['u10']**2 + df['v10']**2)
    else:
        raise ValueError("El archivo no contiene las columnas 'u10' y 'v10'.")
    
    # Calcular la diferencia de temperatura del aire y superficie
    if 't2m' in df.columns and 'sst' in df.columns:
        df['Air-Sea Temp Difference'] = df['t2m'] - df['sst']
    
    return df

# Procesar cada archivo en el directorio de entrada
for filename in os.listdir(input_dir):
    if filename.endswith(".csv"):
        # Ruta completa del archivo de entrada
        input_path = os.path.join(input_dir, filename)
        
        print(f"Procesando archivo: {filename}")
        try:
            data = pd.read_csv(input_path)
            
            # Calcular las nuevas magnitudes
            data = calculate_magnitudes(data)
        
            columns_to_remove = ['longitude', 'number', 'step', 'surface', 'valid_time', 'meansea']
            data = data.drop(columns=[col for col in columns_to_remove if col in data.columns], errors='ignore')
            output_filename = filename.replace('.csv', '_MAGNITUDNOM.csv').replace('nc_con_nombre', '')
            output_path = os.path.join(output_dir, output_filename)
            
            # Guardar los resultados en un nuevo archivo CSV
            data.to_csv(output_path, index=False)
            
            print(f"Archivo procesado y guardado en: {output_path}")
        except Exception as e:
            print(f"Error procesando {filename}: {e}")
