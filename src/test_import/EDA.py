import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from limpieza_data import dataFrame_limpiado 
from plots import plot_bar_graphs, grafico_Histograma


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

#H1. El importe gastado en la orden puede ayudar a identificar patrones de consumo entre los usuarios.
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