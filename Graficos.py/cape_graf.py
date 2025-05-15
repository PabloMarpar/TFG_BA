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

# Variable CAPE que deseas analizar
cape_var = 'cape'  # Cambia si tu columna tiene otro nombre

# Manejar valores faltantes en el CAPE
if cape_var not in data.columns:
    raise ValueError(f"La columna '{cape_var}' no se encuentra en el dataset.")
data[cape_var] = data[cape_var].interpolate(method='linear')

# Crear carpeta para guardar gráficos
output_folder = r"C:\Users\pablo\OneDrive - UFV\Cuarto Año\TFG\dana\Graficos.py\Grafico_cape"
os.makedirs(output_folder, exist_ok=True)

# Estadísticas mensuales (promedio)
monthly_cape = data[cape_var].resample('ME').mean()

# Crear gráfico mensual del CAPE
plt.figure(figsize=(14, 8))
plt.bar(monthly_cape.index.strftime('%m-%y'), monthly_cape, color='purple', alpha=0.7)
plt.title('Promedio Mensual del CAPE', fontsize=16)
plt.xlabel('Mes-Año', fontsize=12)
plt.ylabel('CAPE Promedio', fontsize=12)
plt.xticks(rotation=90, fontsize=10)
plt.grid(axis='y', alpha=0.5)
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'cape_promedio_mensual.png'))
plt.show()

print(f"Gráfico de CAPE guardado en: {output_folder}")
