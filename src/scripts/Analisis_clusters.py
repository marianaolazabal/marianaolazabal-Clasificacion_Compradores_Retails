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

df_Kp =pd.read_csv(csv_path + 'Data_Modelar.zip')


#Informacion generica del dataframe
data.info()
df_Kp['Categoria_Edad'].unique()

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

# Define the mapping
country_mapping = {
    0: 'Australia',
    1: 'United Kingdom',
    2: 'Canada',
    3: 'Germany',
    4: 'United States'
}


data_analizar = data_analizar.copy()

# Map the 'Country' column values to the new 'mapeo_country' column
data_analizar.loc[:, 'mapeo_country'] = data_analizar['Country'].map(country_mapping)

print('''En el primer cluster se observa que la mayoria de los clientes estan concentrados en el pais 4.
      El cluster 1 y 2 por su lado tiene una mayor diversidad geografica.''')

cluster_summary['City_Moda_Cliente'].head()

city_mapping={
    0:'Wollongong',
    1: 'Portsmouth',
    2: 'Leeds',
    3: 'Edinburgh',
    4: 'Belfast',
    5: 'Cardiff',
    6: 'Oxford',
    7: 'Manchester',
    8: 'Hull',
    9: 'Leicester',
    10: 'Liverpool',
    11: 'Nottingham',
    12: 'Brighton',
    13: 'Newcastle upon Tyne',
    14: 'Glasgow',
    15: 'Hamilton',
    16: 'Cairns',
    17: 'London',
    18: 'Quebec City',
    19: 'Adelaide',
    20: 'Townsville',
    21: 'Launceston',
    22: 'Melbourne',
    23: 'Toowoomba',
    24: 'Victoria',
    25: 'Regina',
    26: 'Kelowna',
    27: 'Frankfurt',
    28: 'Nürnberg',
    29: 'Hobart',
    30: 'Saskatoon',
    31: 'Bendigo',
    32: 'Kitchener',
    33: 'Duisburg',
    34: 'Birmingham',
    35: 'Geelong',
    36: 'Bielefeld',
    37: 'Boston',
    38: 'Halifax',
    39: 'Fort Worth',
    40: 'Atlanta',
    41: 'Dresden',
    42: 'Düsseldorf',
    43: 'Bochum',
    44: 'Dortmund',
    45: 'Bonn',
    46: 'Bremen',
    47: 'Berlin',
    48: 'Essen',
    49: 'Cologne',
    50: 'Canberra',
    51: 'Montréal',
    52: 'Sydney',
    53: 'Perth',
    54: 'Gold Coast',
    55: 'Darwin',
    56: 'Brisbane',
    57: 'Windsor',
    58: 'Barrie',
    59: 'Fresno',
    60: 'San Francisco',
    61: 'Winnipeg',
    62: 'Oshawa',
    63: 'Wuppertal',
    64: 'Southampton',
    65: 'Munich',
    66: 'Sheffield',
    67: 'Las Vegas',
    68: 'Albury',
    69: 'Ballarat',
    70: 'Houston',
    71: 'Calgary',
    72: 'Raleigh',
    73: 'Newcastle',
    74: 'Toronto',
    75: "St. John's",
    76: 'Kansas City',
    77: 'Leipzig',
    78: 'Stuttgart',
    79: 'Hannover',
    80: 'Münster',
    81: 'Hamburg',
    82: 'Mackay',
    83: 'Edmonton',
    84: 'Vancouver',
    85: 'Ottawa',
    86: 'Plymouth',
    87: 'Chicago',
    88: 'Phoenix',
    89: 'Tucson',
    90: 'Memphis',
    91: 'Bristol',
    92: 'Sacramento',
    93: 'Colorado Springs',
    94: 'Nashville',
    95: 'Virginia Beach',
    96: 'Louisville',
    97: 'Columbus',
    98: 'Austin',
    99: 'El Paso',
    100: 'Milwaukee',
    101: 'New York',
    102: 'Portland',
    103: 'Cleveland',
    104: 'Dallas',
    105: 'Oakland',
    106: 'Mesa',
    107: 'San Jose',
    108: 'Seattle',
    109: 'Charlotte',
    110: 'San Antonio',
    111: 'Miami',
    112: 'Baltimore',
    113: 'Minneapolis',
    114: 'New Orleans',
    115: 'San Diego',
    116: 'Wichita',
    117: 'Philadelphia',
    118: 'Indianapolis',
    119: 'Denver',
    120: 'Omaha',
    121: 'Oklahoma City',
    122: 'Washington',
    123: 'Detroit',
    124: 'Albuquerque',
    125: 'Arlington',
    126: 'Long Beach',
    127: 'Tulsa',
    128: 'Jacksonville',
    129: 'Los Angeles'

}

# Aplicar el mapeo de manera segura:
data_analizar.loc[:, 'mapeo_city'] = data_analizar['City_Moda_Cliente'].map(city_mapping)

