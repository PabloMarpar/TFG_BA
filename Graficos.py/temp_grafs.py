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
output_folder = r"C:\Users\pablo\OneDrive - UFV\Cuarto Año\TFG\dana\Graficos.py\Gráfico_temp"
os.makedirs(output_folder, exist_ok=True)

# 1. Gráfico de media mensual de la temperatura
monthly_mean = data[temperature_var].resample('M').mean()

plt.figure(figsize=(14, 8))
plt.plot(monthly_mean.index.strftime('%m-%y'), monthly_mean, marker='o', color='orange', label='Media Mensual')
plt.title('Media Mensual de la Temperatura', fontsize=16)
plt.xlabel('Mes-Año', fontsize=12)
plt.ylabel('Temperatura (°C)', fontsize=12)
plt.xticks(rotation=90, fontsize=10)
plt.grid(alpha=0.5)
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'media_mensual_temperatura.png'))
plt.show()

# 2. Gráfico de mínimo y máximo mensual sin apilar
monthly_stats = data[temperature_var].resample('M').agg(['min', 'max'])
monthly_stats['month_year'] = monthly_stats.index.strftime('%m-%y')

x = range(len(monthly_stats))
plt.figure(figsize=(14, 8))
plt.bar([i - 0.2 for i in x], monthly_stats['max'], width=0.4, color='red', alpha=0.7, label='Máximo Mensual')
plt.bar([i + 0.2 for i in x], monthly_stats['min'], width=0.4, color='blue', alpha=0.7, label='Mínimo Mensual')
plt.title('Máximo y Mínimo Mensual de la Temperatura', fontsize=16)
plt.xlabel('Mes-Año', fontsize=12)
plt.ylabel('Temperatura (°C)', fontsize=12)
plt.xticks(x, monthly_stats['month_year'], rotation=90, fontsize=10)
plt.grid(axis='y', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'min_max_mensual_temperatura_no_apiladas.png'))
plt.show()

print(f"Gráficos guardados en: {output_folder}")
