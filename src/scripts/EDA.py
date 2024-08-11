import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
#from limpieza_data import dataFrame_limpiado 
from funciones_generales import pathToData
from plots import plot_bar_graphs, grafico_Histograma
import gc
import plotly.express as px

#TIENE QUE QUEDARME UNA TABLA CON UNA LINEA POR CLIENTEEEEEE


csv_path = pathToData()
df =pd.read_csv(csv_path + 'Limpiado.zip')

#df=dataFrame_limpiado()
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

# Ligadas a las características de la orden


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

# Transformacion Gasto total/Cantidad comprada (Historicamente por el cliente)




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

pd.set_option('display.max_columns', None)
df.head()

# Agrupar los datos por producto, año y mes, y sumar las cantidades demandadas
df_grouped = df.groupby(['products', 'Month','Product_Category', 'Total_Amount_log', 'Amount'])['Total_Purchases'].sum().reset_index()
df_grouped.head()
df_grouped_Electronics=df_grouped[df_grouped['Product_Category']=='Electronics']


def grafico_cantidadesDemandadas(dataFrame, variable, valor):
  # Definir el orden de los meses
  order = [
      'March', 'April', 'May', 'June', 'July', 'August',
      'September', 'October', 'November', 'December',
      'January', 'February'
  ]

  # Filtrar los datos para 'Lenovo Tab'
  df_grouped_filtrado = dataFrame[dataFrame[variable] == valor]

  # Ordenar los datos por el mes
  df_grouped_filtrado['Month'] = pd.Categorical(df_grouped_filtrado['Month'], categories=order, ordered=True)
  df_grouped_filtrado.sort_values(by='Month', inplace=True)

  # Configurar el estilo de Seaborn
  sns.set(style="whitegrid")

  # Crear la figura y los ejes
  fig, ax1 = plt.subplots(figsize=(14, 8))

  # Graficar la cantidad demandada en el primer eje
  color = 'tab:blue'
  ax1.set_xlabel('Fecha')
  ax1.set_ylabel('Cantidad Demandada', color=color)
  sns.lineplot(data=df_grouped_filtrado, x='Month', y='Total_Purchases', marker='o', ax=ax1, color=color)
  ax1.tick_params(axis='y', labelcolor=color)

  # Crear un segundo eje para el precio
  ax2 = ax1.twinx()
  color = 'tab:red'
  ax2.set_ylabel('Precio', color=color)
  sns.lineplot(data=df_grouped_filtrado, x='Month', y='Amount', marker='x', ax=ax2, color=color)
  ax2.tick_params(axis='y', labelcolor=color)

  # Añadir título y ajustar la leyenda
  plt.title('Evolución de Cantidades Demandadas y Precios por Producto')
  fig.tight_layout()
  plt.xticks(rotation=45)

  # Mostrar el gráfico
  plt.show()


df_grouped_Electronics['products'].unique()


grafico_cantidadesDemandadas(df_grouped_Electronics, 'products', 'Lenovo Tab')
grafico_cantidadesDemandadas(df_grouped_Electronics, 'products', '4K TV')


# Agrupar los datos por producto y mes
df_grouped_by_product_month = df.groupby(['products', 'Month']).agg({
    'Total_Purchases': 'sum',
    'Amount': 'mean'
}).reset_index()


# Para simplificar, se usará una estructura básica de dos periodos para el cálculo
# Encuentra los productos únicos
products = df_grouped_by_product_month['products'].unique()

total_purchases_per_product = df.groupby('products')['Total_Purchases'].sum().reset_index()
total_purchases_per_product.rename(columns={'Total_Purchases': 'Total_Purchases_All'}, inplace=True)

df = df.merge(total_purchases_per_product, on='products', how='left')

df.head()


elasticity_results = []

for product in products:
    df_product = df_grouped_by_product_month[df_grouped_by_product_month['products'] == product]

    # Asegúrate de que haya datos suficientes
    if df_product.shape[0] < 2:
        elasticity_results.append({
            'Product': product,
            'Elasticity': None
        })
        continue

    # Preparar datos para regresión
    X = df_product['Amount']  # Precio
    Y = df_product['Total_Purchases']  # Cantidad demandada

    X = sm.add_constant(X)  # Añadir constante para el término de intersección

    model = sm.OLS(Y, X).fit()  # Ajustar el modelo

    # Extraer el coeficiente de precio (beta)
    beta = model.params['Amount']

    # Calcular elasticidad
    P_avg = X['Amount'].mean()  # Precio promedio
    Q_avg = Y.mean()  # Cantidad promedio

    if P_avg != 0:
        elasticity = beta * (P_avg / Q_avg)
    else:
        elasticity = None

    elasticity_results.append({
        'Product': product,
        'Elasticity': elasticity
    })

