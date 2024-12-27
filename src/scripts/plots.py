import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import plotly.express as px
from mensajes import *

#current_dir = os.path.dirname(os.path.abspath(__file__))

# Sube dos niveles para llegar al directorio raíz del proyecto
#root_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))

# Construye la ruta al archivo CSV en el directorio 'data'
#csv_path = os.path.join(root_dir, 'data', 'new_retail_data.csv')
#print(f"CSV path: {csv_path}")
#df_Retail = pd.read_csv(csv_path)

#df_Retail = pd.read_csv(r'C:\Users\mariana\Desktop\repos\Clasificacion_Compradores_Retails\data\new_retail_data.csv')


def grafico_Histograma(dataFrame,variable,titulo,xlabel,ylabel):
    sns.histplot(dataFrame[variable], kde=True)
    plt.title(f'Histograma de {titulo}')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


def grafico_qqPlot(dataFrame, variable):
    stats.probplot(dataFrame[variable], dist="norm", plot=plt)
    plt.title('Diagrama Q-Q')
    plt.show()

def graficoDisplot(dataFrame, variable):
    sns.displot(dataFrame[variable], kde = True)


def graficoBoxPlot(dataFrame, variable, titulo, ylabel):
    sns.boxplot(y=dataFrame[variable])
    plt.title(f'Box Plot de {titulo}')
    plt.ylabel(ylabel)
    plt.show()


def plot_bar_graphs(dataFrame, variable):
    plt.figure(figsize=(15, 5))
    ax = sns.countplot(x=variable, data=dataFrame, order=dataFrame[variable].value_counts().index)
    ax.bar_label(ax.containers[0],rotation=45)
    plt.xlabel(variable, fontsize=15)
    plt.ylabel('Count', fontsize=15)
    plt.title(f'Bar Graph of {variable}', fontsize=20)
    plt.xticks(rotation=45, ha='right', fontsize=12)
    plt.show()

def barplot(df, var_x, var_y, var_hue):
   
   plt.figure(figsize=(10, 6))
   sns.barplot(x=var_x, y=var_y, hue=var_hue, data=df)
   
   plt.title(f'Porcentaje del {var_y} por Grupo de {var_x} y {var_hue}')
   plt.ylabel(f'Porcentaje del {var_y} Dentro de cada Grupo de {var_x}')
   plt.xlabel(f'Grupo de {var_x}')
   plt.legend(title=f'{var_hue}')
   plt.show()


def graficoGasto_cliente(df, cluster):
    df_grouped = df.groupby(['mapeo_income', 'mapeo_gender'])['TotalHistorico_GastadoCliente'].sum().reset_index()

    total_por_ingreso = df_grouped.groupby('mapeo_income')['TotalHistorico_GastadoCliente'].transform('sum')
    df_grouped['porcentaje_gasto'] = (df_grouped['TotalHistorico_GastadoCliente'] / total_por_ingreso) * 100

    barplot(df_grouped, 'mapeo_income', 'porcentaje_gasto', 'mapeo_gender')

    mensaje_graficoGasto_cliente(cluster)



def grafico_Edades_pais (df, cluster):
  # 1. Contar el número de personas por país y categoría de edad
  df_counts = df.groupby(['mapeo_country', 'mapeo_Categoria_Edad']).size().reset_index(name='Group_Count')

  # 2. Calcular el total de personas por país
  df_totals = df.groupby('mapeo_country').size().reset_index(name='Total')

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
      width=1000,
      height=800
  )


  fig.show()

  mensaje_grafico_Edades_pais(cluster)



def grafico_gastos_genero_edad(df, cluster):
  sns.boxplot(data=df, x="TotalHistorico_GastadoCliente", y="mapeo_gender", hue="mapeo_Categoria_Edad")

  mensaje_grafico_gastos_genero_edad(cluster)


def grafico_gastos_genero_ingreso(df, cluster):
  sns.boxplot(data=df, x="TotalHistorico_GastadoCliente", y="mapeo_gender", hue="mapeo_income")

  mensaje_grafico_gastos_genero_ingreso(cluster)




def grafico_productos_mas_comprados(df, cluster, categorias):

  df_long = pd.melt(df, id_vars=['mapeo_income'], value_vars=categorias,
                  var_name='Categoria', value_name='Cantidad_Comprada')
  
  barplot(df_long, 'mapeo_income', 'Cantidad_Comprada', 'Categoria')

  mensaje_grafico_productos_mas_comprados(cluster)




def grafico_dispersion_gastos_frecuencia(df, cluster):
  sns.scatterplot(
      data=df, x="TotalHistorico_CompradoCliente", y="TotalHistorico_GastadoCliente", hue="frecuencia_comp_cliente", size="frecuencia_comp_cliente",
      sizes=(20, 200), legend="full"
  )

  mensaje_grafico_dispersion_gastos_frecuencia(cluster)




