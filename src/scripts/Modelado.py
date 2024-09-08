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


def cambiarTipo(columnas):
    for col in columnas:
        if col in df.columns:
            df[col] = df[col].astype(int)
        else:
            print(f"Advertencia: La columna '{col}' no se encuentra en el DataFrame.")



# Lista de columnas que deseas convertir
columnas = ['Suma_Total_Amount_log_Cliente', 'Cantidades_Totales_cliente', 'Cantidades_Totales_Standard',
            'Cantidades_Totales_Urgent-Delivery', 'Cantidades_Totales_Appliances', 'Cantidades_Totales_Audio',
            'Cantidades_Totales_Books', 'Cantidades_Totales_Clothing', 'Cantidades_Totales_Computer',
            'Cantidades_Totales_Food', 'Cantidades_Totales_Furniture', 'Cantidades_Totales_Games/Toys', 
            'Cantidades_Totales_Health/PersonalCare', 'Cantidades_Totales_Home_Decor', 'Cantidades_Totales_Home_Necessities', 
            'Cantidades_Totales_Shoes', 'Cantidades_Totales_Smart_Phone', 'Cantidades_Totales_Sports', 'Cantidades_Totales_TV',
            'Cantidades_Totales_Tools', 'Cash', 'Credit', 'Debit', 'frecuencia_comp_cliente', 'Invierno', 'Otoño', 'Primavera', 
            'Verano', 'madrugada', 'mañana', 'medioDia', 'noche', 'tarde']
# Llama a la función con la lista de columnas
cambiarTipo(columnas)


def cambiarTipoCat(columnas_cat):
    for col in columnas_cat:
        if col in df.columns:
            df[col] = df[col].astype('category')
        else:
            print(f"Advertencia: La columna '{col}' no se encuentra en el DataFrame.")



columnas_cat = ['City_Moda_Cliente', 'Gender', 'Income', 'Country', 'Satisfaction', 'Categoria_Edad']
# Llama a la función con la lista de columnas
cambiarTipoCat(columnas_cat)

df.rename(columns={'Suma_Total_Amount_log_Cliente': 'TotalHistorico_GastadoCliente'}, inplace=True)
df.rename(columns={'Cantidades_Totales_cliente': 'TotalHistorico_CompradoCliente'}, inplace=True)
df.rename(columns={'Cantidades_Totales_Games/Toys': 'Cantidades_Totales_Games_Toys'}, inplace=True)
df.rename(columns={'Cantidades_Totales_Health/PersonalCare': 'Cantidades_Totales_Health_PersonalCare'}, inplace=True)
pd.set_option('display.max_columns', None)
df.head()


df.drop(columns=['Customer_ID'], inplace=True)
df.drop(columns=['Cantidades_Totales_Appliances'], inplace=True)
df.drop(columns=['Cantidades_Totales_Audio'], inplace=True)
df.drop(columns=['Cantidades_Totales_Books'], inplace=True)
df.drop(columns=['Cantidades_Totales_Clothing'], inplace=True)
df.drop(columns=['Cantidades_Totales_Computer'], inplace=True)
df.drop(columns=['Cantidades_Totales_Food'], inplace=True)
df.drop(columns=['Cantidades_Totales_Furniture'], inplace=True)
df.drop(columns=['Cantidades_Totales_Games_Toys'], inplace=True)
df.drop(columns=['Cantidades_Totales_Health_PersonalCare'], inplace=True)
df.drop(columns=['Cantidades_Totales_Home_Decor'], inplace=True)
df.drop(columns=['Cantidades_Totales_Home_Necessities'], inplace=True)
df.drop(columns=['Cantidades_Totales_Shoes'], inplace=True)
df.drop(columns=['Cantidades_Totales_Smart_Phone'], inplace=True)
df.drop(columns=['Cantidades_Totales_Sports'], inplace=True)
df.drop(columns=['Cantidades_Totales_TV'], inplace=True)
df.drop(columns=['Cantidades_Totales_Tools'], inplace=True)



df_Kmeans=df.copy()

#sns.pairplot(df_Kmeans)
df_Kmeans.drop(columns=['City_Moda_Cliente'], inplace=True)
df_Kmeans.drop(columns=['Gender'], inplace=True)
df_Kmeans.drop(columns=['Income'], inplace=True)
df_Kmeans.drop(columns=['Country'], inplace=True)
df_Kmeans.drop(columns=['Satisfaction'], inplace=True)
df_Kmeans.drop(columns=['Cantidades_Totales_Standard'], inplace=True)
df_Kmeans.drop(columns=['Cantidades_Totales_Urgent-Delivery'], inplace=True)
df_Kmeans.drop(columns=['Cash'], inplace=True)
df_Kmeans.drop(columns=['Credit'], inplace=True)
df_Kmeans.drop(columns=['Debit'], inplace=True)
df_Kmeans.drop(columns=['Invierno'], inplace=True)
df_Kmeans.drop(columns=['Otoño'], inplace=True)
df_Kmeans.drop(columns=['Verano'], inplace=True)
df_Kmeans.drop(columns=['madrugada'], inplace=True)
df_Kmeans.drop(columns=['mañana'], inplace=True)
df_Kmeans.drop(columns=['medioDia'], inplace=True)
df_Kmeans.drop(columns=['noche'], inplace=True)
df_Kmeans.drop(columns=['tarde'], inplace=True)
df_Kmeans.drop(columns=['Categoria_Edad'], inplace=True)
df_Kmeans.drop(columns=['Primavera'], inplace=True)

df_Kmeans.head()