# Convertir resultados a DataFrame
df_elasticity = pd.DataFrame(elasticity_results)

# Mostrar los resultados
df_elasticity.head()

# Unir df_elasticity con df para copiar la columna Total_Purchases_All
df_elasticity = df_elasticity.merge(df[['products', 'Total_Purchases_All']], left_on='Product', right_on='products', how='left')

# Eliminar la columna Product duplicada
df_elasticity.drop(columns=['Product'], inplace=True)
df_elasticity=df_elasticity.drop_duplicates()
df_elasticity.head(20)
df.head(20)


df_elasticity_filtro=df_elasticity['Total_Purchases_All'].min()
print(df_elasticity_filtro)


# Crear el gráfico de barras interactivo
fig = px.bar(df_elasticity, 
             x='products', 
             y='Elasticity',
             height=800, 
             color='Elasticity', 
             text='Elasticity', 
             hover_data={'products': True, 'Elasticity': True})

# Configuración del título y etiquetas
fig.update_layout(
    title='Elasticidad Precio de la Demanda por Producto',
    xaxis_title='Producto',
    yaxis_title='Elasticidad',
    title_font_size=20,
    yaxis=dict(tickfont=dict(size=14))
)

# Mostrar el gráfico
fig.show()


print("""El grafico muestra la elasticidad precio de la demanda para diferentes productos.
      
Los clientes que compran productos con elasticidad negativa podria indicar que el cliente es sensible al precio 
ya que un cambio en el precio afecta a las cantidades demandadas. Cuanto mas negativo sea el valor, mayor
sera el cambio en las cantidades demandadas en relacion al precio.

En contrapartida, los clientes que compran productos con elasticidades cercanas a cero, podrian ser clasificados
como menos sensibles al precio, ya que cambios en el precio no afectan demasiado su comportamiento de compra.
      
Por último, los productos con elasticidades positivas son los llamados de Veblen y Giffen para los cuales al 
aumentar el precio, aumenta la demanda. Son por ejemplo, bienes de lujo o productos en los que un mayor precio
percibido puede aumentar la demanda debido a la percepción de mayor calidad o prestigio.

Entender estos patrones permite conocer insights para definir promociones y descuentos con mayor exactitud.
Para productos con alta elasticidad negativa (valor absoluto alto), ofrecer descuentos o promociones puede 
atraer más ventas, ya que los clientes son muy sensibles a cambios en el precio.
Para productos con elasticidad baja (valor absoluto bajo), se puede ajustar los precios sin esperar grandes 
cambios en la demanda, optimizando así los márgenes de ganancia.""")

#Transformacion elasticidad de los productos comprados por el cliente 

# H3. Los tipos de productos y las características inherentes a los productos comprados ayudan a explicar patrones de consumo.
df.head()
df.columns
df['Product_Brand'].unique()
fig = px.treemap(df, 
                 path=['Product_Category', 'Product_Type', 'Product_Brand'], 
                 values='Total_Purchases',
                 title='Productos más comprados por categoría',
                 color='Total_Purchases',
                 color_continuous_scale='RdBu')

fig.show()

print('''De este grafico se destacan algunas marcas y productos mas frecuentes entre los que compran los clientes.
Samsung y Sony son las marcas mas destacadas de la categoria Electronics. Por su parte, Pepsi y Coca-Cola, son las mas 
vendidas en Grocery y tambien se observa en esta categoria que las bebidas son las mas compradas, seguidas por Chocolate 
snacks. En la categoria de ropa tenemos Adidas y Nike como las predominantes para zapatos, shorts y camperas, 
seguido por Zara en cuando a pantalones, vestidos y remeras. En la categoria books figuran tres marcas, Random House, Harper Collins 
y Penguin Books. Para Home Decor esta IKEA, Bed Bath & Beyond y Home Depot.
Viendo que las marcas se repiten en varias categorias, parece que los clientes podrian tener preferencias entre estas marcas.
Si bien hay diferencia entre las cantidades compradas, esta diferencia no es tan pronunciada, lo que podria estar diciendo 
que si bien los clientes prefieren algunas marcas sobre otras, las marcas mas compradas parecen estar equilibradas en cuanto a su 
market sheare. Esto podria ser beneficio para la empresa ya que tiene un mejor margen para negociar, impulsando ventas de 
algunos productos con promociones o descuentos.
Este tipo de análisis es útil para entender las preferencias del consumidor y puede ayudar a las empresas a tomar decisiones informadas 
sobre inventarios, estrategias de marketing y asociaciones de marca.''')

