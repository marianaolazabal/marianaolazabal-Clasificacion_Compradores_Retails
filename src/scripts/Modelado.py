import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from datetime import datetime
from sklearn.preprocessing import MinMaxScaler
from kmodes.kprototypes import KPrototypes
import gc
import plotly.express as px
import requests
import io
import zipfile
from sklearn.cluster import KMeans
from funciones_generales import pathToData
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from yellowbrick.cluster import SilhouetteVisualizer
from sklearn.metrics import silhouette_score
import numpy as np
from sklearn.metrics import pairwise_distances_argmin_min
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#TIENE QUE QUEDARME UNA TABLA CON UNA LINEA POR CLIENTEEEEEE

# Leo el dataset que obtuve de limpiar los datos en el archivo limpieza_data.py
csv_path = pathToData()
df =pd.read_csv(csv_path + 'Data_Modelar.zip')

#Informacion generica del dataframe
df.info()

#K-Means

#Nos quedamos unicamente con las variables cuantitativas.

df.rename(columns={'Cantidades_Totales_Children\'s': 'Cantidades_Totales_Children'}, inplace=True)

def cambiarTipo(columnas):
    for col in columnas:
        if col in df.columns:
            df[col] = df[col].astype(int)
        else:
            print(f"Advertencia: La columna '{col}' no se encuentra en el DataFrame.")


# Lista de columnas que deseas convertir
columnas = [
    'Age', 'Suma_Total_Amount_log_Cliente', 'Cantidades_Totales_cliente',
    'Cantidades_Totales_Express',
    'Cantidades_Totales_Same-Day', 'Cantidades_Totales_Standard',
    'Cantidades_Totales_Average', 'Cantidades_Totales_Bad',
    'Cantidades_Totales_Excellent', 'Cantidades_Totales_Good',
    'Cash', 'Credit Card', 'Debit Card',
    'PayPal', 'frecuencia_comp_cliente', 'madrugada', 'mañana', 'medioDia',
    'noche', 'tarde', 'New', 'Premium', 'Regular',]
# Llama a la función con la lista de columnas
cambiarTipo(columnas)


def cambiarTipoCat(columnas_cat):
    for col in columnas_cat:
        if col in df.columns:
            df[col] = df[col].astype('category')
        else:
            print(f"Advertencia: La columna '{col}' no se encuentra en el DataFrame.")



columnas_cat = ['Country', 'Gender', 'Income', 'City_Moda_Cliente']
# Llama a la función con la lista de columnas
cambiarTipoCat(columnas_cat)


df_Kp=df.copy()

df_Kp.drop(columns=['Customer_ID'], inplace=True)

# Separar las características categóricas y numéricas
categorical_columns = ['Country', 'Gender', 'Income', 'City_Moda_Cliente']
categorical_features = df_Kp[categorical_columns]

numeric_features = df_Kp.drop(columns=categorical_columns)

# Convertir las características categóricas a índices numéricos
for col in categorical_columns:
    df_Kp[col] = pd.factorize(df_Kp[col])[0]

# Concatenar características numéricas y categóricas
features = df_Kp

# Crear el modelo K-Prototypes
kproto = KPrototypes(n_clusters=4, init='Cao', verbose=2)

# Ajustar el modelo
categorical_indices = [df_Kp.columns.get_loc(col) for col in categorical_columns]
clusters = kproto.fit_predict(features, categorical=categorical_indices)

# Añadir los resultados de cluster al DataFrame original
df_Kp['Cluster'] = clusters


df_Kp.head()


# Calcular el Silhouette Score
silhouette_avg = silhouette_score(df_Kp, clusters)
print(f'Silhouette Score: {silhouette_avg}')
