import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configuración inicial
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# Ruta del archivo CSV
archivo_csv = r"C:\Users\pablo\OneDrive - UFV\Cuarto Año\TFG\dana\merged\ERA5_2012_2018.csv"

# Crear la carpeta para guardar los gráficos
output_folder = r"C:\Users\pablo\OneDrive - UFV\Cuarto Año\TFG\dana\img2"
os.makedirs(output_folder, exist_ok=True)

# Leer solo el 5% de los datos
df = pd.read_csv(archivo_csv)

# Seleccionamos una muestra del 5% de los datos aleatoriamente
df_sample = df.sample(frac=0.10, random_state=42)

# Variables numéricas que necesitamos para el análisis
variables_numericas = ['u10', 'v10', 'd2m', 't2m', 'msl', 'sst', 'sp', 'cape', 'Wind Magnitude', 'Air-Sea Temp Difference']

# 1. Diagramas de dispersión entre las variables
for x in variables_numericas:
    for y in variables_numericas:
        if x != y:  # Evitar el gráfico de x vs x
            plt.figure()
            sns.scatterplot(data=df_sample, x=x, y=y, alpha=0.6)
            plt.title(f"Relación entre {x} y {y}")
            plt.xlabel(x)
            plt.ylabel(y)
            plt.grid()
            plt.savefig(os.path.join(output_folder, f"dispersión_{x}_vs_{y}.png"))
            plt.close()

# 2. Diagramas de caja para cada variable
for var in variables_numericas:
    plt.figure()
    sns.boxplot(data=df_sample, y=var, color='orange')
    plt.title(f"Valores atípicos en {var}")
    plt.ylabel(var)
    plt.grid(axis='y')
    plt.savefig(os.path.join(output_folder, f"outliers_{var}.png"))
    plt.close()

# 3. Tendencia entre 'cape' y otras variables (puedes personalizar esta parte según tus necesidades)
for var in variables_numericas:
    if var != 'cape':  # Evitar cape vs cape
        plt.figure()
        sns.regplot(data=df_sample, x=var, y='cape', scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
        plt.title(f"Tendencia entre {var} y cape")
        plt.xlabel(var)
        plt.ylabel("cape")
        plt.grid()
        plt.savefig(os.path.join(output_folder, f"tendencia_cape_{var}.png"))
        plt.close()

print("Gráficos descriptivos generados y guardados exitosamente.")