fig = px.treemap(df, 
                 path=['Product_Category', 'Product_Type', 'Product_Brand'], 
                 values='Amount',
                 title='Productos más comprados por categoría',
                 color='Total_Purchases',
                 color_continuous_scale='RdBu')

fig.show()

df['Product_Type'].unique()
#customer_counts = df.groupby(['Product_Category', 'Product_Type', 'Product_Brand','Customer_ID'])['Total_Amount'].sum().reset_index()
#customer_counts.rename(columns={'Customer_ID': 'Customer_Count'}, inplace=True)
#fig = px.treemap(customer_counts, 
#                 path=['Product_Category', 'Product_Type', 'Product_Brand'], 
#                 values='Customer_Count',
#                 title='Número de clientes que compraron por categoría de producto',
#                 color='Customer_Count',
#                 color_continuous_scale='RdBu')

#fig.show()

# Contar las ocurrencias de cada cliente
customer_counts = df['Customer_ID'].value_counts()

# Obtener el ID del cliente que se repite más veces
most_frequent_customer_id = customer_counts.idxmax()

print(f"El ID del cliente que se repite más veces es {most_frequent_customer_id}.")

#df47382=df[df['Customer_ID']==47382]
#df47382.head(10)


#No voy a usar los productos para modelar, sino para separar funcionalmente



#H4. El tipo de envío solicitado para la entrega del pedido.


def graficoTorta(variableInteres, variableFiltro, titulo):
    # Agrupar por cliente y el interés, y sumar las compras
    df_suma = df.groupby([variableInteres, 'Customer_ID'])[variableFiltro].sum().reset_index()

    # Agrupar por el interés y sumar las compras
    df_total = df_suma.groupby(variableInteres)[variableFiltro].sum().reset_index()

    # Crear el gráfico de torta
    fig = px.pie(
        df_total,
        names=variableInteres,
        values=variableFiltro,
        title=titulo
    )
    fig.show()


graficoTorta('Shipping_Method', 'Total_Purchases', 'Gráfico Shipping Method por compras de cliente')


print('''Preferencia por Envíos Rápidos: La mayoría de los clientes prefieren métodos de envío rápidos 
("Same-Day" y "Express"), sumando un 68.5% del total de compras, lo que sugiere una tendencia hacia la necesidad 
de recibir los productos rápidamente.
Implicaciones para la Logística: Las empresas deberían asegurar una logística eficiente para mantener la satisfacción 
del cliente, dado el alto porcentaje de pedidos que requieren envíos rápidos.''')


df['Product_Category'].unique()


#Porcentaje comprado por cada tipo de envio 


# H5. El Feedback permite entender a la satisfaccion del cliente. Podria ser una herramienta de clasificacion funcional.


#Debo contar los Feedback de cada TransactionID, de lo contrario estaria contando de mas las que estan repetidas.
df_unique_customers = df.drop_duplicates(subset='Transaction_ID')
age_summary = df_unique_customers.groupby('Feedback').size().reset_index(name='Number_of_Customers')

# Crear el gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(age_summary['Feedback'], age_summary['Number_of_Customers'], color='skyblue')

# Configurar el título y las etiquetas
plt.title('Cantidad de Clientes por Feedback')
plt.xlabel('Feedback')
plt.ylabel('Número de Clientes')

# Configurar las etiquetas del eje x para mostrar todas las edades
plt.xticks(ticks=age_summary['Feedback'], labels=age_summary['Feedback'].astype(str), rotation=90)

# Ajustar el diseño para que el texto sea visible
plt.tight_layout()

# Mostrar el gráfico
plt.show()


print('''Los clientes están en su mayoría muy satisfechos con el servicio. Sin embargo, hay un porcentaje elevado 
que lo considera malo o promedio. La satisfacción de los clientes es una de las razones más frecuentes por las que 
se ve afectado el churn. Estudiar este fenómeno con mayor profundidad y ofrecer programas de compensación podría ayudar 
a incentivar nuevas compras.''')


#No lo voy a usar para modelar


#H6. Las categorías de productos más compradas pueden indicar intereses y necesidades predominantes entre diferentes grupos 
# de compradores.

graficoTorta('Product_Category', 'Total_Purchases', 'Grafico Categoria de productos comprados por los clientes')

