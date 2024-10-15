import pandas as pd
import seaborn as sns # Visualización
import matplotlib.pyplot as plt
#from gapminder import gapminder # data set
#import squarify    # pip install squarify (algorithm for treemap)
import numpy as np
import plotly.express as px
from funciones_generales import pathToData
from plots import plot_bar_graphs, grafico_Histograma


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

cluster_summary['Country'].head()

print('''En el primer cluster se observa que la mayoria de los clientes estan concentrados en el pais United States.
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
    El cluster 0 tiene ingresos altos en comparación con los otros dos clusters, lo que sugiere que agrupa a
    clientes de ingresos menos modestos.''')

cluster_summary['Gender'].head()

gender_mapping={
    0:'Male',
    1: 'Female',
    2: 'Indeterminate'
}

data_analizar.loc[:,'mapeo_gender']=data_analizar['Gender'].map(gender_mapping)

print('''Se observa que no hay representatividad de Indeterminados en el cluster 2, es decir, los clientes del cluster son
      unicamente hombres y mujeres.
      El cluster 0 y 1 son en mayoria Hombres y en ambos hay representatividad de clientes cuyo genero no ha sido
      identificado.''')


cluster_summary['Satisfaction'].head()

satisfaction_mapping={
    0:'Dissatisfied',
    1: 'Satisfied'
}

data_analizar.loc[:,'mapeo_satisfaction']=data_analizar['Satisfaction'].map(satisfaction_mapping)

print('''No hay una clara diferenciación de satisfaccion entre los clusters.''')


cluster_summary['Categoria_Edad'].head()

df_Kp['Categoria_Edad'].unique()


categoria_Edad_mapping={
    0:'Adulto',
    1: 'Adulto_Mayor',
    2: 'Adulto_Joven',
    3: 'Joven',
    4: 'Veterano'
}

data_analizar.loc[:,'mapeo_Categoria_Edad']=data_analizar['Categoria_Edad'].map(categoria_Edad_mapping)

print('''En todos los clusters hay presencia de jovenes, en el cluster 2 tambien se ven adultos jovenes''')

cluster_summary = data.groupby('cluster').describe(include='all')
print(cluster_summary)


print('''El cluster 0 es el mas chico y tiene 51.320 observaciones, seguido por el cluster 1 que tiene
      128.290 observaciones y por el ultimo, el cluster con mas observaciones es el 2 y presenta 132.561.
      El cluster 1 y el cluster 2 tienen muchos más datos que el cluster 0, lo que indica que son más
      representativos en términos de cantidad de observaciones''')


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

print('''Los clientes del cluster 0 compran con mayor frecuencia que los del cluster 1 y 2. Sin embargo, resulta interesante resaltar que el cluster 1,
    compra en promedio casi una unidad menos que
    el cluster 1, pero su desvio es menor y el grupo es mayor, esto podria indicar que si bien el cluster 1 presenta clientes que compran menos, 
    desarrollar productos que incentiven a este grupo a consumir en mayor frecuencia podria ser mas eficiente que concentrar esfuerzos en el cluster 0.''')



# La mayoria de los clientes del cluster estan concentrados en el pais United States
# El cluster 0 tiene ingresos más altos en comparación con los otros dos clusters, lo que sugiere que agrupa a
# clientes de ingresos menos modestos.
# Hay mas hombres que mujeres pero hay representatividad de clientes cuyo genero no ha sido identificado
# Alta representatividad de grupos Jovenes
# El cluster 0 presenta un promedio de gasto mayor al de los otros clusters, esto es consistente con los ingresos de los individuos que integran los clusters
# Los clientes del cluster 0 compran con mayor frecuencia

# Analisis del cluster 0

df_cluster0_analisis = data_analizar[data_analizar['cluster'] == 0]
df_cluster0_analisis.head()

# La mayoria de los clientes del cluster estan concentrados en el pais United States
# Estudio de las caracteristicas de USA

df_cluster0_analisis_USA=df_cluster0_analisis[df_cluster0_analisis['mapeo_country']=='United States']
df_cluster0_analisis_USA.head()

#Gender and Income
#El gráfico muestra la distribución del porcentaje de gasto total de los clientes dentro de cada grupo de ingreso, desglosado por género


df_grouped = df_cluster0_analisis.groupby(['mapeo_income', 'mapeo_gender'])['TotalHistorico_GastadoCliente'].sum().reset_index()

# Agrupamos los datos en función de la columna mapeo_income, lo que significa que estamos creando grupos de clientes 
# que tienen el mismo nivel de ingresos.
# Dentro de cada grupo, estamos seleccionando la columna TotalHistorico_GastadoCliente, que contiene el total gastado 
# por los clientes en ese grupo.
# El método transform() aplica una operación a cada grupo de forma que se conserva el tamaño original del DataFrame.
# función anónima (lambda) que toma los valores de gasto dentro de un grupo (representados por x), calcula el total 
# del gasto en ese grupo (x.sum()) y luego divide cada valor individual dentro del grupo por ese total. 
# Finalmente, multiplicamos por 100 para obtener un porcentaje.

