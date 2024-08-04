import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from limpieza_data import dataFrame_limpiado 
from plots import plot_bar_graphs, grafico_Histograma
import gc


df=dataFrame_limpiado()
df.head()

df.info()

columns_to_convert = ['Transaction_ID', 'Customer_ID', 'Zipcode']

# Iterar sobre cada columna y convertir a tipo 'category'
for column in columns_to_convert:
    df[column] = df[column].astype('category')

df.describe(percentiles=[.05,.5,.25,.75,.95,.99])

print("""La edad promedio es de 35, siendo 18 la minima y 70 la maxima. En general parece que los cliente son jovenes, viendo que el 75% son menores de 46.
Las transacciones tienen un promedio de 5 articulos. Como minimo 1 y como maximo 10, lo que indica que no hay compras de grandes volumenes.
El total gastado es en promedio 1368, siendo 10 el minimo y 5000 el maximo, como habiamos visto en la limpieza de datos, esta variable presenta una 
distribucion que no es normal, por lo que me concentrare en estudiar el logaritmo de dicha variable.
El Retaing promedio se encuentra en 3, siendo 1 el minimo y 5 el maximo. Pareciera que hay posibilidad de mejora en este aspecto.
El logaritmo del total gastado tiene un promedio de 6.7744, siendo 1.084 el minimo y 8.5169 el maximo. El 50% de las compras esta muy cercano al 
promedio en un valor de 6.9488""")


# La matriz de correlacion proporciona evidencia sobre la existencia y la fuerza de la relación entre variables.
# Una alta correlacion entre variables podria ser evidencia de colinealidad o multicolinealidad, lo que puede hacer que sea difícil determinar los efectos individuales de cada variable.
# Cuando se incluyen variables altamente correlacionadas en un modelo de análisis, estas pueden recibir un mayor peso en el modelo, lo que puede afectar la interpretación de los resultados.

numeric_columns = df.select_dtypes(include=[np.number]).columns
correlation_matrix = df[numeric_columns].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Matriz de Correlación')
plt.show()


# Hipotesis

# H1. El importe gastado en la orden puede ayudar a identificar patrones de consumo entre los usuarios.
df_clientes_gasto = df.groupby('Customer_ID')['Total_Amount_log'].sum().reset_index()
df_clientes_gasto['Customer_ID'].nunique()
df_clientes_gasto.head()
# 2. Renombrar la columna para mayor claridad
df_clientes_gasto.rename(columns={'Total_Amount_log': 'Total_Gastado'}, inplace=True)


#plot_bar_graphs(df_clientes_gasto, "Total_Gastado")


grafico_Histograma(df_clientes_gasto,'Total_Gastado','Total gastado por cliente','Total_Gastado','Frecuencia')

print("""Se puede observar del grafico que existen distintos grupos de clientes. Principalmente, los picos podrian estar indicando grupos específicos de gasto
Por ejemplo, hay un gran número de clientes que gastan entre 5 y 10 unidades, otro grupo que gasta entre 10 y 15 unidades, y así sucesivamente.
A medida que el total gastado aumenta, la frecuencia de los clientes disminuye, lo que indica que menos clientes gastan cantidades más altas.
La cola que se extiende hacia la derecha sugiere que hay algunos clientes que gastan cantidades significativamente altas, 
pero estos son mucho menos frecuentes.""")


del df_clientes_gasto
gc.collect()


# - H2. La cantidad comprada y el precio de productos son factores que permite definir perfiles de compradores.

df_clientes_gasto = df.groupby('Customer_ID')['Total_Purchases'].sum().reset_index()
df_clientes_gasto['Customer_ID'].nunique()
df_clientes_gasto.head()
# 2. Renombrar la columna para mayor claridad
df_clientes_gasto.rename(columns={'Total_Purchases': 'Cantidades_Totales'}, inplace=True)


#plot_bar_graphs(df_clientes_gasto, "Total_Gastado")


grafico_Histograma(df_clientes_gasto,'Cantidades_Totales','Cantidades totales compradas por cliente','Cantidades_Totales','Frecuencia')

print("""La mayoria de los clientes compran de 10 a 15 unidades, siendo este el punto de mayor frecuencia. A medida que la cantidad aumenta el total comprado 
      disminuye; lo que indica que hay pocos clientes que compran mcuhas unidades""")

#La teoría microeconómica de las demandas Marshallianas se utiliza para entender cómo los consumidores toman decisiones de consumo en función 
# de sus recursos disponibles y sus preferencias. La demanda Marshalliana depende del ingreso del consumidor y de los precios de los bienes disponibles. 
# Dado que el consumidor tiene un ingreso limitado 𝑚 y desea consumir una cantidad 𝑥 de cada bien, enfrenta un problema de asignación de recursos 
# para maximizar su utilidad.
# Para esto, es crucial estudiar el concepto de elasticidad precio de la demanda, ya que la utilidad del consumidor está estrechamente relacionada 
# con los precios de los bienes. 

# Alfred Marshall, en su libro Principles of Economics (1890), desarrolló este concepto para analizar cómo cambian las decisiones de consumo cuando 
# varía el precio de un bien.

#Elasticidad Precio Mayor a 1:

#Cuando la elasticidad precio de la demanda es mayor que 1, la cantidad demandada cambia más que proporcionalmente en relación con los cambios 
# en el precio. 
# Por ejemplo, si un aumento del precio del 10% resulta en una disminución de la cantidad demandada del 20%, la elasticidad es mayor a 1. 
# Esto significa que un pequeño cambio en el precio puede provocar un cambio considerable en la cantidad demandada. 
# Los bienes con sustitutos cercanos suelen tener una demanda más elástica. Por ejemplo, si un consumidor considera sustitutos similares 
# como Coca-Cola y jugo de naranja, un aumento en el precio de uno de ellos puede llevar a un cambio rápido hacia el otro.

#Elasticidad Precio Menor a 1:

#Cuando la elasticidad precio de la demanda es menor que 1, la cantidad demandada cambia menos que proporcionalmente en respuesta a cambios 
# en el precio. Este comportamiento es común en bienes esenciales, como medicamentos, donde la demanda es relativamente inelástica porque el 
# consumidor necesita estos bienes independientemente de las variaciones en el precio.

#Elasticidad Precio Igual a 1:

#Cuando la elasticidad precio de la demanda es igual a 1, la cantidad demandada cambia exactamente en la misma proporción que el cambio en el precio. 
# En este caso, el cambio en el precio resulta en un cambio proporcional en la cantidad demandada.
#Por tanto, comprender cómo cambian las cantidades demandadas para cada producto puede ayudar a segmentar a los consumidores. 
# Los consumidores que compran productos con alta elasticidad precio tienden a responder más significativamente a los cambios de precios. 
# Este análisis puede ser útil para clasificar a los consumidores en grupos basados en su sensibilidad a los cambios de precios.

#Fórmula de Elasticidad Precio de la Demanda:
#Elasticidad Precio = (Variacion % en la cantidad demandada)/(Variacion % en el precio) = (Δ𝑄/𝑄)/(Δ𝑃/𝑃) 

#El objetivo es calcular la elasticidad precio de la demanda para cada producto, lo que puede ayudar a clasificar a los consumidores y realizar 
# una segmentación funcional basada en su sensibilidad al precio. Este análisis permite a las empresas ajustar sus estrategias de precios y marketing
#  para maximizar la efectividad y mejorar la satisfacción del cliente.



#OTRA HIPOTESIS
#BIENES SUSTITUTOS Y COMPLEMENTARIOS, HACER ELASTICIDAD CRUZADA