print('''El grafico revela que los clientes compran productos de una amplia variedad de categorias.
Esto genera que la empresa deba tener un inventario variado que pueda atender las necesidades de sus clientes y cuidar el
churn.
La diversidad en las compras podria indicar patrones especificos en los clientes y con eso una posible segmentacion 
de mercado, lo que permite a la empresa anticiparse a las necesidades de los clientes, ofreciendo los productos que mas les interesan
y disponibilizando promociones y descuentos. Conocer los segmentos permite al sector de marketing enfocar sus campa;as con mas
eficiencia y optimizar los recursos disponibilizando publicidades en los medios indicados.
Un inventario variado requiere una gestión eficiente de la cadena de suministro. Esto puede incluir la adopción de tecnologías avanzadas 
para el seguimiento de inventarios y la previsión de la demanda.
Ofrecer una variedad de productos puede mejorar la experiencia del cliente y aumenta las ventas al fomentar ventas adicionales.
La diversificacion de la oferta permite a la empresa una estabilidad financiera ya que la caida de ventas de un producto
puede verse compensada mediante el aumento de otro.''')


graficoTorta('Product_Category', 'Total_Amount_log', 'Grafico Categoria de productos gastados por los clientes')


total_purchases_by_category_shipping = df.groupby(['Product_Category', 'Shipping_Method'])['Total_Purchases'].sum().reset_index()

# Paso 2: Calcular el total de compras por categoría
total_purchases_by_category = df.groupby('Product_Category')['Total_Purchases'].sum().reset_index()
total_purchases_by_category.rename(columns={'Total_Purchases': 'Total_Purchases_Category'}, inplace=True)

# Paso 3: Unir los totales de cada categoría con el DataFrame agrupado por tipo de envío
df_merged = total_purchases_by_category_shipping.merge(total_purchases_by_category, on='Product_Category')

# Paso 4: Calcular el porcentaje de compras para cada tipo de envío dentro de cada categoría
df_merged['Percentage'] = (df_merged['Total_Purchases'] / df_merged['Total_Purchases_Category']) * 100

# Paso 5: Crear el gráfico de barras con porcentajes
plt.figure(figsize=(12, 6))
sns.barplot(x='Product_Category', y='Percentage', hue='Shipping_Method', data=df_merged, ci=None)
plt.title('Porcentaje de Compras por Categoría y Método de Envío')
plt.xlabel('Categoría de Producto')
plt.ylabel('Porcentaje de Compras')
plt.legend(title='Método de Envío')
plt.xticks(rotation=45)  # Opcional: para mejorar la legibilidad de las etiquetas
plt.tight_layout()  # Ajusta el diseño para que todo el texto sea visible
plt.show()


print('''Del grafico se observa que en su mayoria los clientes prefieren metodos de envio rapido. 
Sin embargo, para la categoria Electronics los consumidores buscan en su mayoria que se haga el mimso dia o en forma expres, 
el metodo de envio Standard es el menos usado. Esto puede deberse a que los clientes no quieren tener incertidumbre 
en cuanto a su entrega, prefieren asegurarse que llegara ese dia y no tener que coordinar pero estan menos dispuestos 
que en otras categorias, a pagar un envio expres. Es probable que el importe de los articulos sea de mayor porte y 
por tanto prefieren ahorrar en el metodo de envio. Para esto podria ser oportuno ver en mas detalle el metodo de envio 
de los productos.''')


# Supongamos que df ya está definido con las columnas 'Product_Category', 'products', 'Shipping_Method', y 'Total_Purchases'

# Paso 1: Filtrar datos para la categoría Electronics
df_Electronics = df[df['Product_Category'] == 'Electronics']
total_purchases_Electronics = df_Electronics.groupby(['products', 'Shipping_Method'])['Total_Purchases'].sum().reset_index()

# Paso 2: Calcular el total de compras por producto
total_purchases_by_Electronics = df_Electronics.groupby('products')['Total_Purchases'].sum().reset_index()
total_purchases_by_Electronics.rename(columns={'Total_Purchases': 'Total_Purchases_products'}, inplace=True)

# Paso 3: Unir los totales de cada producto con el DataFrame agrupado por tipo de envío
df_merged = total_purchases_Electronics.merge(total_purchases_by_Electronics, on='products')

# Paso 4: Calcular el porcentaje de compras para cada tipo de envío dentro de cada producto
df_merged['Percentage'] = (df_merged['Total_Purchases'] / df_merged['Total_Purchases_products']) * 100

# Paso 5: Crear el gráfico de barras apiladas
products = df_merged['products'].unique()
shipping_methods = df_merged['Shipping_Method'].unique()

# Crear una matriz para las compras
matrix = pd.pivot_table(df_merged, values='Percentage', index='products', columns='Shipping_Method', fill_value=0)

# Crear el gráfico de barras apiladas
ax = matrix.plot(kind='bar', stacked=True, figsize=(25, 18))