df_grouped['porcentaje_gasto'] = df_grouped.groupby('mapeo_income')['TotalHistorico_GastadoCliente'].transform(lambda x: x / x.sum() * 100)

# Crear el gráfico
plt.figure(figsize=(10, 6))
sns.barplot(x='mapeo_income', y='porcentaje_gasto', hue='mapeo_gender', data=df_grouped)

plt.title('Porcentaje del Gasto Total por Grupo de Ingreso y Género')
plt.ylabel('Porcentaje del Gasto Total Dentro de cada Grupo de Ingreso')
plt.xlabel('Grupo de Ingreso')
plt.legend(title='Género')
plt.show()

#Los porcentajes indican qué fracción del gasto total en cada grupo es atribuible a los diferentes géneros.
#El gráfico sugiere que, en todos los grupos de ingresos, los hombres tienen una participación significativamente mayor en el gasto total, especialmente en los grupos de ingresos bajos, medios e indeterminados. Las mujeres tienen una menor participación en todos los grupos de ingresos, mientras que el género indeterminado contribuye con el menor porcentaje en general.
#Dado que los hombres representan la mayor parte del gasto en todos los grupos de ingresos, especialmente en los segmentos de ingresos bajos, medios e indeterminados, las campañas de marketing podrían orientarse más hacia este público.
#Ofrecer productos y promociones que se alineen con las preferencias de este grupo sería una estrategia clave, ya que tienen una mayor propensión a gastar.
#Un enfoque de personalización en el sitio web, mostrando diferentes productos o promociones en función del género del cliente (si se dispone de esta información), podría mejorar la experiencia del usuario y potencialmente aumentar las conversiones de las mujeres.
# El porcentaje de gasto del género indeterminado es bajo en comparación con los hombres y mujeres en todos los grupos de ingresos. Esto podría indicar que el sitio web no está siendo lo suficientemente inclusivo o atractivo para este grupo.
#Se podría considerar realizar mejoras en la usabilidad del sitio, asegurándose de que sea inclusivo para personas de todos los géneros, lo que podría incluir ajustes en el lenguaje, las opciones de género en los formularios de registro o la representación de productos y modelos diversos.
#Estrategias como opciones de financiamiento, descuentos por volumen, o promociones de productos esenciales podrían resonar mejor con estos segmentos, maximizando el valor por cliente en estos grupos.
#Ofertas como ventas flash, recomendaciones de productos relacionadas, y envíos rápidos o gratuitos podrían aumentar las conversiones y los ingresos.
#Dado que los hombres son los principales consumidores en todos los grupos, un programa de fidelización dirigido a ellos podría ser muy efectivo. Esto podría incluir recompensas por compras frecuentes, descuentos personalizados o membresías exclusivas para mantener a estos consumidores comprometidos con la plataforma.
#Las ofertas pueden incluir productos exclusivos, tecnologías de punta, artículos de lujo, y envíos rápidos o gratuitos.
#En lugar de campañas exclusivas para hombres o mujeres, se pueden crear campañas neutras de género que apelen a una audiencia más amplia y diversa.

df_cluster0_analisis.head()
# 1. Contar el número de personas por país y categoría de edad
df_counts = df_cluster0_analisis.groupby(['mapeo_country', 'mapeo_Categoria_Edad']).size().reset_index(name='Group_Count')

# 2. Calcular el total de personas por país
df_totals = df_cluster0_analisis.groupby('mapeo_country').size().reset_index(name='Total')

# 3. Unir los dos DataFrames para calcular los porcentajes
df_counts = pd.merge(df_counts, df_totals, on='mapeo_country')

# 4. Calcular el porcentaje para cada categoría dentro del país
df_counts['Percentage'] = (df_counts['Group_Count'] / df_counts['Total']) * 100

# Crear el gráfico sunburst
fig = px.sunburst(
    df_counts,
    path=['mapeo_country', 'mapeo_Categoria_Edad'],
    values='Percentage',
    title='Distribución de Edades por País'
)

# Ajustar el tamaño del gráfico
fig.update_layout(
    autosize=False,
    width=1000,  # Ajusta el ancho según tus necesidades
    height=800   # Ajusta la altura según tus necesidades
)

# Mostrar el gráfico
fig.show()


