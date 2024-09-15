import pandas as pd
import seaborn as sns # Visualización
import matplotlib.pyplot as plt
#from gapminder import gapminder # data set
#import squarify    # pip install squarify (algorithm for treemap)
import numpy as np
import plotly.express as px
from funciones_generales import pathToData



csv_path = pathToData()
data =pd.read_csv(csv_path + 'ClusterFinal_df.zip')

#Informacion generica del dataframe
data.info()

# Verificar si hay Customer_ID duplicados
duplicados = data[data.duplicated(subset='Customer_ID', keep=False)]
pd.set_option('display.max_columns', None)
# Mostrar las filas donde Customer_ID está duplicado
duplicados.head()

# Contar los registros de order_id distintos
num_clientes_ids = data['Customer_ID'].nunique()

print("Número de registros de order_id distintos:", num_clientes_ids)

data_analizar=data.drop_duplicates()

data_analizar.head()
data_analizar.size


cluster_summary = data.groupby('cluster').describe(include='all')
print(cluster_summary)

print('''El cluster 0 es el mas chico y tiene 51.320 observaciones, seguido por el cluster 1 que tiene 
      128.290 observaciones y por el ultimo, el cluster con mas observaciones es el 2 y presenta 132.561.
      El cluster 1 y el cluster 2 tienen muchos más datos que el cluster 0, lo que indica que son más 
      representativos en términos de cantidad de observaciones''')


cluster_summary['Country'].head()

print('''En el primer cluster se observa que la mayoria de los clientes estan concentrados en el pais 4.
      El cluster 1 y 2 por su lado tiene una mayor diversidad geografica.''')

cluster_summary['City_Moda_Cliente'].head()

print('La ciudades parecen ser mas diversas entre los clusters. Sera mejor estudiar la representacion grafica.')


cluster_summary['Income'].head()

print('''No hay representatividad de ingresos de nivel 1 en los cluster 1 y 2.
    El cluster 0 tiene ingresos más bajos en comparación con los otros dos clusters, lo que sugiere que agrupa a
    clientes de ingresos más modestos. Cluster 1 tiene el ingreso promedio más alto, lo que indica que agrupa a los 
    clientes de ingresos más altos.
    Cluster 0 tiene menos dispersión, lo que podría indicar que sus ingresos están más concentrados en un rango 
    más estrecho, lo cual refuerza la idea de que este grupo está compuesto por personas de ingresos más bajos 
    y menos variables.''')

# Analisis del cluster 0

df_cluster0_analisis = data_analizar[data_analizar['cluster'] == 0]
df_cluster0_analisis.head()

# Contar el número de transacciones por país y mes
df_counts = df_cluster0_analisis.groupby(['Country', 'City_Moda_Cliente']).size().reset_index(name='Customer_Count')

# Crear el gráfico sunburst
fig = px.sunburst(
    df_counts,
    path=['Country', 'City_Moda_Cliente'],
    values='Customer_Count',
    title='Distribución de clientes por País y Ciudad'
)

# Mostrar el gráfico
fig.show()


print('La mayoria de las personas que integran el cluster 0 son del pais 4, de la ciudad 87 y 37. Seguido por el pais 1, la ciudad 1')

#Gender

ax = sns.countplot(data=df_cluster0_analisis,x='Gender')
ax.tick_params(axis='x', rotation=90, size=7)

print('La mayoria de las personas que integran el cluster 0 son (gender) 0')

#Income

ax = sns.countplot(data=df_cluster0_analisis,x='Income')
ax.tick_params(axis='x', rotation=90, size=7)

print('El Income de las personas en el cluster 0 parece no ser determinante')