plt.title('Porcentaje de Compras por Productos en la Categoría Electronics y Método de Envío')
plt.xlabel('Productos')
plt.ylabel('Porcentaje de Compras')
plt.xticks(rotation=90, fontsize=12)  # Rotar etiquetas x y ajustar el tamaño de la fuente
plt.legend(title='Método de Envío')
plt.tight_layout()  # Ajusta el diseño para que todo el texto sea visible

plt.show()


print('''Los productos que se compran unicamente con envio en el día o Express son los aires acondicionados. 
Esto puede deberse a compras de urgencia, por ejemplo una ola de calor en la que el cliente prefiere tener el articulo 
cuanto antes. Tambien puede deberse a la disponibilidad horaria, si son articulos que el cliente necesita y no quiere 
correr el riesgo de no estar cuando lo lleven, paga para asegurarse de que le sera entregado ese mismo dia o en un 
horario acotado con la opcion express. Otra explicacion puede ser promociones o descuentos en las que el cliente es 
incentivado a realizar la compra y solicitarlo con esos metodos de envio.''')


# Transormacion, pocentaje comprado por el cliente por categoria de producto


# H7. El Rating de productos permite entender porque los clientes compran determinados productos.

df.columns
# Agrupar por Product_Type y Ratings y sumar Total_Purchases
TotalComprado_TipoProducto = df.groupby(['products'])['Total_Purchases'].sum().reset_index(name='Total_Comprado')
TotalComprado_TipoProducto.head()
Cantidad_por_Rating = df.groupby(['Ratings', 'products'])['Transaction_ID'].nunique().reset_index(name='Clientes_por_Rating')
Cantidad_por_Rating.head()

df_grafico=TotalComprado_TipoProducto.merge(Cantidad_por_Rating, on='products', how='left')
df_grafico.head(10)

# Crear el gráfico de dispersión interactivo con plotly
fig = px.scatter(
    df_grafico,
    x='Clientes_por_Rating',
    y='Total_Comprado',
    color='Ratings',
    hover_name='products',  # Mostrar el nombre del producto al pasar el mouse
    size_max=100,
    title='Diagrama de Dispersión: Total Comprado vs Clientes por Rating'
)

# Personalizar etiquetas de los ejes
fig.update_layout(
    xaxis_title="Clientes por Rating",
    yaxis_title="Total Comprado",
    legend_title="Ratings",
    template="plotly_white"
)

# Mostrar el gráfico interactivo
fig.show()



print('''El grafico muestra si existe una relacion entre la cantidad comprada por los clientes en un determinado producto 
y el rating que le dan al producto. Seria de esperar que los productos mas comprados presenten Ratings mayores.
Se observa una tendencia de puntajes altos para los productos mas comprados, siendo el 4 y el 3 los valores mas presentes.
En todos los productos predomina el ranking 5, 4 y 3. Lo cual es favorable y brinda a los clientes mayor confianza al 
comprar los productos.''')

#Transformacion, poner el para el cliente cuantos productos compro en cada rating


# Ligadas a las características del usuario

# H7. El método de pago utilizado en la transacción es un factor determinante para analizar tipos de consumidores.

graficoTorta('Payment_Method', 'Total_Amount_log', 'Grafico Categoria de productos gastados por los clientes')

# La mayoria d elos clientes prefieren un metodo de pago online, rapido y eficiente.
# Visualizar por categoria y productos
print('''Del grafico de torta se desprende que la mayoria de los usuarios prefieren pagar con tarjeta de credito o debito
lo que podria dar lugar a promociones que ofrezcan beneficios adicionales al usar tarjetas de credito para incentivar
las ventas. La empresa podria asociarse con bancos y ofrecer promociones exclusivas a los clientes que usen tarjetas de credito
que provengan de dichos bancos. Lo mismo se podria considerer para las tarjetas de debito.
Sin emabrgo, hay un porcentaje importante de clientes que pagan en efectivo, por un lado la empresa se
ahorra la comision del banco pero por otro lado puede presentar un riesgo minimo, si el delivery llega a la direccion
del cliente y este no tiene el dinero, el costo del envio es un costo perdido. Lo que puede hacer la empresa para mitigar
este riesgo es ofrecer un descuento a los clientes que pagan en efectivo pero cobrar un importe mayor por el envio
para cubrir las perdidas del traslado. Tambien puede incentivar transferencia bancaria lo que evitaria el riesgo.
Pay pal es el metodo menos utilizado, podria deberse a que los clientes no estan familiarizados con su uso,
la empresa podria ofrecer ayudas o videos instructivos para incentivar el uso del mismo.''')

total_purchases_by_category_Payment_Method = df.groupby(['Product_Category', 'Payment_Method'])['Total_Amount_log'].sum().reset_index()

