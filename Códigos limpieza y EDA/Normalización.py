import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import os

# Ruta del archivo CSV
archivo_csv = r"C:\Users\pablo\OneDrive - UFV\Cuarto Año\TFG\dana\merged\ERA5_2012_2018.csv"

# Leer el CSV
df = pd.read_csv(archivo_csv)

# Eliminar las columnas 'latitude' y 'meanSea'
df = df.drop(columns=['latitude', 'meanSea'])

columnas_a_normalizar = ['u10', 'v10', 'd2m', 't2m', 'msl', 'sst', 'sp', 'cape', 'Wind Magnitude', 'Air-Sea Temp Difference']
scaler = MinMaxScaler()

# Normalizar las columnas seleccionadas
df[columnas_a_normalizar] = scaler.fit_transform(df[columnas_a_normalizar])
output_folder = "Normalizados"
os.makedirs(output_folder, exist_ok=True)

# Guardar el CSV con los datos normalizados
output_csv = os.path.join(output_folder, "Datos_normalizados.csv")
df.to_csv(output_csv, index=False)

print(f"Datos normalizados guardados en: {output_csv}")
