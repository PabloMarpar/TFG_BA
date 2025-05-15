import os
import xarray as xr
import pandas as pd


ruta_datos = r"C:\Users\pablo\OneDrive - UFV\Cuarto Año\TFG\dana\Datos_era5_2"
ruta_salida = r"C:\Users\pablo\OneDrive - UFV\Cuarto Año\TFG\dana\datos_transformados_pt1_COORDENADAS"
os.makedirs(ruta_salida, exist_ok=True)  

datos_por_dia = {}

# Procesar cada archivo .nc en la carpeta
for archivo in os.listdir(ruta_datos):
    if archivo.endswith(".nc"):
        ruta_archivo = os.path.join(ruta_datos, archivo)
        if not os.path.exists(ruta_archivo):
            print(f"Archivo no encontrado: {ruta_archivo}")
            continue
        
        try:
            #Abrir el archivo .nc usando xarray con cfgrib
            ds = xr.open_dataset(ruta_archivo, engine="cfgrib")
            df = ds.to_dataframe().reset_index()

            # Extraer la fecha del nombre del archivo y agrupar por día
            nombre_archivo = os.path.basename(archivo)
            fecha_str = "_".join(nombre_archivo.split('_')[2:5])  
            if fecha_str not in datos_por_dia:
                datos_por_dia[fecha_str] = []
            datos_por_dia[fecha_str].append(df)

        except Exception as e:
            print(f"Error al procesar el archivo {archivo}: {e}")

# Guardar CSV ordenados
for dia, dfs in datos_por_dia.items():
    df_dia = pd.concat(dfs)
    nombre_csv = os.path.join(ruta_salida, f"datos_{dia}.csv")
    df_dia.to_csv(nombre_csv, index=False)
    print(f"Archivo guardado: {nombre_csv}")
