import pandas as pd
import os

# Ruta del archivo de coordenadas categorizadas
categorical_file = r"C:\Users\pablo\OneDrive - UFV\Cuarto Año\TFG\dana\Coordenadas_categorizadas.xlsx"
# Cargar las coordenadas categorizadas en un DataFrame
categorical_df = pd.read_excel(categorical_file)
ruta_salida = r"C:\Users\pablo\OneDrive - UFV\Cuarto Año\TFG\dana\datos_transformados_pt1_COORDENADAS"
os.makedirs(ruta_salida, exist_ok=True)  

categorical_df = categorical_df[['latitude', 'longitude', 'location_type']]

# procesar cada archivo CSV
def process_csv(file_path):
    csv_df = pd.read_csv(file_path)

    merged_df = pd.merge(csv_df, categorical_df, on=['latitude', 'longitude'], how='inner')
    merged_df = merged_df.rename(columns={'location_type': 'Nombre_loc'})
    cols = list(merged_df.columns)
    cols.insert(2, cols.pop(cols.index('Nombre_loc')))
    merged_df = merged_df[cols]
    
    nombre_archivo = os.path.basename(file_path)
    output_path = os.path.join(ruta_salida, f"{os.path.splitext(nombre_archivo)[0]}_con_nombre.csv")
    merged_df.to_csv(output_path, index=False)
    print(f"Archivo procesado guardado en: {output_path}")

csv_directory = r"C:\Users\pablo\OneDrive - UFV\Cuarto Año\TFG\dana\datos_transformados_pt1"

# Procesar todos los archivos CSV en la carpeta
for csv_file in os.listdir(csv_directory):
    if csv_file.endswith('.csv'):
        process_csv(os.path.join(csv_directory, csv_file))
