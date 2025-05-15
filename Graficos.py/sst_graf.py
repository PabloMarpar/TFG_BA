import pandas as pd
import matplotlib.pyplot as plt
import os

# Cargar datos
file_path = r"C:\Users\pablo\OneDrive - UFV\Cuarto Año\TFG\dana\merged\ERA5_2012_2018.csv"
data = pd.read_csv(file_path)

# Convertir la columna de tiempo a formato datetime
data['time'] = pd.to_datetime(data['time'])

# Establecer 'time' como índice
data.set_index('time', inplace=True)

# Reducir memoria si es necesario
data = data.astype('float32', errors='ignore')

# Variable de SST que deseas analizar
sst_var = 'sst'  # Cambia esto si tu columna tiene otro nombre

# Manejar valores faltantes en la SST
if sst_var not in data.columns:
    raise ValueError(f"La columna '{sst_var}' no se encuentra en el dataset.")

data[sst_var] = data[sst_var].interpolate(method='linear')

# Convertir temperaturas a grados Celsius si estuvieran en Kelvin
if data[sst_var].max() > 100:  # Supongamos que >100 indica Kelvin
    data[sst_var] = data[sst_var] - 273.15

# Crear carpeta para guardar gráficos
output_folder = r"C:\Users\pablo\OneDrive - UFV\Cuarto Año\TFG\dana\Graficos.py\Graficos_sst"
os.makedirs(output_folder, exist_ok=True)

# Estadísticas mensuales: mínimo y máximo
monthly_stats = data[sst_var].resample('M').agg(['min', 'max'])
monthly_stats['month_year'] = monthly_stats.index.strftime('%m-%y')

# 1. Gráfico para SST mínima mensual
plt.figure(figsize=(14, 8))
plt.bar(monthly_stats['month_year'], monthly_stats['min'], color='blue', alpha=0.7, label='Mínimo Mensual')
plt.title('SST Mínima Mensual', fontsize=16)
plt.xlabel('Mes-Año', fontsize=12)
plt.ylabel('SST Mínima (°C)', fontsize=12)
plt.xticks(rotation=90, fontsize=10)
plt.grid(axis='y', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'minima_mensual_sst.png'))
plt.show()

# 2. Gráfico para SST máxima mensual
plt.figure(figsize=(14, 8))
plt.bar(monthly_stats['month_year'], monthly_stats['max'], color='red', alpha=0.7, label='Máximo Mensual')
plt.title('SST Máxima Mensual', fontsize=16)
plt.xlabel('Mes-Año', fontsize=12)
plt.ylabel('SST Máxima (°C)', fontsize=12)
plt.xticks(rotation=90, fontsize=10)
plt.grid(axis='y', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'maxima_mensual_sst.png'))
plt.show()

print(f"Gráficos de SST guardados en: {output_folder}")