# Determinar el valor óptimo de k usando el método del codo
wcss = []  # Within-cluster sum of squares
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i,
                    init = "k-means++",
                    max_iter = 300,
                    random_state=42)
    kmeans.fit(df_Kmeans)
    wcss.append(kmeans.inertia_)

# Graficar el método del codo
plt.figure(figsize=(10, 8))
plt.plot(range(1, 11), wcss, marker='o', linestyle='--')
plt.title('Método del codo')
plt.xlabel('Número de clusters')
plt.ylabel('WCSS')
plt.show()


# Calcular el puntaje de Silhouette para diferentes números de clusters
range_n_clusters = [2,3]
silhouette_avg = []

for n_clusters in range_n_clusters:
    clusterer = KMeans(n_clusters=n_clusters, random_state=10)
    cluster_labels = clusterer.fit_predict(df_Kmeans)
    silhouette_avg.append(silhouette_score(df_Kmeans, cluster_labels))



# Visualizar los puntajes de Silhouette
plt.plot(range_n_clusters, silhouette_avg, marker='o')
plt.xlabel('Número de clusters')
plt.ylabel('Puntaje promedio de Silhouette')
plt.title('Puntaje de Silhouette para diferentes números de clusters')
plt.show()

#7


# Número óptimo de clusters basado en el análisis anterior

kmeans = KMeans(n_clusters=2, random_state=10)
cluster_labels = kmeans.fit_predict(df_Kmeans)



visualizer = SilhouetteVisualizer(kmeans, colors='yellowbrick')
visualizer.fit(df_Kmeans)
visualizer.poof()



# Obtener los centroides y las distancias al centroide más cercano
centroids = kmeans.cluster_centers_
closest, distances = pairwise_distances_argmin_min(df_Kmeans, centroids)

# Calcular la suma de las distancias al cuadrado para 3 clusters
sse_7 = np.sum(distances ** 2)
print(f'Suma de las distancias al cuadrado (SSE) para 3 clusters: {sse_7}')


df_Kmeans['Cluster'] = cluster_labels

df_Kmeans.head()


# Miramos cuántas observaciones quedaron en cada uno de los 4 clusters
cluster_sizes = np.bincount(kmeans.labels_)
print(cluster_sizes)

# Miramos los centroides de cada uno de los 3 clusters
cluster_centers = kmeans.cluster_centers_
print(cluster_centers)


# Agrupar por cluster y calcular estadísticas descriptivas
cluster_profiles = df_Kmeans.groupby('Cluster').describe()

# Mostrar el perfil de cada cluster
print(cluster_profiles)


cluster_profiles['Age'].head()

# Mostrar los datos específicos en cada cluster
for cluster in df_Kmeans['Cluster'].unique():
    print(f"Datos en el Cluster {cluster}:")
    print(df_Kmeans[df_Kmeans['Cluster'] == cluster])
    print("\n")



# K Prototipos

# Copiar el DataFrame original
df_Kp = df.copy()

df_Kp.drop(columns=['Cantidades_Totales_Standard'], inplace=True)
df_Kp.drop(columns=['Cantidades_Totales_Urgent-Delivery'], inplace=True)
df_Kp.drop(columns=['Cash'], inplace=True)
df_Kp.drop(columns=['Credit'], inplace=True)
df_Kp.drop(columns=['Debit'], inplace=True)
df_Kp.drop(columns=['Invierno'], inplace=True)
df_Kp.drop(columns=['Otoño'], inplace=True)
df_Kp.drop(columns=['Verano'], inplace=True)
df_Kp.drop(columns=['madrugada'], inplace=True)
df_Kp.drop(columns=['mañana'], inplace=True)
df_Kp.drop(columns=['medioDia'], inplace=True)
df_Kp.drop(columns=['noche'], inplace=True)
df_Kp.drop(columns=['tarde'], inplace=True)
df_Kp.drop(columns=['Primavera'], inplace=True)
df_Kp.drop(columns=['Age'], inplace=True)

df_Kp.head()

# Separar las características categóricas y numéricas
categorical_features = df_Kp[columnas_cat]
numeric_features = df_Kp.drop(columns=columnas_cat)

# Convertir las características categóricas a índices numéricos
for col in columnas_cat:
    df_Kp[col] = pd.factorize(df_Kp[col])[0]

# Convertir a array de numpy
data_array = df_Kp.values

# Definir el modelo K-Prototypes
kproto = KPrototypes(n_clusters=3, init='Huang', random_state=42)
categorical=[df_Kp.columns.get_loc(col) for col in columnas_cat]

# Ajustar el modelo
clusters = kproto.fit_predict(data_array, categorical=[df_Kp.columns.get_loc(col) for col in columnas_cat])

# Añadir las etiquetas de cluster al DataFrame original
df_Kp['cluster'] = clusters

# Calcular el Silhouette Score solo para las características numéricas
silhouette_avg = silhouette_score(numeric_features, clusters)
print(f'Silhouette Score: {silhouette_avg}')




















# Supongamos que df es tu DataFrame
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(x)


# Si necesitas volver a convertirlo a DataFrame
scaled_df = pd.DataFrame(scaled_data, columns=x.columns)

scaled_df.head()

# Convertir a array de numpy
data_array = features.values

# Definir el modelo K-Prototypes
kproto = KPrototypes(n_clusters=3, init='Huang', random_state=42)

# Ajustar el modelo
clusters = kproto.fit_predict(data_array, categorical=[0, 2]) #Indica las columnas categorias que son binarias (0 y 2)

# Añadir las etiquetas de cluster al DataFrame original
features['cluster'] = clusters













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
