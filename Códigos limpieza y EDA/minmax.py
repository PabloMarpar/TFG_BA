import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Ruta del archivo CSV
archivo_csv = r"C:\Users\pablo\OneDrive - UFV\Cuarto Año\TFG\dana\merged\ERA5_2012_2018.csv"

# Leer el CSV
df = pd.read_csv(archivo_csv)

# Eliminar las columnas 'latitude' y 'meanSea'
df = df.drop(columns=['latitude', 'meanSea'])

# Definir las columnas a normalizar
columnas_a_normalizar = ['u10', 'v10', 'd2m', 't2m', 'msl', 'sst', 'sp', 'cape', 'Wind Magnitude', 'Air-Sea Temp Difference']

# Calcular y mostrar los valores mínimos y máximos de cada columna
minimos = df[columnas_a_normalizar].min()
maximos = df[columnas_a_normalizar].max()

print("Valores mínimos de cada columna:")
print(minimos)

print("\nValores máximos de cada columna:")
print(maximos)