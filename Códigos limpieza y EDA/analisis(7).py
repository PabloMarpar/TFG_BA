import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Cargar el archivo CSV
directorio = r"C:\Users\pablo\OneDrive - UFV\Cuarto Año\TFG\dana\merged"
archivo_csv = os.path.join(directorio, "Datos_normalizados.csv")

# Leer el CSV
df = pd.read_csv(archivo_csv)

# Análisis básico
print("Número de observaciones:", df.shape[0])
print("Número de variables:", df.shape[1])
print("\nTipos de datos de cada variable:")
print(df.dtypes)
print("\nPrimeras filas del dataset:")
print(df.head())

