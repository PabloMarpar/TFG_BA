import pandas as pd

# Cargar el dataset
df = pd.read_csv(r"C:\Users\pablo\OneDrive - UFV\Cuarto Año\TFG\dana\merged\Datos_normalizados.csv")

# Reemplazar valores nulos en las columnas especificadas con 0
df[["sst", "Air-Sea Temp Difference"]] = df[["sst", "Air-Sea Temp Difference"]].fillna(0)

# Guardar el archivo corregido
df.to_csv(r"C:\Users\pablo\OneDrive - UFV\Cuarto Año\TFG\dana\merged\Datos_normalizados_corregido.csv", index=False)

print("Valores nulos reemplazados con 0 y archivo guardado correctamente.")
