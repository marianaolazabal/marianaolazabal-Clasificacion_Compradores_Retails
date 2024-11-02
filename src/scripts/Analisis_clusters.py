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
#El gráfico sugiere que, en todos los grupos de ingresos, los hombres tienen una participación significativamente mayor en el 
# gasto total, especialmente en los grupos de ingresos bajos, medios e indeterminados. Las mujeres tienen una menor participación 
# en todos los grupos de ingresos, mientras que el género indeterminado contribuye con el menor porcentaje en general.
#Dado que los hombres representan la mayor parte del gasto en todos los grupos de ingresos, especialmente en los segmentos de 
# ingresos bajos, medios e indeterminados, las campañas de marketing podrían orientarse más hacia este público.
#Ofrecer productos y promociones que se alineen con las preferencias de este grupo sería una estrategia clave, ya que tienen 
# una mayor propensión a gastar.
#Un enfoque de personalización en el sitio web, mostrando diferentes productos o promociones en función del género del cliente 
# (si se dispone de esta información), podría mejorar la experiencia del usuario y potencialmente aumentar las conversiones de 
# las mujeres.
# El porcentaje de gasto del género indeterminado es bajo en comparación con los hombres y mujeres en todos los grupos 
# de ingresos. Esto podría indicar que el sitio web no está siendo lo suficientemente inclusivo o atractivo para este grupo.
#Se podría considerar realizar mejoras en la usabilidad del sitio, asegurándose de que sea inclusivo para personas de todos 
# los géneros, lo que podría incluir ajustes en el lenguaje, las opciones de género en los formularios de registro o la 
# representación de productos y modelos diversos.
#Estrategias como opciones de financiamiento, descuentos por volumen, o promociones de productos esenciales podrían resonar 
# mejor con estos segmentos, maximizando el valor por cliente en estos grupos.
#Ofertas como ventas flash, recomendaciones de productos relacionadas, y envíos rápidos o gratuitos podrían aumentar las 
# conversiones y los ingresos.
#Dado que los hombres son los principales consumidores en todos los grupos, un programa de fidelización dirigido a ellos 
# podría ser muy efectivo. Esto podría incluir recompensas por compras frecuentes, descuentos personalizados o membresías 
# exclusivas para mantener a estos consumidores comprometidos con la plataforma.
#Las ofertas pueden incluir productos exclusivos, tecnologías de punta, artículos de lujo, y envíos rápidos o gratuitos.
#En lugar de campañas exclusivas para hombres o mujeres, se pueden crear campañas neutras de género que apelen a una audiencia 
# más amplia y diversa.

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


#sns.violinplot(x=df_cluster0_analisis["mapeo_income"], y=df_cluster0_analisis["Cantidades_Totales_Appliances"])

sns.boxplot(data=df_cluster0_analisis, x="TotalHistorico_GastadoCliente", y="mapeo_gender", hue="mapeo_Categoria_Edad")

print('''Como se puede apreciar en el gráfico, la distribución de gasto en los jóvenes es muy parecida, tanto para mujeres como hombres.
En el caso de Adulto-Joven, las mujeres gastan un poco más que los hombres.
En los adultos, adultos mayores y veteranos, los hombres gastan más.
El grupo de género indeterminado se encuentra con una distribución menos dispersa, no presenta casi datos atípicos y en general gastan lo mismo o en el caso de los adultos y veteranos, más que los otros
géneros. Se recomienda replantear la descripción de género para ser más inclusivo con el grupo y aplicar publicidades destinadas a aumentar la participación de personas de este grupo.''')

sns.boxplot(data=df_cluster0_analisis, x="TotalHistorico_GastadoCliente", y="mapeo_gender", hue="mapeo_income")


print('''En el caso de la distribucion del gasto por genero y grupo de ingresos, se observa que las personas que pertenecen al 
genero Femenino y el grupo de ingresos altos, tienden a gastar mas que los hombres y personas del genero indeterminado. 
Teniendo en cuenta el grafico anterior, podria ser beneficioso realizar campañas de marketing apuntadas a ofrecer 
productos premium, a personas dentro de estas categorias.
''')

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

