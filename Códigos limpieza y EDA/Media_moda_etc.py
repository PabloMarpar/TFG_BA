import pandas as pd

# Ruta del archivo CSV
archivo_csv = r"C:\Users\pablo\OneDrive - UFV\Cuarto Año\TFG\dana\merged\Datos_normalizados_corregido.csv"
df = pd.read_csv(archivo_csv)


# Seleccionar variables numéricas
variables_numericas = df.select_dtypes(include=['float64', 'int64']).columns

# Calcular medidas de tendencia central y dispersión
medidas = pd.DataFrame(columns=['Media', 'Mediana', 'Moda', 'Rango', 'Varianza', 'Desviación Estándar'])

for var in variables_numericas:
    media = df[var].mean()
    mediana = df[var].median()
    moda = df[var].mode()[0]  
    rango = df[var].max() - df[var].min()
    varianza = df[var].var()
    desviacion_estandar = df[var].std()
    
    medidas.loc[var] = [media, mediana, moda, rango, varianza, desviacion_estandar]
print(medidas)