print('La ciudades parecen ser mas diversas entre los clusters. Sera mejor estudiar la representacion grafica.')



cluster_summary['Income'].head()

income_mapping={
    0:'Medium',
    1: 'High',
    2: 'Low',
    3: 'Indeterminate'
}

data_analizar.loc[:,'mapeo_income']=data_analizar['Income'].map(income_mapping)


print('''No hay representatividad de ingresos de nivel 1 en los cluster 1 y 2.
    El cluster 0 tiene ingresos más bajos en comparación con los otros dos clusters, lo que sugiere que agrupa a
    clientes de ingresos más modestos. Cluster 1 tiene el ingreso promedio más alto, lo que indica que agrupa a los 
    clientes de ingresos más altos.
    Cluster 0 tiene menos dispersión, lo que podría indicar que sus ingresos están más concentrados en un rango 
    más estrecho, lo cual refuerza la idea de que este grupo está compuesto por personas de ingresos más bajos 
    y menos variables.''')


gender_mapping={
    0:'Male',
    1: 'Female',
    2: 'Indeterminate'
}

data_analizar.loc[:,'mapeo_gender']=data_analizar['Gender'].map(gender_mapping)



satisfaction_mapping={
    0:'Dissatisfied',
    1: 'Satisfied'
}

data_analizar.loc[:,'mapeo_satisfaction']=data_analizar['Satisfaction'].map(satisfaction_mapping)


df_Kp['Categoria_Edad'].unique()


categoria_Edad_mapping={
    0:'Adulto',
    1: 'Adulto_Mayor',
    2: 'Adulto_Joven',
    3: 'Joven',
    4: 'Veterano'
}

data_analizar.loc[:,'mapeo_Categoria_Edad']=data_analizar['Categoria_Edad'].map(categoria_Edad_mapping)


cluster_summary = data.groupby('cluster').describe(include='all')
print(cluster_summary)


print('''El cluster 0 es el mas chico y tiene 51.320 observaciones, seguido por el cluster 1 que tiene
      128.290 observaciones y por el ultimo, el cluster con mas observaciones es el 2 y presenta 132.561.
      El cluster 1 y el cluster 2 tienen muchos más datos que el cluster 0, lo que indica que son más
      representativos en términos de cantidad de observaciones''')


data_analizar.groupby('mapeo_country')['Country'].unique()

cluster_summary['Country'].head()

print('''En el primer cluster se observa que la mayoria de los clientes estan concentrados en el pais 4 (United States).
      El cluster 1 y 2 por su lado tiene una mayor diversidad geografica.''')

cluster_summary['City_Moda_Cliente'].head()

print('La ciudades parecen ser mas diversas entre los clusters. Sera mejor estudiar la representacion grafica.')

data_analizar.groupby('mapeo_income')['Income'].unique()

cluster_summary['Income'].head()

print('''No hay representatividad de ingresos de nivel 1 (High) en los cluster 1 y 2, por lo que se entiende que es un grupo de ingresos más modestos.''')

data_analizar.groupby('mapeo_gender')['Gender'].unique()

cluster_summary['Gender'].head()

print('''El cluster 0 y 1 tienen una alta representatividad del sexo Masculino. En el cluster 2 hay una mayor representatividad del sexo Femenino.''')

cluster_summary['TotalHistorico_GastadoCliente'].head()


print('''El cluster 0 presenta un promedio de gasto mayor al de los otros clusters, esto es consistente con los ingresos de los individuos que integran los clusters, como se vio en el analisis
        de ingresos, estos clusters no presentan representatividad de ingresos altos.
        El minimo gastado en este cluster es tambien mayor que en los otros clusters, lo mismo sucede con los quintiles y el maximo.
        El cluster 1 gasta mas que el 2 y las dispersion de los datos son muy parecidas. Se observa que el cluster''')


cluster_summary['TotalHistorico_CompradoCliente'].head()

print('''Al igual que el total gastado, la cantidad comprada por el cliente mantiene la misma relacion entre los cluster. Siendo el cluster 0 el que mas cantidades compra,
      seguido por el 1 y por ultimo el 2.''')

data_analizar.groupby('mapeo_satisfaction')['Satisfaction'].unique()

cluster_summary['Satisfaction'].head()

print('''La satisfaccion del cliente es igual para todos los clusters, por lo que no es una variable que aporte informacion para clasificar.''')

cluster_summary['frecuencia_comp_cliente'].head()

print('''Los clientes del cluster 0 compran con mayor frecuencia que los del cluster 1 y 2. Sin embargo, resulta interesante resaltar que el cluster 1, compra en promedio casi una unidad menos que
      el cluster 1, pero su desvio es menor y el grupo es mayor, esto podria indicar que si bien el cluster 1 ''')

data_analizar.groupby('mapeo_Categoria_Edad')['Categoria_Edad'].unique()

cluster_summary['Categoria_Edad'].head()

print('''En todos los clusters hay presencia de jovenes, en el cluster 2 tambien se ven adultos jovenes''')










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