df_long = pd.melt(df_cluster0_analisis, id_vars=['mapeo_income'], value_vars=categorias,
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


print('''Las categorías de Food y Clothing son las más compradas en todos los grupos de ingresos. Lo que hace que sea crucial prestar atención al stock de estos productos para garantizar su disponibilidad.
También se destaca la categoría de Books, en todos los segmentos de mercado.

Una estrategia efectiva podría ser ofrecer devoluciones en la categoría de ropa, permitiendo a los clientes seleccionar
lo que les gusta, probarse las prendas y devolver lo que no les interesa. Además, se podría fomentar el alquiler y la compra de libros, optimizando los envíos de ambas categorías y ofreciendo envío
gratuito a los clientes que realicen devoluciones y alquilen o compren libros.

El grupo de ingresos bajos muestra interés por productos de decoración para el hogar. Ofrecer artículos decorativos que complementen la comida podría potenciar las ventas,
como bandejas decorativas, platos y jarras.

Las categorías de tecnología, como smartphones y televisores, están presentes en todos los grupos. Dado que estos productos suelen tener precios más elevados, sería beneficioso explorar
estrategias para impulsar las ventas en estas categorías. En particular, los teléfonos móviles, que requieren poco espacio de almacenamiento y son fáciles de transportar, podrían beneficiarse
de opciones de financiamiento. También se podría considerar la inclusión de suscripciones a plataformas de streaming, audiolibros o juegos para incentivar la compra.

Finalmente, es recomendable evaluar la categoría de Sports, ya sea eliminándola o investigando más a fondo su baja popularidad.''')


df_cluster0_analisis.head()


sns.scatterplot(
    data=df_cluster0_analisis, x="TotalHistorico_CompradoCliente", y="TotalHistorico_GastadoCliente", hue="frecuencia_comp_cliente", size="frecuencia_comp_cliente",
    sizes=(20, 200), legend="full"
)


print('''El gráfico muestra una clara correlación positiva entre la cantidad total comprada y el gasto histórico del cliente. Ademas muestra como el tamaño de los circulos aumentan conforme aumenta la frecuencia de compra.
A medida que aumenta el TotalHistorico_CompradoCliente, también lo hace el TotalHistorico_GastadoCliente y con ello la frecuencia de compra. Esto sugiere que los clientes que compran más también tienden a gastar más.
Los clientes que realizan compras más frecuentes o de mayor volumen también representan un mayor valor para el negocio en términos de ingresos.
Aunque la correlación es positiva, hay una dispersión significativa entre los clientes que tienen un valor de TotalHistorico_CompradoCliente similar, lo que indica que algunos clientes gastan más que otros para un número similar de compras. Esto puede estar influenciado por factores como el tipo de producto comprado o la elección de productos premium frente a económicos.
Se observa una concentración de clientes que han gastado históricamente alrededor de 45 unidades y que también han comprado en cantidades elevadas.
Estos clientes pueden ser candidatos ideales para programas de fidelización, recompensas o servicios premium, ya que han demostrado un alto compromiso con la tienda.
En la parte inferior izquierda del gráfico, se encuentra un grupo considerable de clientes con un TotalHistorico_CompradoCliente relativamente bajo (15-25) y un gasto histórico entre 20 y 35. Estos clientes podrían estar realizando compras más esporádicas o comprando productos más económicos.
Este grupo podría ser un objetivo para aumentar su gasto y frecuencia de compra mediante campañas de marketing dirigidas, como promociones o descuentos específicos.
Segmentación basada en comportamiento: Usar esta correlación para segmentar a los clientes en categorías de alto y bajo valor podría ayudar a personalizar estrategias de retención y adquisición.''')



sns.scatterplot(data=df_cluster0_analisis, x="Cantidades_Totales_Standard", y="TotalHistorico_GastadoCliente")

sns.scatterplot(data=df_cluster0_analisis, x="Cantidades_Totales_Urgent-Delivery", y="TotalHistorico_GastadoCliente")
df_cluster0_analisis.columns

#Cash
#Credit
#Debit



# Agrupar y derretir el DataFrame
df_grouped = df_cluster0_analisis.groupby(['mapeo_income', 'mapeo_gender'])[['Cash', 'Credit', 'Debit']].sum().reset_index()
df_melted = df_grouped.melt(id_vars=['mapeo_income', 'mapeo_gender'], value_vars=['Cash', 'Credit', 'Debit'], 
                            var_name='Método de Pago', value_name='Total')

# Crear un FacetGrid con un gráfico separado por cada sexo
g = sns.FacetGrid(df_melted, col='mapeo_gender', height=5, aspect=1.2)

# Especificar el orden de los métodos de pago
order_pago = ['Cash', 'Credit', 'Debit']

# Aplicar el gráfico de barras a cada faceta
g.map(sns.barplot, 'mapeo_income', 'Total', 'Método de Pago', order=df_melted['mapeo_income'].unique(), hue_order=order_pago, palette='dark:#1f77b4')

# Añadir etiquetas y títulos a cada gráfico
g.set_axis_labels('Categoría de Ingresos', 'Total Gasto')
g.set_titles('Gasto total por sexo: {col_name}')
g.add_legend()

# Rotar las etiquetas del eje x para que sean más legibles
for ax in g.axes.flat:
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)