# Paso 2: Calcular el total de compras por categoría
Total_Amount_log_category = df.groupby('Product_Category')['Total_Amount_log'].sum().reset_index()
Total_Amount_log_category.rename(columns={'Total_Amount_log': 'Total_Amount_log_Category'}, inplace=True)

# Paso 3: Unir los totales de cada categoría con el DataFrame agrupado por tipo de envío
df_merged = total_purchases_by_category_Payment_Method.merge(Total_Amount_log_category, on='Product_Category')

# Paso 4: Calcular el porcentaje de compras para cada tipo de envío dentro de cada categoría
df_merged['Percentage'] = (df_merged['Total_Amount_log'] / df_merged['Total_Amount_log_Category']) * 100

# Paso 5: Crear el gráfico de barras con porcentajes
plt.figure(figsize=(12, 6))
sns.barplot(x='Product_Category', y='Percentage', hue='Payment_Method', data=df_merged, ci=None)
plt.title('Porcentaje de Compras por Categoría y Método de Pago')
plt.xlabel('Categoría de Producto')
plt.ylabel('Porcentaje de Compras')
plt.legend(title='Método de Pago')
plt.xticks(rotation=45)  # Opcional: para mejorar la legibilidad de las etiquetas
plt.tight_layout()  # Ajusta el diseño para que todo el texto sea visible
plt.show()


print('''Se destaca en la categoria Electronics el uso de Tarjeta de credito por ensima del resto de los metodos de pago.
Para los productos electronicos de mayor costo, la empresa podria ofrecer un sistema de financiamiento con tarjeta de credito,
incentivando asi las ventas.''')

#Transformacion, porcentaje comprado por el cliente por cada metodo



# H9. La frecuencia de compras puede revelar la lealtad del cliente y su comportamiento de compra recurrente.

frecuencia_comp_cliente = df.groupby('Customer_ID')['Transaction_ID'].nunique().reset_index()
frecuencia_comp_cliente.rename(columns={'Transaction_ID': 'frecuencia_comp_cliente'}, inplace=True)

# Paso 2: Unir esta información al DataFrame original
df = df.merge(frecuencia_comp_cliente, on='Customer_ID', how='left')


df62101=df[df['Customer_ID']==62101]
df62101.head()


plt.figure(figsize=(12, 6))
sns.histplot(df['frecuencia_comp_cliente'], bins=30)  # kde=True añade una estimación de la densidad
plt.title('Distribución de la Frecuencia de Compras de Clientes')
plt.xlabel('Número de Compras')
plt.ylabel('Número de Clientes')
plt.show()

print('''En este grafico se calcula primero cuantas compras ha realizado cada cliente, para graficar luego 
la frecuencia de cada cantidad comprada. Como se puede apreciar del grafico, la mayoria de los clientes han comprado 
entre 3 y 4 veces. Esto muestra que los clientes estan satisfechos y vuelven a utilizar la plataforma. Sin embargo, 
hay algunos clientes que han realizado hasta 8 o más compras, pero son mucho menos frecuentes. 
Esto sugiere un pequeño grupo de clientes muy leales o recurrentes. Se podria considerar un programa de fidelidad 
o recompensas para estos clientes frecuentes, ofreciendo incentivos para seguir comprando. Por ejemplo, un carrito de compras 
automatico para aquellos que compran Grocery.
Para los clientes que no han comprado mas de dos veces podria ser util observar el feedback que dieron, ya que puede deberse
a instaisfaccion o porque no fueron incentivados a realizar mas compras.''')

categories = df['Product_Category'].unique()

plt.figure(figsize=(14, 10))
for category in categories:
    # Filtrar por categoría
    df_category = df[df['Product_Category'] == category]

    # Crear un histograma para cada categoría
    sns.histplot(df_category['frecuencia_comp_cliente'], bins=30, label=category)

plt.title('Distribución de la Frecuencia de Compras por Categoría de Producto')
plt.xlabel('Número de Compras')
plt.ylabel('Número de Clientes')
plt.legend(title='Categoría de Producto')
plt.show()


print('''Como se puede apreciar del grafico, la mayoria de los clientes compran la categoria Clothing, 
seguido por Grocery y Electronics.
La empresa debe tener en consideracion el stock de productos dentro de estas categorias. Tambien podria considerar 
vender en conjunto alguno de estos, generando nuevas oportunidades de venta
y optimizacion de stock y envios.
Por ejemplo, cuando se compra ropa deportiva se pueden ofrecer productos electronicos de deportes o bebidas, alimentos 
o suplementos deportivos.''')


#Transformacion, poner la cantidad de compras realizadas por el cliente en la plataforma


