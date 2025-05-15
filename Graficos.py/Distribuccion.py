import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configuración inicial
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# Ruta del archivo CSV
archivo_csv = r"C:\Users\pablo\OneDrive - UFV\Cuarto Año\TFG\dana\merged\Datos_normalizados.csv"

# Crear la carpeta para guardar los gráficos
output_folder = r"C:\Users\pablo\OneDrive - UFV\Cuarto Año\TFG\dana\img2"
os.makedirs(output_folder, exist_ok=True)

# Leer solo el 5% de los datos
df = pd.read_csv(archivo_csv)

# Seleccionamos una muestra del 5% de los datos aleatoriamente
df_sample = df.sample(frac=0.05, random_state=42)

# Variables numéricas que necesitamos para el análisis
variables_numericas = ['u10', 'v10', 'd2m', 't2m', 'msl', 'sst', 'sp', 'cape', 'Wind Magnitude', 'Air-Sea Temp Difference']

# Creamos los gráficos por cada variable numérica
for var in variables_numericas:
    plt.figure()
    sns.histplot(df_sample[var], kde=True, bins=30, color='blue', alpha=0.6)
    plt.title(f"Distribución de {var}")
    plt.xlabel(var)
    plt.ylabel("Frecuencia")
    plt.grid(axis='y')
    
    # Guardar el gráfico en la ruta indicada
    plt.savefig(os.path.join(output_folder, f"distribucion_{var}.png"))
    plt.close()

print("Gráficos generados y guardados exitosamente.")
