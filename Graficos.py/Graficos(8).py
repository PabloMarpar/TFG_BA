import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configuración inicial
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# Ruta del archivo CSV
archivo_csv = r"C:\Users\pablo\OneDrive - UFV\Cuarto Año\TFG\dana\merged\ERA5_2012_2018.csv"

# Cargar solo el 20% de los datos
df = pd.read_csv(archivo_csv)
df = df.sample(frac=0.2, random_state=42)

# Crear la carpeta para guardar los gráficos
output_folder = "graficos"
os.makedirs(output_folder, exist_ok=True)

# 1. Distribución de cada variable numérica
variables_numericas = df.select_dtypes(include=['float64', 'int64']).columns
for var in variables_numericas:
    plt.figure()
    sns.histplot(df[var], kde=True, bins=30, color='blue', alpha=0.6)
    plt.title(f"Distribución de {var}")
    plt.xlabel(var)
    plt.ylabel("Frecuencia")
    plt.grid(axis='y')
    plt.savefig(os.path.join(output_folder, f"distribucion_{var}.png"))
    plt.close()

# 2. Correlaciones entre las variables
plt.figure(figsize=(10, 8))
correlaciones = df[variables_numericas].corr()
sns.heatmap(correlaciones, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Mapa de calor: Correlaciones entre variables")
plt.savefig(os.path.join(output_folder, "correlaciones_calor.png"))
plt.close()

# 3. Relación entre 'cape' y otras variables (verifica el nombre correcto)
if 'cape' in variables_numericas:  # Solo si 'cape' está en los datos
    for var in variables_numericas:
        if var != 'cape':  # Evitar cape vs cape
            plt.figure()
            sns.scatterplot(data=df, x=var, y='cape', alpha=0.5, color='green')
            plt.title(f"Relación entre {var} y cape")
            plt.xlabel(var)
            plt.ylabel("cape")
            plt.grid()
            plt.savefig(os.path.join(output_folder, f"relacion_cape_{var}.png"))
            plt.close()

# 4. Cajas para detectar valores atípicos (outliers)
for var in variables_numericas:
    plt.figure()
    sns.boxplot(data=df, y=var, color='orange')
    plt.title(f"Valores atípicos en {var}")
    plt.ylabel(var)
    plt.grid(axis='y')
    plt.savefig(os.path.join(output_folder, f"outliers_{var}.png"))
    plt.close()

# 5. Diagrama de dispersión para variables clave (pares relevantes)
pares_relevantes = [('t2m', 'meanSea'), ('sst', 'sp'), ('cape', 't2m')]
for x, y in pares_relevantes:
    if x in variables_numericas and y in variables_numericas:
        plt.figure()
        sns.scatterplot(data=df, x=x, y=y, alpha=0.6, hue='cape', palette='viridis')
        plt.title(f"Relación entre {x} y {y}")
        plt.xlabel(x)
        plt.ylabel(y)
        plt.grid()
        plt.savefig(os.path.join(output_folder, f"dispersión_{x}_vs_{y}.png"))
        plt.close()