# Mostrar el gráfico
plt.show()


#Invierno
#Otoño
#Verano
#Primavera




# Agrupar y derretir el DataFrame
df_grouped_estacion = df_cluster0_analisis.groupby(['mapeo_income', 'mapeo_gender'])[['Invierno', 'Otoño', 'Verano', 'Primavera']].sum().reset_index()
df_melted_estacion = df_grouped_estacion.melt(id_vars=['mapeo_income', 'mapeo_gender'], value_vars=['Invierno', 'Otoño', 'Verano', 'Primavera'], 
                            var_name='Estación', value_name='Total')

# Crear un FacetGrid con un gráfico separado por cada sexo
g = sns.FacetGrid(df_melted_estacion, col='mapeo_gender', height=5, aspect=1.2)

# Especificar el orden de los métodos de pago
order_estacion = ['Invierno', 'Otoño', 'Verano', 'Primavera']

# Aplicar el gráfico de barras a cada faceta
g.map(sns.barplot, 'mapeo_income', 'Total', 'Estación', order=df_melted_estacion['mapeo_income'].unique(), hue_order=order_estacion, palette='dark:#1f77b4')

# Añadir etiquetas y títulos a cada gráfico
g.set_axis_labels('Categoría de Ingresos', 'Total Gasto')
g.set_titles('Gasto total por sexo: {col_name}')
g.add_legend()

# Rotar las etiquetas del eje x para que sean más legibles
for ax in g.axes.flat:
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)

# Mostrar el gráfico
plt.show()




#madrugada
#mañana
#medioDia
#noche
#tarde
#TotalHistorico_GastadoCliente



# Agrupar y derretir el DataFrame
df_grouped_momento = df_cluster0_analisis.groupby(['mapeo_income', 'mapeo_gender'])[['madrugada', 'mañana', 'medioDia', 'noche', 'tarde']].sum().reset_index()
df_melted_momento = df_grouped_momento.melt(id_vars=['mapeo_income', 'mapeo_gender'], value_vars=['madrugada', 'mañana', 'medioDia', 'noche', 'tarde'], 
                            var_name='Momento del día', value_name='Total')

# Crear un FacetGrid con un gráfico separado por cada sexo
g = sns.FacetGrid(df_melted_momento, col='mapeo_gender', height=5, aspect=1.2)

# Especificar el orden de los métodos de pago
order_momentoDia = ['madrugada', 'mañana', 'medioDia', 'noche', 'tarde']

# Aplicar el gráfico de barras a cada faceta
g.map(sns.barplot, 'mapeo_income', 'Total', 'Momento del día', order=df_melted_momento['mapeo_income'].unique(), hue_order=order_momentoDia, palette='dark:#1f77b4')

# Añadir etiquetas y títulos a cada gráfico
g.set_axis_labels('Categoría de Ingresos', 'Total Gasto')
g.set_titles('Gasto total por sexo: {col_name}')
g.add_legend()

# Rotar las etiquetas del eje x para que sean más legibles
for ax in g.axes.flat:
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)

# Mostrar el gráfico
plt.show()


print('''Ofrecer a las mujeres dentro de la categoria Adulto Joven de ingresos medios y altos, productos que sean de su interes,
hacerlo en la madrugada y la mañana, cuando mas se compra. Para ello es necesario estudiar los productos que se compran.
Estudiar si las personas que compran al medioDia y en la tarde son de otro grupo de edad y que productos se compra.''')


print('''*******Grupo femenino************''')
df_cluster0_analisis_f=df_cluster0_analisis[df_cluster0_analisis['mapeo_gender']=='Female']

#Como se distribuyen las mujeres en cada pais

ax = sns.countplot(x="mapeo_country", data=df_cluster0_analisis_f)

#Hay más representatividad en United States y United Kingdom
#Como se distribuye las edades en estos paises

print('''*******Grupo femenino en Estados Unidos************''')
df_cluster0_analisis_f_USA=df_cluster0_analisis_f[df_cluster0_analisis_f['mapeo_country']=='United States']

ax = sns.countplot(x="mapeo_Categoria_Edad", data=df_cluster0_analisis_f_USA)

#En USA hay mayor representatividad de mujeres Jovenes y Adultas
#A que hora compran estos grupos?

