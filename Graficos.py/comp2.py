import pandas as pd
import numpy as np
from statsmodels.tsa.seasonal import STL

# Ruta del archivo CSV
ruta_csv = r"C:\Users\pablo\OneDrive - UFV\Cuarto Año\TFG\dana\merged\ERA5_2012_2018.csv"

# Cargar los datos
data = pd.read_csv(ruta_csv, parse_dates=['time'])  # Asegurar que 'time' es datetime
data.set_index('time', inplace=True)  # Usar 'time' como índice

# Variables a analizar
variables = ['msl', 't2m', 'd2m', 'u10', 'v10', 'sst', 'sp', 'cape', 'Wind Magnitude', 'Air-Sea Temp Difference']

# Diccionario para guardar las tendencias en % por año
tendencias_porcentaje = {}

for var in variables:
    if var in data.columns:
        # Descomponer la serie con STL (asumiendo datos diarios, period=365)
        serie = data[var].dropna()
        stl = STL(serie, period=365, robust=True)
        resultado = stl.fit()
        
        # Extraer la tendencia
        trend = resultado.trend
        
        # Convertir el tiempo a "días desde el inicio"
        x = (trend.index - trend.index[0]).days
        
        # Ajustar una recta (y = m*x + b) sobre la tendencia
        slope, intercept = np.polyfit(x, trend.values, 1)
        
        # Convertir la pendiente a "por año"
        slope_year = slope * 365
        
        # Expresar en porcentaje respecto a la media de la tendencia
        media_trend = trend.mean()
        slope_percent = (slope_year / media_trend) * 100
        
        # Guardamos el resultado
        tendencias_porcentaje[var] = slope_percent
    else:
        print(f"La variable '{var}' no existe en el DataFrame.")

# Mostrar resultados
for var, valor in tendencias_porcentaje.items():
    print(f"Tendencia anual de {var}: {valor:+.2f}%")
