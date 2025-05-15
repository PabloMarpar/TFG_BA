import pandas as pd

# Cargar el archivo CSV
file_path = r"C:\Users\pablo\OneDrive - UFV\Cuarto Año\TFG\dana\Datos_era5\datos_combinados.csv"
df = pd.read_csv(file_path)

# Eliminar las columnas
columns_to_remove = ['number', 'step', 'surface', 'meanSea']
df = df.drop(columns=columns_to_remove)

# Guardar el archivo sin las columnas eliminadas
output_path = r"C:\Users\pablo\OneDrive - UFV\Cuarto Año\TFG\dana\Datos_era5\datos_combinados_modificado.csv"
df.to_csv(output_path, index=False)

print("Las columnas se han eliminado y el archivo ha sido guardado.")