def f_joven_USA_Hora(df_usar, valor1, valor2):
    # Filtrar por categoría de edad
    df_cluster0_analisis_f_USA_hora = df_usar[df_usar['mapeo_Categoria_Edad'].isin([valor1, valor2])]

    # Convertir a formato largo para obtener la frecuencia por cada momento del día
    df_long = df_cluster0_analisis_f_USA_hora.melt(value_vars=["madrugada", "mañana", "medioDia", "noche", "tarde"], 
                                                   var_name="Hora", value_name="Frecuencia")

    # Sumar las frecuencias por hora para el gráfico de barras
    df_suma = df_long.groupby("Hora")["Frecuencia"].sum().reset_index()

    # Crear gráfico de barras
    ax = sns.barplot(x="Hora", y="Frecuencia", data=df_suma)

    # Identificar los momentos del día con mayores compras
    max_frecuencias = df_suma[df_suma["Frecuencia"] == df_suma["Frecuencia"].max()]["Hora"].values
    condiciones = df_cluster0_analisis_f_USA_hora[max_frecuencias].sum(axis=1) > 0.0
    
    # Filtrar por los momentos de mayor compra identificados
    df_cluster0_analisis_f_USA_ingresos = df_cluster0_analisis_f_USA_hora[condiciones]

    return df_cluster0_analisis_f_USA_ingresos


#----------------------------------
def top10 (df_top):
    
    totals = df_top[['Cantidades_Totales_Appliances', 'Cantidades_Totales_Audio', 'Cantidades_Totales_Books', 
            'Cantidades_Totales_Clothing', 'Cantidades_Totales_Computer', 'Cantidades_Totales_Food', 
            'Cantidades_Totales_Furniture', 'Cantidades_Totales_Games_Toys', 
            'Cantidades_Totales_Health_PersonalCare', 'Cantidades_Totales_Home_Decor', 
            'Cantidades_Totales_Home_Necessities', 'Cantidades_Totales_Shoes', 
            'Cantidades_Totales_Smart_Phone', 'Cantidades_Totales_Sports', 
            'Cantidades_Totales_TV', 'Cantidades_Totales_Tools']].sum()
    
    return totals

#----------------------------------

def estuadio_ingresos (df, valor):

    df_top= df[df['mapeo_income']==valor]

    top_10 = top10(df_top).sort_values(ascending=False).head(10)
    print("Top 10 de categorías más compradas:")
    print(top_10)

    return df_top


#----------------------------------