print('''Se observa una alta representatividad de la categoría "Joven", en todos los países. Siendo en Alemania, 
      Reino Unido, Estados Unidos y Australia una significativa proporción de los clientes que se encuentran en estos 
      países.
      Las estrategias de marketing y ofertas para estos países deberían incluir productos orientados a consumidores 
      jóvenes. Entre estos podría considerarse productos de tecnología, ropa de moda y otros; más adelante en el análisis
      se estudiará los productos más comprados por este grupo.
      Canadá y Australia tienen una distribución más balanceada entre las categorías "Joven", "Adulto Joven" y "Adulto", 
      lo que indica que las campañas en estos países .
      Algunos países, como Alemania, Canadá y Australia, tienen una notable proporción de "Adulto Joven" y "Adulto". 
      Las estrategias de marketing deben diversificarse para diferentes segmentos etarios. Considerar productos que
      productos sean de interés para clientes jóvenes como también productos dirigidos a personas de más edad. 
      Algunos ejemplos podrían ser, electrodomésticos, productos de salud y bienestar, entre otros.
      ''')


#ver los productos comprados por nivel de ingreso

df_cluster0_analisis.head()
#Cantidades_Totales_Appliances, Cantidades_Totales_Audio, Cantidades_Totales_Books, Cantidades_Totales_Clothing	
# Cantidades_Totales_Computer, Cantidades_Totales_Food, Cantidades_Totales_Furniture, Cantidades_Totales_Games_Toys	
# Cantidades_Totales_Health_PersonalCare, Cantidades_Totales_Home_Decor, Cantidades_Totales_Home_Necessities	
# Cantidades_Totales_Shoes, Cantidades_Totales_Smart_Phone, Cantidades_Totales_Sports, Cantidades_Totales_TV	
# Cantidades_Totales_Tools


sns.violinplot(x=df_cluster0_analisis["mapeo_income"], y=df_cluster0_analisis["Cantidades_Totales_Appliances"])


df_cluster0_analisis_jovenes=df_cluster0_analisis[df_cluster0_analisis['mapeo_Categoria_Edad']=='Joven']


categorias = [
    'Cantidades_Totales_Appliances', 'Cantidades_Totales_Audio', 'Cantidades_Totales_Books', 
    'Cantidades_Totales_Clothing', 'Cantidades_Totales_Computer', 'Cantidades_Totales_Food', 
    'Cantidades_Totales_Furniture', 'Cantidades_Totales_Games_Toys', 
    'Cantidades_Totales_Health_PersonalCare', 'Cantidades_Totales_Home_Decor', 
    'Cantidades_Totales_Home_Necessities', 'Cantidades_Totales_Shoes', 
    'Cantidades_Totales_Smart_Phone', 'Cantidades_Totales_Sports', 
    'Cantidades_Totales_TV', 'Cantidades_Totales_Tools'
]

df_long = pd.melt(df_cluster0_analisis_jovenes, id_vars=['mapeo_income'], value_vars=categorias, 
                  var_name='Categoria', value_name='Cantidad_Comprada')

# Crear el barplot
plt.figure(figsize=(16, 10))
sns.barplot(data=df_long, x='mapeo_income', y='Cantidad_Comprada', hue='Categoria')

# Ajustar etiquetas
plt.title('Cantidad Comprada por Categoría y Tipo de Ingreso')
plt.xlabel('Tipo de Ingreso', fontsize=14)
plt.ylabel('Cantidad Comprada', fontsize=12)
plt.xticks(rotation=45, fontsize=12)
plt.legend(title='Categoría', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()








# Contar el número de transacciones por país y mes
df_counts = df_cluster0_analisis.groupby(['mapeo_country', 'mapeo_city']).size().reset_index(name='Customer_Count')

# Crear el gráfico sunburst
fig = px.sunburst(
    df_counts,
    path=['mapeo_country', 'mapeo_city'],
    values='Customer_Count',
    title='Distribución de clientes por País y Ciudad'
)

# Mostrar el gráfico
fig.show()


print('''La mayoria de las personas que integran el cluster 0 viven en las ciudades de Chicago y Boston de Estados Unidos.
      Seguido por United Kigdom, la ciudad de Portsmouth.''')

# Como compran? Cuanto compran? Cuanto gastan?
df_cluster0_analisis.head()
grafico_Histograma(df_cluster0_analisis,'TotalHistorico_GastadoCliente','Total gastado por cliente','TotalHistorico_GastadoCliente','Frecuencia')


#Gender

ax = sns.countplot(data=df_cluster0_analisis,x='Gender')
ax.tick_params(axis='x', rotation=90, size=7)

print('La mayoria de las personas que integran el cluster 0 son (gender) 0')

#Income

ax = sns.countplot(data=df_cluster0_analisis,x='Income')
ax.tick_params(axis='x', rotation=90, size=7)

print('El Income de las personas en el cluster 0 parece no ser determinante')




#https://python-graph-gallery.com/11-grouped-barplot/