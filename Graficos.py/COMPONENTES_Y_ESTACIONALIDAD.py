import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose

# Ruta del archivo con los datos
file_path = r"C:\Users\pablo\OneDrive - UFV\Cuarto Año\TFG\dana\merged\ERA5_2012_2018.csv"

# Variables a analizar
variables = ['msl','t2m','d2m','u10','v10','sst', 'sp', 'cape', 'Wind Magnitude', 'Air-Sea Temp Difference']

# Carpeta para guardar los gráficos
output_folder = r"C:\Users\pablo\OneDrive - UFV\Cuarto Año\TFG\dana\Graficos.py\componentes2"
os.makedirs(output_folder, exist_ok=True)

# Cargar datos
df = pd.read_csv(file_path, parse_dates=['time'], index_col='time', date_format="%Y-%m-%d %H:%M:%S")

# Verificar cada variable
for variable in variables:
    if variable not in df.columns:
        print(f"La variable {variable} no está en el dataset, se omite.")
        continue

    # Interpolar NaN si es necesario
    df[variable] = df[variable].interpolate(method='linear')

    # Verificar si la serie es constante
    if df[variable].nunique() <= 1:
        print(f"La variable {variable} es constante. Se omite la prueba.")
        continue

    # Extraer una muestra de 100,000 valores para ADF
    serie = df[variable].dropna().tail(100000)

    if len(serie) < 12:
        print(f"La variable {variable} no tiene datos suficientes tras limpieza. Se omite.")
        continue

    # Prueba de estacionariedad ADF
    print(f"\nPrueba de estacionariedad para '{variable}'")
    resultado = adfuller(serie)

    print("Resultados de la Prueba Dickey-Fuller Aumentada:")
    print(f"Estadístico ADF: {resultado[0]}")
    print(f"p-valor: {resultado[1]}")
    print("Valores Críticos:")
    for clave, valor in resultado[4].items():
        print(f"   {clave}: {valor}")
    
    if resultado[1] <= 0.05:
        print(f"La variable '{variable}' es estacionaria (rechazamos H0).")
    else:
        print(f"La variable '{variable}' no es estacionaria (no rechazamos H0).")

    # Descomposición de la serie temporal (solo últimos 100,000 valores)
    if len(serie) >= 12:
        sample_series = serie.tail(100000)
        decomposition = seasonal_decompose(sample_series, model='additive', period=12)

        # Extraer componentes
        tendencia = decomposition.trend
        estacionalidad = decomposition.seasonal
        residuo = decomposition.resid

        # Graficar y guardar resultados
        fig, axes = plt.subplots(1, 4, figsize=(16, 4))
        fig.suptitle(f"Descomposición de '{variable}'", fontsize=14)

        axes[0].plot(sample_series, label='Serie Original', color='black')
        axes[0].set_title('Serie Original')

        axes[1].plot(tendencia, label='Tendencia', color='blue')
        axes[1].set_title('Tendencia')

        axes[2].plot(estacionalidad, label='Estacionalidad', color='green')
        axes[2].set_title('Estacionalidad')

        axes[3].plot(residuo, label='Ruido (Irregularidad)', color='red')
        axes[3].set_title('Ruido')

        plt.tight_layout(rect=[0, 0, 1, 0.95])
        output_path = os.path.join(output_folder, f"descomposicion_{variable}.png")
        plt.savefig(output_path)
        plt.close()

        print(f"Análisis completado para '{variable}'. Gráfico guardado en {output_path}\n")
