import pandas as pd
import matplotlib.pyplot as plt
import os

# Cargar datos
file_path = r"C:\Users\pablo\OneDrive - UFV\Cuarto Año\TFG\dana\merged\Datos_normalizados.csv"
data = pd.read_csv(file_path)

# Convertir la columna de tiempo a formato datetime
data['time'] = pd.to_datetime(data['time'])

# Establecer 'time' como índice
data.set_index('time', inplace=True)

# Reducir memoria si es necesario
data = data.astype('float32', errors='ignore')

# Variables que deseas analizar
sst_var = 'sst'          # Cambia si tu columna de SST tiene otro nombre
temperature_var = 't2m'  # Cambia si tu columna de temperatura tiene otro nombre
cape_var = 'cape'        # Cambia si tu columna de CAPE tiene otro nombre

# Manejar valores faltantes
for var in [sst_var, temperature_var, cape_var]:
    if var not in data.columns:
        raise ValueError(f"La columna '{var}' no se encuentra en el dataset.")
    data[var] = data[var].interpolate(method='linear')

# Crear carpeta para guardar gráficos
output_folder = r"C:\Users\pablo\OneDrive - UFV\Cuarto Año\TFG\dana\Graficos.py\Grafico_sst_temp_cape"
os.makedirs(output_folder, exist_ok=True)

# Estadísticas mensuales (promedio)
monthly_stats = data[[sst_var, temperature_var, cape_var]].resample('ME').mean()

# Crear gráfico de líneas
plt.figure(figsize=(14, 8))
plt.plot(monthly_stats.index.strftime('%m-%y'), monthly_stats[sst_var], label='SST Promedio', color='blue', linewidth=2)
plt.plot(monthly_stats.index.strftime('%m-%y'), monthly_stats[temperature_var], label='Temperatura Promedio', color='red', linewidth=2)
plt.plot(monthly_stats.index.strftime('%m-%y'), monthly_stats[cape_var], label='CAPE Promedio', color='purple', linewidth=2)

# Títulos y etiquetas
plt.title('Promedio Mensual de SST, Temperatura y CAPE', fontsize=16)
plt.xlabel('Mes-Año', fontsize=12)
plt.ylabel('Valores Normalizados', fontsize=12)
plt.xticks(rotation=90, fontsize=10)
plt.legend()
plt.grid(axis='y', alpha=0.5)
plt.tight_layout()

# Guardar gráfico
output_file = os.path.join(output_folder, 'sst_temp_cape_promedio_mensual.png')
plt.savefig(output_file)
plt.show()

print(f"Gráfico de SST, Temperatura y CAPE guardado en: {output_folder}")
