import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Cargar datos
file_path = r"C:\Users\pablo\OneDrive - UFV\Cuarto Año\TFG\dana\merged\ERA5_2012_2018.csv"
data = pd.read_csv(file_path)

# Convertir la columna de tiempo a formato datetime
data['time'] = pd.to_datetime(data['time'])

# Establecer 'time' como índice
data.set_index('time', inplace=True)

# Crear una carpeta para guardar los gráficos
output_folder = r"C:\Users\pablo\OneDrive - UFV\Cuarto Año\TFG\dana\Graficos.py\Agrupacion_b"
os.makedirs(output_folder, exist_ok=True)

# Lista de variables a analizar
variables = ['sst', 'sp', 'cape', 'Wind Magnitude', 'Air-Sea Temp Difference']

### 4. Rosa de Viento ###
if 'u10' in data.columns and 'v10' in data.columns:
    from windrose import WindroseAxes
    wind_magnitude = (data['u10']**2 + data['v10']**2)**0.5
    wind_direction = (180 / 3.14159) * np.arctan2(data['v10'], data['u10'])
    ax = WindroseAxes.from_ax()
    ax.bar(wind_direction, wind_magnitude, normed=True, opening=0.8, edgecolor='white')
    ax.set_title('Rosa de Viento')
    plt.savefig(os.path.join(output_folder, 'rosa_viento.png'))
    plt.close()

### 2. Mapa de Calor (Heatmap) ###
correlation_matrix = data[['u10', 'v10', 't2m', 'sst', 'cape', 'Wind Magnitude', 'Air-Sea Temp Difference']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Mapa de Calor de Correlaciones')
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'heatmap.png'))
plt.close()

print(f"Gráficos generados y guardados en: {output_folder}")
