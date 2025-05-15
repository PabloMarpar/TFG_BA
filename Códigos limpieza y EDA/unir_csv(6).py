import os
import pandas as pd
import re

# Directorio donde están los archivos CSV
directorio = r"C:\Users\pablo\OneDrive - UFV\Cuarto Año\TFG\dana\DATOS_NUEVAS_MAGINTUDES"

# Crear un directorio llamado "merged" para guardar el archivo final
directorio_merged = os.path.join(directorio, "merged")
os.makedirs(directorio_merged, exist_ok=True)

# Crear una lista para almacenar los DataFrames
dataframes = []

# Expresión regular para identificar archivos con el patrón específico
patron = re.compile(r'^datos_\d{4}_\d{2}_\d{2}\._MAGNITUDNOM\.csv$')

# Recorrer todos los archivos en el directorio
for archivo in os.listdir(directorio):
    if archivo.endswith(".csv") and patron.match(archivo):  # Filtrar por el patrón
        ruta = os.path.join(directorio, archivo)
        # Leer el archivo CSV y añadirlo a la lista
        df = pd.read_csv(ruta)
        dataframes.append(df)

# Verificar si hay DataFrames antes de combinar
if dataframes:
    # Combinar todos los DataFrames en uno solo
    df_combinado = pd.concat(dataframes, ignore_index=True)

    # Guardar el archivo combinado en el directorio "merged"
    ruta_salida = os.path.join(directorio_merged, "ERA5_2012_2018.csv")
    df_combinado.to_csv(ruta_salida, index=False)

    print(f"Archivos combinados exitosamente. Archivo guardado en: {ruta_salida}")
else:
    print("No se encontraron archivos que coincidan con el patrón especificado.")