def mensaje(num):
    if(num==1):
        return '''Análisis de comportamiento de compra en mujeres jóvenes y adultas en USA:
        En los Estados Unidos, hay una alta representación de mujeres jóvenes y adultas con ingresos elevados que compran principalmente 
        en las primeras horas del día, especialmente durante la madrugada y la mañana. 
        Estas consumidoras se enfocan en diversas categorías de productos, con particular preferencia por alimentos, ropa y libros.
        Los Alimentos son la categoría más comprada por este grupo.
        Ropa y libros, le siguen en popularidad. Existe una oportunidad para ofrecer estos productos con una plataforma que permita tanto 
        la compra de artículos nuevos como la reventa de productos usados, incentivando así un ciclo de consumo sostenible. 
        También podría considerarse la integración de libros electrónicos (e-books) en la plataforma.
        Decoración del hogar, muebles y electrodomésticos: Aunque estos productos tienden a ser más costosos, presentan alta rotación. 
        Esto sugiere que estas compradoras buscan productos en tendencia, de calidad y que reflejen un interés en la moda y el diseño. 
        Sería beneficioso ofrecer artículos de vanguardia que satisfagan esta demanda.
        Productos electrónicos (audio, smartphones y televisores): Estos productos, aunque presentan pocas cantidades vendidas, tienen un impacto 
        significativo en los ingresos de la empresa, ya que pequeños aumentos en las unidades vendidas pueden significar cambios mayores en la rentabilidad de la empresa. 
        En particular, los smartphones son altamente rentables, ya que ocupan poco espacio de almacenamiento y son fáciles de transportar. 
        Una estrategia atractiva podría ser la oferta de un plan de recambio anual, en el cual las clientas puedan obtener el último modelo de teléfono 
        al entregar su dispositivo usado, que a su vez podría repararse y revenderse a clientes de ingresos más bajos. 
        Además, se podrían ofrecer descuentos en audífonos al comprar un smartphone o parlantes con la compra de un televisor.
        La mayoría de estas consumidoras opta por pagar con crédito.
        Las ciudades con mayor representatividad en este grupo son Boston y Chicago. Aunque el nivel de satisfacción es bueno en ambas, 
        se observa una porción de clientes insatisfechas. Esto abre una oportunidad para investigar las causas de esta insatisfacción, diferenciando 
        las características de estos grupos para mejorar la experiencia de compra. Si no se cuenta con más información al respecto, podría ser útil 
        enviar un cuestionario de satisfacción acompañado de un incentivo, como un descuento en alimentos, libros o ropa, para animar la participación.
        Como estas compradoras tienden a realizar sus compras en la madrugada y la mañana, sería conveniente implementar un carrito de compras programado. 
        Este podría optimizar el tiempo de búsqueda, sugiriendo automáticamente productos que suelen comprar y dejando espacio para descubrir nuevos 
        artículos o recomendaciones personalizadas en función de sus preferencias. Esto permitiría una experiencia de compra eficiente y atractiva.
        '''
    elif(num==2):
        return '''Análisis de satisfacción y optimización de envíos en diferentes categorías de productos:.
        Se observa que las clientas de ingresos altos están muy satisfechas con el servicio de entrega para productos de electrodomésticos (Appliances). 
        Sin embargo, en las categorías de Books y Food, la diferencia en satisfacción es menor, lo que podría indicar problemas en el servicio de envío 
        específico para estos productos. En la categoría de Clothing, el índice de satisfacción es significativamente mejor, lo que sugiere que el proceso 
        de entrega para ropa se maneja con mayor eficacia que en las otras categorías.
        Para optimizar la satisfacción de las clientas y mejorar la eficiencia en los envíos, podría ser beneficioso implementar una plataforma de 
        alquiler de libros online. Esto permitiría a las clientas alquilar libros junto con sus compras de ropa, combinando envíos y disminuyendo 
        la carga logística en momentos de alta demanda.
        En caso de que la empresa experimente saturación de entregas en ciertos momentos del día, podría ser útil incentivar la compra de artículos 
        menos urgentes, como libros, junto con productos de alta demanda. Esto permitiría agrupar envíos y liberar recursos para atender otras categorías 
        con mayor rapidez.
        Para ofrecer mayor conveniencia a las clientas, podría implementarse un sistema de casilleros en lugares estratégicos de la ciudad. 
        De esta forma, las clientas podrían retirar sus pedidos en el horario que más les convenga, reduciendo la presión sobre el sistema de entregas 
        y mejorando la experiencia del cliente al permitirle flexibilidad en la recogida de sus productos.
        ''' 
    elif(num==3):
        return '''El gráfico muestra que los clientes insatisfechos representan casi el 80% de la cantidad de clientes satisfechos, lo cual indica una 
        deficiencia significativa en el servicio de envíos. Este dato sugiere que es crucial mejorar la calidad de entrega, especialmente en las 
        ciudades de Chicago y Boston, donde se concentra la mayor cantidad de clientes.
        Foco en Chicago y Boston: Dado que estas ciudades presentan el mayor volumen de clientes, es prioritario optimizar el servicio de entrega 
        en estas áreas para reducir la insatisfacción. Identificar las causas de los problemas actuales en la logística de envío (como demoras, 
        entregas fallidas o falta de opciones flexibles) sería fundamental para mejorar la experiencia de los clientes y fortalecer la retención.
        Expansión en San Francisco: La ciudad de San Francisco es un mercado con gran potencial de crecimiento, especialmente por su población 
        predominantemente joven, que valora la flexibilidad y las opciones de conveniencia. Implementar casilleros de recogida en puntos estratégicos 
        de la ciudad podría mejorar la experiencia del cliente, permitiéndole retirar sus pedidos en el momento que más le convenga y facilitar el 
        proceso de devolución. Estos casilleros podrían situarse en ubicaciones clave, como estaciones de transporte público, gimnasios y áreas de 
        trabajo, para adaptarse al estilo de vida activo y dinámico de estos clientes.
        Además de brindar conveniencia a los clientes, los casilleros reducirían la presión sobre el sistema de entregas al disminuir el número de 
        envíos a domicilio y facilitar la logística de devoluciones. Los clientes podrían gestionar sus devoluciones fácilmente mientras realizan 
        otras actividades cotidianas, lo que aumentaría la eficiencia operativa y mejoraría la satisfacción general con el servicio.
        '''

    elif(num==4):
        return
    elif(num==5):
        return
    elif(num==6):
        return

#----------------------------------


