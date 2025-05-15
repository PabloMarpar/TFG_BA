import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Ruta del archivo
file_path = r"C:\Users\pablo\OneDrive - UFV\Cuarto Año\TFG\dana\merged\Datos_normalizados_corregido.csv"

# Cargar datos
data = pd.read_csv(file_path)

# Lista de variables a analizar
variables = ['msl', 't2m', 'd2m', 'u10', 'v10', 'sst', 'sp', 'cape', 'Wind Magnitude', 'Air-Sea Temp Difference']

# Filtrar el dataframe para incluir solo las variables seleccionadas
data_filtered = data[variables]

# Calcular la matriz de correlación
correlation_matrix = data_filtered.corr()

# Configurar el gráfico
plt.figure(figsize=(10, 8))
sns.set(font_scale=1.2)
sns.set_style("whitegrid")

# Crear el heatmap
ax = sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5, square=True)

# Ajustar el título y mostrar la figura
plt.title("Matriz de Correlación", fontsize=16)
plt.xticks(rotation=45, ha="right")
plt.yticks(rotation=0)
plt.tight_layout()

# Guardar la imagen en la carpeta de salida (opcional)
output_path = r"C:\Users\pablo\OneDrive - UFV\Cuarto Año\TFG\dana\Graficos.py\correlacion\correlation_matrix.png"
plt.savefig(output_path, dpi=300)

# Mostrar el gráfico
plt.show()
