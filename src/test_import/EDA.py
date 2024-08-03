import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from limpieza_data import dataFrame_limpiado 


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

def plot_bar_graphs(df, columns):
    for column in columns:
        plt.figure(figsize=(15, 5))
        ax = sns.countplot(x=column, data=df, order=df[column].value_counts().index)
        ax.bar_label(ax.containers[0],rotation=45)
        plt.xlabel(column, fontsize=15)
        plt.ylabel('Count', fontsize=15)
        plt.title(f'Bar Graph of {column}', fontsize=20)
        plt.xticks(rotation=45, ha='right', fontsize=12)
        plt.show()
        
cat_features = ['make','vehicle_class', 'engine_size', 'cylinders', 'transmission', 'fuel_type']

plot_bar_graphs(df, cat_features)