def f_joven_USA_ing (df_f_USA_ingresos, valor):

    def top10_metodoPago(df_top):
        # Seleccionar las columnas de categorías y métodos de pago
        categorias = ['Cantidades_Totales_Appliances', 'Cantidades_Totales_Audio', 'Cantidades_Totales_Books', 
                    'Cantidades_Totales_Clothing', 'Cantidades_Totales_Computer', 'Cantidades_Totales_Food', 
                    'Cantidades_Totales_Furniture', 'Cantidades_Totales_Games_Toys', 
                    'Cantidades_Totales_Health_PersonalCare', 'Cantidades_Totales_Home_Decor', 
                    'Cantidades_Totales_Home_Necessities', 'Cantidades_Totales_Shoes', 
                    'Cantidades_Totales_Smart_Phone', 'Cantidades_Totales_Sports', 
                    'Cantidades_Totales_TV', 'Cantidades_Totales_Tools']
        
        # Crear un DataFrame solo con las columnas de interés
        df_totals1 = df_top[categorias + ['Cash', 'Credit', 'Debit']]
        

        # Convertir el DataFrame a formato largo para tener cada categoría y método de pago en filas separadas
        df_long = df_totals1.melt(id_vars=['Cash', 'Credit', 'Debit'], 
                                value_vars=categorias, 
                                var_name="Categoria", 
                                value_name="Cantidad_Total")
        
        # Ordenar primero por "Cantidad_Total" y luego por el valor de cada método de pago
        df_sorted = df_long.sort_values(by=["Cantidad_Total", "Cash", "Credit", "Debit"], ascending=False)
        
        # Seleccionar el Top 10
        top_10 = df_sorted.head(10)
        
        return top_10

    # Ejecutar la función y ver los resultados
    top_10_metodoPago = top10_metodoPago(df_f_USA_ingresos)
    print("Top 10 de categorías más compradas por métodos de pago:")
    print(top_10_metodoPago)



    #como es el nivel de satisfaccion?
    df_counts = df_f_USA_ingresos.groupby(['mapeo_city', 'mapeo_satisfaction']).size().reset_index(name='Group_Count')

    # Crear el gráfico sunburst
    fig = px.sunburst(
        df_counts,
        path=['mapeo_city', 'mapeo_satisfaction'],
        values='Group_Count',
        title='Distribución de Transacciones por País y Mes'
    )

    # Mostrar el gráfico
    fig.show()


    if(valor=='High'):
        print(mensaje(1))
    elif(valor=='Low'):
        print(mensaje(4))
    elif(valor=='Indeterminate'):
        print(mensaje(7))
    else:
        return ''



    #--------------------------------------------------------------------------------------------------

    categorias = [
        'Cantidades_Totales_Appliances', 'Cantidades_Totales_Audio', 'Cantidades_Totales_Books', 
        'Cantidades_Totales_Clothing', 'Cantidades_Totales_Computer', 'Cantidades_Totales_Food', 
        'Cantidades_Totales_Furniture', 'Cantidades_Totales_Games_Toys', 
        'Cantidades_Totales_Health_PersonalCare', 'Cantidades_Totales_Home_Decor', 
        'Cantidades_Totales_Home_Necessities', 'Cantidades_Totales_Shoes', 
        'Cantidades_Totales_Smart_Phone', 'Cantidades_Totales_Sports', 
        'Cantidades_Totales_TV', 'Cantidades_Totales_Tools'
    ]

    # Usamos idxmax en las columnas de categorías para obtener la categoría con el valor máximo
    df_f_USA_ingresos['Modalidad_Preferida_producto'] = df_f_USA_ingresos[categorias].idxmax(axis=1)

    # Opcional: Limpiamos el nombre de la categoría eliminando el prefijo "Cantidades_Totales_"
    df_f_USA_ingresos['Modalidad_Preferida_producto'] = df_f_USA_ingresos['Modalidad_Preferida_producto'].str.replace('Cantidades_Totales_', '', regex=False)

    df_f_USA_ingresos.head()

    # Contamos la cantidad de clientes por satisfacción y modalidad preferida
    df_count = df_f_USA_ingresos.groupby(['mapeo_satisfaction', 'Modalidad_Preferida_producto']).size().reset_index(name='Total_Clientes')

    # Creamos el gráfico
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df_count, x='Modalidad_Preferida_producto', y='Total_Clientes', hue='mapeo_satisfaction')

    plt.title('Preferencia de Modalidad de producto por Satisfacción del Cliente')
    plt.ylabel('Número de Clientes')
    plt.xlabel('Modalidad de Producto Preferido')
    plt.legend(title='Satisfacción')
    plt.show()


    if(valor=='High'):
        print(mensaje(2))
    elif(valor=='Low'):
        print(mensaje(5))
    elif(valor=='Indeterminate'):
        print(mensaje(8))
    else:
        return ''


    # Supongamos que tienes tu DataFrame llamado df
    # Creamos una columna que indica la modalidad de envío preferida por cada cliente
    df_f_USA_ingresos['Modalidad_Preferida'] = df_f_USA_ingresos.apply(
        lambda x: 'Standard' if x['Cantidades_Totales_Standard'] > x['Cantidades_Totales_Urgent-Delivery'] else 'Urgent-Delivery', 
        axis=1
    )

    # Contamos la cantidad de clientes por satisfacción y modalidad preferida
    df_count = df_f_USA_ingresos.groupby(['mapeo_satisfaction', 'Modalidad_Preferida']).size().reset_index(name='Total_Clientes')

    # Creamos el gráfico
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df_count, x='Modalidad_Preferida', y='Total_Clientes', hue='mapeo_satisfaction')

    plt.title('Preferencia de Modalidad de Envío por Satisfacción del Cliente')
    plt.ylabel('Número de Clientes')
    plt.xlabel('Modalidad de Envío Preferida')
    plt.legend(title='Satisfacción')
    plt.show()


    df_f_USA_ingresos.head()

    if(valor=='High'):
        print(mensaje(3))
    elif(valor=='Low'):
        print(mensaje(6))
    elif(valor=='Indeterminate'):
        print(mensaje(9))
    else:
        return ''

