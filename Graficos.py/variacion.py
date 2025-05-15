import pandas as pd
import matplotlib.pyplot as plt
import os

# Cargar datos
file_path = r"C:\Users\pablo\OneDrive - UFV\Cuarto Año\TFG\dana\merged\Datos_normalizados_corregido.csv" # Cambia esto con la ruta de tu archivo CSV
data = pd.read_csv(file_path)

# Convertir la columna de tiempo a formato datetime
data['time'] = pd.to_datetime(data['time'])

# Establecer 'time' como índice
data.set_index('time', inplace=True)

# Reducir memoria si es necesario
data = data.astype('float32', errors='ignore')

# Lista de variables a analizar
variables = ['t2m', 'sst', 'cape']  # Las variables que quieres analizar

# Crear una carpeta para guardar los gráficos (si es necesario)
output_folder = r"C:\Users\pablo\OneDrive - UFV\Cuarto Año\TFG\dana\Graficos.py\img"  # Cambia esta ruta si quieres un folder específico
os.makedirs(output_folder, exist_ok=True)

# Función para calcular el cambio porcentual anual
def calculate_yearly_change(df, var):
    # Agrupar por año y calcular el promedio de la variable
    yearly_avg = df.resample('Y')[var].mean()
    
    # Calcular el cambio porcentual entre años
    yearly_change = yearly_avg.pct_change() * 100  # Multiplicamos por 100 para obtener el porcentaje
    
    return yearly_avg, yearly_change

# Analizar las variables
for var in variables:
    if var in data.columns:
        print(f"Calculando cambio anual de {var}...")
        try:
            # Calcular el cambio porcentual anual
            yearly_avg, yearly_change = calculate_yearly_change(data, var)
            
            # Imprimir el cambio porcentual de cada año
            print(f"Cambio anual porcentual de {var}:")
            print(yearly_change)
            
            # Graficar los resultados
            plt.figure(figsize=(10, 6))
            plt.plot(yearly_avg.index, yearly_avg, label=f'{var} - Promedio Anual', marker='o')
            plt.title(f"Promedio Anual de {var} con Cambio Porcentual Anual")
            plt.xlabel('Año')
            plt.ylabel(f'{var}')
            plt.xticks(rotation=45)
            plt.legend()
            plt.grid(True)

            # Guardar gráfico
            plt.savefig(os.path.join(output_folder, f"{var}_yearly_change.png"))
            plt.close()
        except Exception as e:
            print(f"Error procesando {var}: {e}")
    else:
        print(f"Variable {var} no encontrada en los datos.")

print(f"Gráficos de cambios anuales guardados en: {output_folder}")
