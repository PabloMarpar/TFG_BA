import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configuración inicial
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# Ruta del archivo CSV
archivo_csv = r"C:\Users\pablo\OneDrive - UFV\Cuarto Año\TFG\dana\merged\ERA5_2012_2018.csv"

# Crear la carpeta para guardar los gráficos
output_folder = r"C:\Users\pablo\OneDrive - UFV\Cuarto Año\TFG\dana\img"
os.makedirs(output_folder, exist_ok=True)

# Leer solo el 5% de los datos
df = pd.read_csv(archivo_csv)

# Seleccionamos una muestra del 5% de los datos aleatoriamente
df_sample = df.sample(frac=0.50, random_state=42)

# Variable específica para el análisis (cape)
variable = 'cape'

# 1. Diagrama de caja solo para la variable 'cape'
plt.figure()
sns.boxplot(data=df_sample, y=variable, color='orange')
plt.title(f"Valores atípicos en {variable}")
plt.ylabel(variable)
plt.grid(axis='y')
plt.savefig(os.path.join(output_folder, f"outliers_{variable}.png"))
plt.close()

print("Gráfico descriptivo de 'cape' generado y guardado exitosamente.")
