import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt
import os

# Ruta del archivo
file_path = r"C:\Users\pablo\OneDrive - UFV\Cuarto Año\TFG\dana\merged\ERA5_2012_2018.csv"

# Lista de variables a analizar
variables = ['msl', 't2m', 'd2m','sst', 'sp', 'cape']

# Crear una carpeta para guardar los gráficos
output_folder = r"C:\Users\pablo\OneDrive - UFV\Cuarto Año\TFG\dana\Graficos.py\img2"
os.makedirs(output_folder, exist_ok=True)

# Tamaño del chunk
chunk_size = 500000  # Número de filas por chunk

# Leer el archivo CSV en fragmentos y procesar
for chunk in pd.read_csv(file_path, chunksize=chunk_size):
    # Convertir la columna de tiempo a formato datetime
    chunk['time'] = pd.to_datetime(chunk['time'])

    # Establecer 'time' como índice
    chunk.set_index('time', inplace=True)

    # Reducir memoria si es necesario
    chunk = chunk.astype('float32', errors='ignore')

    # Descomponer cada variable y guardar resultados
    for var in variables:
        if var in chunk.columns:
            print(f"Descomponiendo {var}...")
            try:
                # Manejar valores faltantes (opción de interpolación)
                chunk[var] = chunk[var].interpolate(method='linear')

                # Ajustar periodo si los datos son diarios (ajustar el valor de period según la frecuencia de los datos)
                decomposition = seasonal_decompose(chunk[var], model='additive', period=365)

                # Graficar los componentes
                fig, axes = plt.subplots(4, 1, figsize=(10, 8), sharex=True)

                # Título
                fig.suptitle(f"Descomposición de {var}", fontsize=16)

                # Graficar los componentes: observación, tendencia, estacionalidad y residual
                axes[0].plot(decomposition.observed, label='Observado', color='blue')
                axes[0].set_ylabel('Observado')
                axes[0].legend()

                axes[1].plot(decomposition.trend, label='Tendencia', color='orange')
                axes[1].set_ylabel('Tendencia')
                axes[1].legend()

                axes[2].plot(decomposition.seasonal, label='Estacionalidad', color='green')
                axes[2].set_ylabel('Estacionalidad')
                axes[2].legend()

                axes[3].plot(decomposition.resid, label='Residual', color='red')
                axes[3].set_ylabel('Residual')
                axes[3].legend()

                # Ajustar el espacio entre los gráficos
                plt.tight_layout(rect=[0, 0, 1, 0.96])

                # Guardar gráfico
                plt.savefig(os.path.join(output_folder, f"{var}_decomposition.png"))
                plt.close(fig)

            except Exception as e:
                print(f"Error procesando {var}: {e}")
        else:
            print(f"Variable {var} no encontrada en los datos.")

print(f"Gráficos de descomposición guardados en: {output_folder}")