def analisisIngresos (df, edad1, edad2):
    print(f"*******Grupo femenino {edad1} y {edad2} en Estados Unidos con ingresos altos************")

    df_f_USA_ingAltos=estuadio_ingresos(df, 'High')
    f_joven_USA_ing (df_f_USA_ingAltos, 'High')


    print(f"*******Grupo femenino {edad1} y {edad2} en Estados Unidos con ingresos bajos************")

    df_f_USA_ingBajos=estuadio_ingresos(df, 'Low')
    f_joven_USA_ing (df_f_USA_ingBajos, 'Low')


    print(f"*******Grupo femenino {edad1} y {edad2} en Estados Unidos con ingresos indeterminados************")

    df_f_USA_ingIndeterminados=estuadio_ingresos(df, 'Indeterminate')
    f_joven_USA_ing (df_f_USA_ingIndeterminados, 'Indeterminate')




#En USA hay mayor representatividad de mujeres Jovenes y Adultas, compran en la madrugada y en la mañana y tienen ingresos altos
#Top 10 productos comprados


print('''*******Grupo femenino joven y adulto joven en Estados Unidos************''')

df_cluster0_analisis_f_USA_ingresos_jov=f_joven_USA_Hora(df_cluster0_analisis_f_USA,'Adulto_Joven', 'Joven')
analisisIngresos(df_cluster0_analisis_f_USA_ingresos_jov)

# Crear gráfico de ingresos para las filas filtradas
ax = sns.countplot(x="mapeo_income", data=df_cluster0_analisis_f_USA_ingresos_jov)

print('''*******Grupo femenino adulto y adulto mayor en Estados Unidos************''')

df_cluster0_analisis_f_USA_ingresos_adul=f_joven_USA_Hora(df_cluster0_analisis_f_USA,'Adulto', 'Adulto_Mayor')
analisisIngresos(df_cluster0_analisis_f_USA_ingresos_adul)
ax = sns.countplot(x="mapeo_income", data=df_cluster0_analisis_f_USA_ingresos_adul)

print('''*******Grupo femenino joven y adulto joven en Estados Unidos************''')

df_cluster0_analisis_f_USA_ingresos_vet=f_joven_USA_Hora(df_cluster0_analisis_f_USA,'Adulto_Mayor', 'Veterano')
analisisIngresos(df_cluster0_analisis_f_USA_ingresos_vet)
ax = sns.countplot(x="mapeo_income", data=df_cluster0_analisis_f_USA_ingresos_vet)
















# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Hacer generico para los distintos grupos de edades dentro de f-USA, desp los distintos generos y por ultimo los paises.
#PONER TODO DENTRO DE UNA FUNCION PARA PODER REPETIRLO PARA EL CLUSTER 1 y 2










top_10_group = top10(df_cluster0_analisis_f_USA_ingresos_altos).groupby(['Cash', 'Credit', 'Debit']).sort_values(ascending=False).head(10)
print("Top 10 de categorías más compradas:")
print(top_10)


df_cluster0_analisis_f_USA_hora.columns


df_cluster0_analisis_f_JA = df_cluster0_analisis_f[df_cluster0_analisis_f['mapeo_Categoria_Edad'].isin(['Adulto_Joven', 'Joven'])]
df_cluster0_analisis_f_JA_madrugada = df_cluster0_analisis_f_JA[(df_cluster0_analisis_f_JA['madrugada'] > 0.0) | (df_cluster0_analisis_f_JA['mañana'] > 0.0 ) | (df_cluster0_analisis_f_JA['noche']> 0.0)]
df_cluster0_analisis_f_JA_madrugada.head()


# Solo Australia --- 

#FALTA VER INGRESOOOOOOS

df_cluster0_analisis_f_JA_medioDia_Australia=df_cluster0_analisis_f_JA_medioDia[df_cluster0_analisis_f_JA_medioDia['mapeo_country']=='Australia']

