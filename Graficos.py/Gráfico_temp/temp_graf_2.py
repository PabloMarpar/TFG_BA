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

# Variable de temperatura que deseas analizar
temperature_var = 't2m'

# Manejar valores faltantes en la temperatura
data[temperature_var] = data[temperature_var].interpolate(method='linear')

# Convertir temperaturas a grados Celsius (si estuvieran en Kelvin)
if data[temperature_var].max() > 100:  # Supongamos que >100 indica Kelvin
    data[temperature_var] = data[temperature_var] - 273.15

# Crear carpeta para guardar gráficos
output_folder = r"C:\Users\pablo\OneDrive - UFV\Cuarto Año\TFG\dana\Graficos_temp_individuales"
os.makedirs(output_folder, exist_ok=True)

# Estadísticas mensuales: mínimo y máximo
monthly_stats = data[temperature_var].resample('M').agg(['min', 'max'])
monthly_stats['month_year'] = monthly_stats.index.strftime('%m-%y')

# 1. Gráfico para temperaturas mínimas mensuales
plt.figure(figsize=(14, 8))
plt.bar(monthly_stats['month_year'], monthly_stats['min'], color='blue', alpha=0.7, label='Mínimo Mensual')
plt.title('Temperatura Mínima Mensual', fontsize=16)
plt.xlabel('Mes-Año', fontsize=12)
plt.ylabel('Temperatura Mínima (°C)', fontsize=12)
plt.xticks(rotation=90, fontsize=10)
plt.grid(axis='y', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'minima_mensual_temperatura.png'))
plt.show()

# 2. Gráfico para temperaturas máximas mensuales
plt.figure(figsize=(14, 8))
plt.bar(monthly_stats['month_year'], monthly_stats['max'], color='red', alpha=0.7, label='Máximo Mensual')
plt.title('Temperatura Máxima Mensual', fontsize=16)
plt.xlabel('Mes-Año', fontsize=12)
plt.ylabel('Temperatura Máxima (°C)', fontsize=12)
plt.xticks(rotation=90, fontsize=10)
plt.grid(axis='y', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'maxima_mensual_temperatura.png'))
plt.show()

print(f"Gráficos guardados en: {output_folder}")