# H10. El poder adquisitivo del cliente permite identificar patrones de consumo.

graficoTorta('Income', 'frecuencia_comp_cliente', 'Grafico income de los clientes')

print('''Se observa del grafico una alta presencia de clientes con ingresos medios. En el siguiente grafico vemos 
las cantidades compradas de cada categoria de producto por nivel de ingreso.''')


# H12. Las características demográficas del comprador, como edad, género, permiten segmentar a los 
# clientes en grupos específicos.

#Debo contar las edades de cada TransactionID, de lo contrario estaria contando de mas las que estan repetidas.
df_unique_customers = df.drop_duplicates(subset='Transaction_ID')
age_summary = df_unique_customers.groupby('Age').size().reset_index(name='Number_of_Customers')

# Crear el gráfico de barras
plt.figure(figsize=(14, 8))
plt.bar(age_summary['Age'], age_summary['Number_of_Customers'], color='skyblue')

# Configurar el título y las etiquetas
plt.title('Cantidad de Clientes por Edad')
plt.xlabel('Edad')
plt.ylabel('Número de Clientes')

# Configurar las etiquetas del eje x para mostrar todas las edades
plt.xticks(ticks=age_summary['Age'], labels=age_summary['Age'].astype(str), rotation=90)

# Ajustar el diseño para que el texto sea visible
plt.tight_layout()

# Mostrar el gráfico
plt.show()


print('''La edad de los clientes muestra que el grupo que mas compras han realizado es el grupo mas joven, de 
19 a 26. Entender los patrones de consumo de estos e incentivar futuras compras podria ser beneficioso para la empresa. 
Por otro lado, hay tramos de edades en los que las compras son muy constantes, se podria estudiar en mayor profunidad los 
intereses de estos para mejorar este mercado.''')

#GENERO

clientes_por_sexo = df.groupby('Gender')['Customer_ID'].nunique().reset_index(name='Total_Clientes')

# Calcular el porcentaje de clientes por género
clientes_por_sexo['Porcentaje'] = (clientes_por_sexo['Total_Clientes'] / clientes_por_sexo['Total_Clientes'].sum()) * 100

# Mostrar el DataFrame resultante
print(clientes_por_sexo)

# Crear un gráfico de barras para visualizar los porcentajes
plt.figure(figsize=(8, 6))
sns.barplot(x='Gender', y='Porcentaje', data=clientes_por_sexo, palette='pastel')

# Personalizar el gráfico
plt.title('Porcentaje de Clientes por Género')
plt.xlabel('Género')
plt.ylabel('Porcentaje')
plt.ylim(0, 100)
plt.grid(True)

# Mostrar el gráfico
plt.show()



print('''Los clientes se encuentran bastante equilibrados, pese a que hay mas hombres que mujeres.''')



gasto_por_sexo = df.groupby('Gender')['Total_Purchases'].sum().reset_index(name='Total_Comprado')

# Calcular el porcentaje de gasto por género
gasto_por_sexo['Porcentaje_comprado'] = (gasto_por_sexo['Total_Comprado'] / gasto_por_sexo['Total_Comprado'].sum()) * 100

# Mostrar el DataFrame resultante
print(gasto_por_sexo)

# Crear un gráfico de barras para visualizar el porcentaje de gasto por género
plt.figure(figsize=(8, 6))
sns.barplot(x='Gender', y='Porcentaje_comprado', data=gasto_por_sexo, palette='coolwarm')

# Personalizar el gráfico
plt.title('Porcentaje de compras por Género')
plt.xlabel('Género')
plt.ylabel('Porcentaje de compras')
plt.ylim(0, 100)
plt.grid(True)

# Mostrar el gráfico
plt.show()


print('''Del grafico se puede apreciar como los hombres compran mas articulos que las mujeres.''')


# Ligadas al contexto


# H13. La estacionalidad de las compras proporcionan información sobre preferencias estacionales y ciclos de compra.

df.head()

df47382=df[df['Customer_ID']==47382]
df47382.head()


df['Country'].unique()

df['Date'] = pd.to_datetime(df['Date'])

# Función para determinar la estación
def get_season(date, country):
    day_of_year = date.dayofyear
    
    if country in ['Australia']:  # Hemisferio Sur
        if 80 <= day_of_year < 172:
            return 'Otoño'
        elif 172 <= day_of_year < 264:
            return 'Invierno'
        elif 264 <= day_of_year < 355:
            return 'Primavera'
        else:
            return 'Verano'
    else:  # Hemisferio Norte
        if 80 <= day_of_year < 172:
            return 'Primavera'
        elif 172 <= day_of_year < 264:
            return 'Verano'
        elif 264 <= day_of_year < 355:
            return 'Otoño'
        else:
            return 'Invierno'