def grafico_dispersion_Cant(df, var_x, var_y, cluster, tipo):
  sns.scatterplot(data=df, x=var_x, y=var_y)
  mensaje_grafico_dispersion_Cant(cluster,tipo)



def grafico_forma_pago(df, cluster):

  df_grouped = df.groupby(['mapeo_income', 'mapeo_gender'])[['Cash', 'Credit', 'Debit']].sum().reset_index()
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

  plt.show()

  mensaje_grafico_forma_pago(cluster)



def graficoEstacion(df, cluster):
  df_grouped_estacion = df.groupby(['mapeo_income', 'mapeo_gender'])[['Invierno', 'Otoño', 'Verano', 'Primavera']].sum().reset_index()
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

  plt.show()

  mensaje_graficoEstacion(cluster)



def graficoMomentoDia(df, cluster):
  df_grouped_momento = df.groupby(['mapeo_income', 'mapeo_gender'])[['madrugada', 'mañana', 'medioDia', 'noche', 'tarde']].sum().reset_index()
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

  plt.show()

  mensaje_graficoMomentoDia(cluster)


#A que hora compran estos grupos?

def genero_edad_Hora(df_usar,genero, pais, valor, cluster):
    df_usar_pais=df_usar[df_usar['mapeo_country']==pais]

    # Filtrar por categoría de edad
    df_cluster0_analisis_genero_hora = df_usar_pais[df_usar_pais['mapeo_Categoria_Edad'].isin([valor])]

    # Convertir a formato largo para obtener la frecuencia por cada momento del día
    df_long = df_cluster0_analisis_genero_hora.melt(value_vars=["madrugada", "mañana", "medioDia", "noche", "tarde"],
                                                   var_name="Hora", value_name="Frecuencia")

    # Sumar las frecuencias por hora para el gráfico de barras
    df_suma = df_long.groupby("Hora")["Frecuencia"].sum().reset_index()

    # Calcular los porcentajes
    total_frecuencia = df_suma["Frecuencia"].sum()
    df_suma["Porcentaje"] = (df_suma["Frecuencia"] / total_frecuencia) * 100

    # Crear gráfico de barras
    
    ax = sns.barplot(x="Hora", y="Porcentaje", data=df_suma)

    mensajeGenero_edad_Hora(pais, genero, valor, cluster)



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

#----------------------------------

def estuadio_ingresos (df, valor, edad, pais, genero, cluster):

   df_genero_pais= df[df['mapeo_country']==pais]
   df_genero_pais_ingreso= df_genero_pais[df_genero_pais['mapeo_income']==valor]
   df_genero_ingreso_edad= df_genero_pais_ingreso[df_genero_pais_ingreso['mapeo_Categoria_Edad']==edad]

   top_10 = top10(df_genero_ingreso_edad).sort_values(ascending=False).head(10)
   print("Top 10 de categorías más compradas:")
   print(top_10)
#----------------------------------




def genero_edad_ing (df, ingreso, edad, pais):

    filtroIngreso=df[df['mapeo_income']==ingreso]
    filtroIngreso_pais=filtroIngreso[filtroIngreso['mapeo_country']==pais]
    filtroIngresoCategoria=filtroIngreso_pais[filtroIngreso_pais['mapeo_Categoria_Edad']==edad]

    #como es el nivel de satisfaccion?
    df_counts = filtroIngresoCategoria.groupby(['mapeo_city', 'mapeo_satisfaction']).size().reset_index(name='Group_Count')

    # Crear el gráfico sunburst
    fig = px.sunburst(
        df_counts,
        path=['mapeo_city', 'mapeo_satisfaction'],
        values='Group_Count',
        title='Distribución de Transacciones por País y Mes'
    )

    # Mostrar el gráfico
    fig.show()

#--------------------------------------------------------------------------------------------------




def estudioPais(df, genero):

    print(f"******* Gráfica de distribución del grupo {genero} por país ************")
    ax = sns.countplot(x="mapeo_country", data=df)
    plt.show()

    # 5 países con más ventas
    top_paises = (
        df["mapeo_country"]
        .value_counts()
        .head(5)
        .index.tolist()
    )


def paisGenero(df, pais, genero, cluster):

    print(
        f"******* Gráfica de distribución del grupo {genero} en {pais} ************"
    )

    # Filtrar datos para Estados Unidos
    df = df[
        df["mapeo_country"] == pais
    ]

    # Calcular proporciones por categoría de edad
    proporciones = (
        df["mapeo_Categoria_Edad"]
        .value_counts(normalize=True)
        .sort_index()
    )

    # Crear un gráfico de barras para proporciones
    ax = sns.barplot(
        x=proporciones.index,
        y=proporciones.values,
        palette="viridis"
    )
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
    ax.set_ylabel("Proporción")
    ax.set_title(f"Distribución relativa por categoría de edad en {pais}")

    plt.show()

    mensajePaisGenero(cluster, pais, genero)