top_10_medioDia = top10(df_cluster0_analisis_f_JA_medioDia_Australia).sort_values(ascending=False).head(10)
print("Top 10 de categorías más compradas:")
print(top_10_medioDia)


print('''No hay personas del sexo femenino en la categoria Adulto_Joven o Joven que compren en la medioDia o tarde en Australia''')


df_cluster0_analisis_f_JA_madrugada_Australia=df_cluster0_analisis_f_JA_madrugada[df_cluster0_analisis_f_JA_madrugada['mapeo_country']=='Australia']

top_10_medioDia = top10(df_cluster0_analisis_f_JA_madrugada_Australia).sort_values(ascending=False).head(10)
print("Top 10 de categorías más compradas:")
print(top_10_medioDia)

print('''No hay personas del sexo femenino en la categoria Adulto_Joven o Joven que compren en la madrugada, mañana o noche en Australia''')


ax = sns.countplot(x="mapeo_income", data=df_cluster0_analisis_f_JA_madrugada_Australia)


print('''Hacer push de notificaciones de productos de comida y libros, en la madrugada, mañana o noche, a las mujeres de ingresos medios y bajos,
 que se encuentren en la categoría jovenes o jovenes adultas, viven o residen en Australia.''')


#Solo Alemania

df_cluster0_analisis_Alemania=df_cluster0_analisis[df_cluster0_analisis_f_JA_medioDia['mapeo_country']=='Australia']

# Reino Unido

# Estados Unidos


#Estacion y momento del dia

#Cuanto se gasta en Invierno y cuanto de eso se gasta en la mañana, mediodia, tarde y denoche
#Cuanto se gasta en Otoño y cuanto de eso se gasta en la mañana, mediodia, tarde y denoche
#Cuanto se gasta en Primavera y cuanto de eso se gasta en la mañana, mediodia, tarde y denoche
#Cuanto se gasta en Verano y cuanto de eso se gasta en la mañana, mediodia, tarde y denoche


















# Agrupar por género y nivel de ingreso, y sumar las estaciones
suma_momentoDia_income_gender = df_cluster0_analisis.groupby(['mapeo_gender', 'mapeo_income'])[['madrugada', 'mañana', 'medioDia', 'noche', 'tarde']].sum()

# Crear un DataFrame para visualización
suma_momentoDia_income_gender = suma_momentoDia_income_gender.unstack(level=0)  # Para hacer que el género sea una subcategoría

# Crear el gráfico
suma_momentoDia_income_gender.plot(kind='bar', stacked=True, figsize=(12, 8))

plt.title('Suma del gasto por momento del día, por género y nivel de ingreso')
plt.xlabel('Nivel de Ingreso')
plt.ylabel('Suma')
plt.xticks(rotation=45)
plt.legend(title='Género', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()  # Ajustar el espacio
plt.show()
































#Estudiar la distribucion de los datos en cash, credit y debit
#Ver como pagan los distintos generos y los distintos income
#Ver que se compra


df_cluster0_analisis_cash=df_cluster0_analisis[df_cluster0_analisis['Cash']>0]
df_cluster0_analisis_Crash_Credit=df_cluster0_analisis_cash[df_cluster0_analisis_cash['Credit']>0]
df_cluster0_analisis_Crash_Credit_Debit=df_cluster0_analisis_Crash_Credit[df_cluster0_analisis_Crash_Credit['Debit']>0]

sns.histplot(data=df_cluster0_analisis_Crash_Credit_Debit, x="Cash", hue="mapeo_income", multiple="stack")


#Invierno
#Otoño
#Verano
#Primavera


#madrugada
#mañana
#medioDia
#noche
#tarde


#conclusiones al momento, ver de hacer notificaciones push a las mujeres de altos y medios ingresos en algun momento del dia, en algunas festividades o momentos del año de productos premium de tal categoria
#ver de promover nuevos tv y smartphone a las personas de altos ingresos y promover vijeos modelos a personas de bajos ingresos, ofrecer financiamientos y descuentos si son comprador frecuente
#ofrecer los dias y momentos del dia que mas se compra comida
#ofrecer cuando se compra ropa, productos de decoracion y libros para comprar o alquilar, con devolucion gratis si compra ropa y uno de los otros dos (para optimizar el envio). Descontar el envio en la compra si compra
#ropa y deco y libro
#ofrecer pagar con transferencia los que pagan en cash o descuento para tarjetas de forma de incentivar compras en los que pagan con cash y credito.
#ver por pais como se distribuye geneor e income. En usa sabemos que son hombres, ver en que gastan
















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



sns.pairplot(df_cluster0_analisis, hue='mapeo_income', palette='coolwarm')




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
#https://plotly.com/python/bar-charts/