# Aplicar la función al DataFrame
df['Season'] = df.apply(lambda row: get_season(row['Date'], row['Country']), axis=1)



# Filtrar transacciones únicas por cliente, estación, categoría de producto y país
df_unique_customers = df.drop_duplicates(subset=['Transaction_ID', 'Season', 'Product_Category', 'Country'])

# Agrupar los datos por categoría de producto, estación y país para contar las compras únicas
country_season_summary = df_unique_customers.groupby(['Product_Category', 'Season', 'Country'])['Transaction_ID'].nunique().reset_index()
country_season_summary.rename(columns={'Transaction_ID': 'cantidad_compras'}, inplace=True)

# Crear el gráfico de barras apiladas
fig = px.bar(country_season_summary, 
             x='Product_Category', 
             y='cantidad_compras', 
             color='Season', 
             text='cantidad_compras',  # Añadir etiquetas de texto en las barras
             color_discrete_sequence=px.colors.qualitative.Set1,  # Opcional: cambiar la paleta de colores
             title="Cantidad de Compras por Categoría de Producto, Estación y País",
             facet_col='Country',  # Crear facetas por país
             barmode='stack')  # Establecer el modo de barras apiladas

# Mostrar el gráfico
fig.show()


print('''La estacion no parece ser influyente en las decisiones de compra de los usuarios, sin emabrgo, se percibe 
una diferencia entre las compras realizadas en cada uno de los paises, siendo USA el mercado mas grande, especialmente en 
Grocery y Electronics.''')

#Transformacion, dejar country y sacar season


# H14. Las horas y días de la semana, como el mes en que se realizan las compras pueden ofrecer información sobre los hábitos y comportamientos de compra.


df_unique_month = df.drop_duplicates(subset='Transaction_ID')
ax=df_unique_month['Month'].value_counts()\
    .plot(kind='barh', title='Cantidad de compras por mes')

ax.set_xlabel('Cantidad')
ax.set_ylabel('Mes')



plt.figure(figsize=(12, 6))
gender=sns.countplot(x='Month',data=df)


for bars in gender.containers:
    gender.bar_label(bars)

plt.title('Month Bar plot with Count')
plt.show()

# H15. El clima puede ser un factor determinante por el cual se dan determinadas compras.
# H16. El pais y la ciudad en la que se encuentra el cliente permite segmentar los clientes
# H17. El barrio ayuda a entender como clasificara  los clientes









############SEGUIR#################

total_purchases_by_category = df.groupby('Product_Category')['Total_Purchases'].sum().reset_index()
total_purchases_by_category.rename(columns={'Total_Purchases': 'Total_Purchases_Category'}, inplace=True)

# Unir los totales de cada categoría con el DataFrame original
df = df.merge(total_purchases_by_category, on='Product_Category')

# Calcular el porcentaje de compras para cada tipo de envío
df['Percentage'] = (df['Total_Purchases'] / df['Total_Purchases_Category']) * 100

# Crear el gráfico de barras con porcentajes
plt.figure(figsize=(12, 6))
sns.barplot(x='Product_Category', y='Percentage', hue='Shipping_Method', data=df, ci=None)
plt.title('Porcentaje de Compras por Categoría y Método de Envío')
plt.xlabel('Categoría de Producto')
plt.ylabel('Porcentaje de Compras')
plt.legend(title='Método de Envío')
plt.show()




#H7. El método de pago utilizado en la transacción es un factor determinante para analizar tipos de consumidores.

graficoTorta('Payment_Method', 'Total_Amount_log', 'Grafico Categoria de productos gastados por los clientes')

######### CAMBIAR LOS FILTROS POR .query ###################













#PROBAR ESTO

df_prueba = px.data.gapminder().query("country == 'Canada'")
#Age
fig = px.scatter(df.query("year==2007"), x="Age", y="Total_Purchases", size="Total_Amount_log", color="continent",
           hover_name="country", log_x=True, size_max=60)
fig.show()



grouped_df = df.groupby('products')['Total_Purchases'].sum().reset_index()

# Creamos el gráfico de barras
plt.figure(figsize=(60, 26))
sns.barplot(data=grouped_df, x='products', y='Total_Purchases', palette='viridis')
plt.title('Cantidad Comprada de Cada Product_Type')
plt.xlabel('Product_Type')
plt.ylabel('Cantidad Comprada')
plt.xticks(rotation=45)  # Rotar etiquetas del eje x si es necesario
plt.show()

plt.figure(figsize=(5, 5))
df['Product_Type'].value_counts().head(5).plot(kind='pie',  autopct='%1.1f%%')