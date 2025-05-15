import pandas as pd

# Cargar el dataset
df = pd.read_csv(r"C:\Users\pablo\OneDrive - UFV\Cuarto Año\TFG\dana\merged\Datos_normalizados_corregido.csv")



print(df.head())  # Muestra las primeras filas
print(df.info())  # Ver tipos de datos y nulos
print(df.describe())  # Estadísticas generales
