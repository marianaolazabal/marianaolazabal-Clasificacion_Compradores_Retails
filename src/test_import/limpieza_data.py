import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
import calendar
import requests #--pip install requests
#!pip install pycountry
#!pip install pyzipcode
import pycountry
import re
from pandas.plotting import scatter_matrix
from sklearn.model_selection import train_test_split # División del dataset
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from matplotlib.cm import ScalarMappable
from matplotlib.lines import Line2D
from geopy.geocoders import Photon
from geopy.exc import GeocoderTimedOut
from pyzipcode import ZipCodeDatabase
import statsmodels.api as sm
import os
import gc
#from test_import.funciones_generales import getTipoVariable
from funciones_generales import transformarTipoVariable,getTipoVariable, revisarValores
from plots import grafico_Histograma, grafico_qqPlot, graficoDisplot, graficoBoxPlot

#from uszipcode import SearchEngine, SimpleZipcode, Zipcode

##Referencia de dataset##
#Retail Analysis on Large Dataset
#https://www.kaggle.com/datasets/sahilprajapati143/retail-analysis-large-dataset


current_dir = os.path.dirname(os.path.abspath(__file__))

# Sube dos niveles para llegar al directorio raíz del proyecto
root_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))

# Construye la ruta al archivo CSV en el directorio 'data'
csv_path = os.path.join(root_dir, 'data', 'new_retail_data.csv')
#print(f"CSV path: {csv_path}")
df_Retail = pd.read_csv(csv_path)

df_Retail.head()

print("Tamaño inicial del dataFrame " + str(df_Retail.size))

##Estudio univariable. Completitud, correctitud y consistencia

print("Columnas del dataFrame:")
print(df_Retail.columns)



# Controles generales


#Quiero borrar todos los valores nulos o nan pero quiero estudiar primero si me conviene borrar las filas o una columna entera,
# porque si los datos faltantes estan en su mayoria en una columna puede ser mejor deshacerme de esa columna en lugar de borrar registros.
#A continuacion estudio cual es la variable que tiene la mayor cantidad de nulos o valores nan

# Calcular el número de valores NaN por columna
nan_counts = df_Retail.isna().sum()
max_nan_count = nan_counts.max()

print("La columna con la mayor cantidad de números NaN tiene un total de", max_nan_count, "valores. Esta cantidad es pocos datos por lo que no voy a borrar columnas sino filas con valores na")


total_rows_before = df_Retail.shape[0]

# Eliminar todas las filas que contienen al menos un NaN en alguna columna
df_Retail = df_Retail.dropna()

# Contar las filas después de eliminar NaN
total_rows_after = df_Retail.shape[0]

# Calcular cuántas filas se eliminaron
rows_deleted = total_rows_before - total_rows_after

# Mostrar resultados
print("Número total de filas antes de eliminar NaN:", total_rows_before)
print("Número total de filas después de eliminar NaN:", total_rows_after)
print("Número de filas eliminadas:", rows_deleted)

resultado = revisarValores(df_Retail)
print("Columnas con valores nulos:", resultado['columnas_con_nulos'])
print("Columnas con valores 0:", resultado['columnas_con_ceros'])




#Transformaciones de tipos
df_Retail['Total_Amount'] = df_Retail['Total_Amount'].round(2)
df_Retail['Amount'] = df_Retail['Amount'].round(2)
df_Retail['Total_Purchases'] = df_Retail['Total_Purchases'].round(2)

columns_to_convert_int = ['Transaction_ID', 'Customer_ID', 'Zipcode', 'Age','Total_Purchases', 'Amount', 'Total_Amount', 'Ratings']

transformarTipoVariable(columns_to_convert_int, df_Retail, int)

columns_to_convert_category = ['Address', 'City', 'State', 'Country', 'Gender', 'Income',
                      'Customer_Segment', 'Product_Category', 'Product_Brand', 'Product_Type', 'Feedback', 'Shipping_Method',
                      'Payment_Method', 'Order_Status', 'products', 'Date', 'Month', 'Time']

transformarTipoVariable(columns_to_convert_category, df_Retail, 'category')



#Una transaccion puede repetirse por los registros:
# Phone --> Puede tener mas de un telefono de contacto para una misma compra (El del cliente y el de la pareja)
# Total_Purchases --> Son las cantidades compradas de cada producto
# Amount --> Si un cliente compra 2 cantidades de un producto y 3 cantidades de otro, el TransactionID figura dos veces y el Amount va a ser distinto, segun el costo de cada producto
# Total_Amount --> Es el Total_Purchases*Amount 
# Product_Category --> Segun el producto comprado, la categoria sera distinta
# Product_Brand --> Segun el producto comprado, la marca sera distinta
# Product_Type --> Segun el producto comprado, el tipo de producto sera distinto
# Ratings --> Segun el producto comprado, el rating de ese producto va a ser distinto al de otros
# Products --> Si compra distintos productos, van a existir distintos registros



#Todas las demas variables deben ser constantes para una misma TransactionID

columns_to_check = [
       'Customer_ID', 'Name', 'Email', 'Address',
       'City', 'State', 'Zipcode', 'Country', 'Age', 'Gender', 'Income',
       'Customer_Segment', 'Date', 'Year', 'Month', 'Time',
       'Feedback', 'Shipping_Method', 'Payment_Method',
       'Order_Status'
]


# Encontrar Transaction_IDs consistentes para cada columna
consistent_transaction_ids = set(df_Retail['Transaction_ID'])  # Inicialmente todos los IDs son válidos
for column in columns_to_check:
    # Agrupar por Transaction_ID y verificar cuántos valores únicos hay
    consistency = df_Retail.groupby('Transaction_ID')[column].nunique()
    
    # Identificar Transaction_ID donde el valor es consistente (solo un valor único de la columna)
    consistent_ids = consistency[consistency == 1].index
    
    # Intersección con IDs válidos actuales
    consistent_transaction_ids &= set(consistent_ids)


# Filtrar el DataFrame original para mantener solo los Transaction_IDs con valores consistentes en todas las columnas
df_Retail = df_Retail[df_Retail['Transaction_ID'].isin(consistent_transaction_ids)]

df_Retail.head()

df_Retail_unique_copy = df_Retail[df_Retail['Transaction_ID'] == 4676558.0]
df_Retail_unique_copy.head(3)

# Cuntas veces se repite el cliente que compro mas veces

max_compras = df_Retail['Customer_ID'].value_counts().max()
print("El cliente que compró más veces, lo hizo " + str(max_compras) + " veces")


# - City es la ciudad donde el cliente vive

# Paso a corroborar que la ciudad no tenga caracteres raros y que para una misma ciudad este escrito de forma diferente

df_Retail['City'].unique()
df_Retail['Country'].unique()

#Cambio USA y UK por su nombre completo
df_Retail['Country'] = df_Retail['Country'].astype(str).replace({'USA': 'United States', 'UK': 'United Kingdom'})

df_Retail_copy=df_Retail.copy()

df_Retail_copy = df_Retail_copy[['City', 'Country']].drop_duplicates()
df_Retail_copy = df_Retail_copy.dropna()

def validate_country(country_name):
    try:
        # Validate by country name
       
        country = pycountry.countries.lookup(country_name)
        
        if(country_name==country.name):
           #print(country.name)
           pass
        else:
            print("No encontrado")
        return country.name
    except LookupError:
        return None

df_Retail_copy['pais_valido'] = df_Retail_copy.apply(lambda row: validate_country(row['Country']), axis=1)


# Filtra las filas con resultados incorrectos en la validación
df_paises_incorrectos = df_Retail_copy[df_Retail_copy['pais_valido'] == False]
if(df_paises_incorrectos.empty):
    print("Todas los paises son correctos")
else:
    print(df_paises_incorrectos)


del df_Retail_copy
gc.collect()




# - State es el estado donde el cliente vive


df_Retail['State'].unique()

df_Retail_copy=df_Retail.copy()

geolocator = Photon(user_agent="geoapiExercises")

def validate_city_country(city, country):
    try:
        # Ensure proper formatting of the query
        query = f"{city}, {country}"
        location = geolocator.geocode(query, timeout=10)
        if location and location.address:
            return location.address
        else:
            return None
    except GeocoderTimedOut:
        time.sleep(1)  # Wait a bit before retrying
        return validate_city_country(city, country)
    

print(validate_city_country('Montevideo','Uruguay'))

# Extract unique city-country pairs
unique_city_country_pairs = df_Retail[['City', 'Country']].drop_duplicates()
unique_city_country_pairs = unique_city_country_pairs.drop_duplicates()
# Apply the validation function to the unique city-country pairs
unique_city_country_pairs['Validation'] = unique_city_country_pairs.apply(
    lambda row: validate_city_country(row['City'], row['Country']), axis=1
)


print(f"Original dataframe shape: {df_Retail_copy.shape}")
print(f"Unique city-country pairs shape: {unique_city_country_pairs.shape}")

df_Retail_copy = df_Retail_copy.merge(unique_city_country_pairs, on=['City', 'Country'], how='left', suffixes=('', '_Validation'))

print(f"Dataframe shape after merge: {df_Retail_copy.shape}")


# Filtra las filas con resultados incorrectos en la validación
df_incorrectas = df_Retail_copy[df_Retail_copy['Validation'].isna()]
if(df_incorrectas.empty):
    print("Todas las ciudades son correctas")
else:
    print(df_incorrectas)

del df_Retail_copy
gc.collect()

# - Zipcode es el codigo de la direccion del cliente

df_Retail['Zipcode'].unique()


# - Age

print(getTipoVariable(df_Retail, 'Age'))

# Verificar si hay clientes con edad menor a 18
underage_clients = (df_Retail['Age'] < 18).any()

# Mostrar resultado
if underage_clients:
    print("Hay clientes cuya edad es menor a 18.")
else:
    print("No hay clientes cuya edad sea menor a 18.")


# - Year

print(getTipoVariable(df_Retail, 'Year'))
df_Retail['Year'] = df_Retail['Year'].astype('int')
print(getTipoVariable(df_Retail, 'Year'))



# - Name --> Mail del cliente

# Elimino la columna porque no es estadisticamente necesaria
df_Retail = df_Retail.drop(columns=['Name'])

# - Email --> Mail del cliente

#Elimino la columna porque no es estadisticamente necesaria
df_Retail = df_Retail.drop(columns=['Email'])


# - Phone --> Phone del cliente
#Elimino la columna porque no es estadisticamente necesaria
df_Retail = df_Retail.drop(columns=['Phone'])


# - Gender

cantidadUnicos=df_Retail['Gender'].nunique()
print("Hay solo", cantidadUnicos, "valores unicos de la variable genero y son Female and Male")


# - Income

cantidadUnicos=df_Retail['Income'].nunique()
print("Hay solo", cantidadUnicos, "valores unicos de la variable Income y son Low, High and Medium")


# - Customer_Segment

cantidadUnicos=df_Retail['Customer_Segment'].nunique()
print("Hay solo", cantidadUnicos, "valores unicos de la variable Customer_Segment y son Premium, Regular and New")


# - Date --> Figura como mm/dd/yyyy

df_Retail_copy=df_Retail.copy()
num_rows_df_Retail_copy = df_Retail_copy.shape[0]
print(f"Number of rows: {num_rows_df_Retail_copy}")

#Verfico que solo hay datos para el 2023 y 2024
df_Retail_copy['Date'] = pd.to_datetime(df_Retail_copy['Date'], errors='coerce')
df_Retail_copy['Extracted_Year'] = df_Retail_copy['Date'].dt.year
df_Retail_copy['Year_Match'] = df_Retail_copy['Extracted_Year'] == df_Retail_copy['Year']

df_year_mismatch = df_Retail_copy[~df_Retail_copy['Year_Match']]

if df_year_mismatch.empty:
    print("No hay valores False en la columna 'Year_Match'.")
else:
    print("Hay al menos un valor False en la columna 'Year_Match':")
    print(df_year_mismatch)

num_rows = df_Retail_copy.shape[0]
print(f"Number of rows: {num_rows}")

del df_Retail_copy
gc.collect()


# Month

unique_months = df_Retail['Month'].cat.categories

def verificarMeses():
    correct_months = ['April', 'August', 'December', 'February', 'January', 'July', 'June',
                      'March', 'May', 'November', 'October', 'September']

    # Iniciar el resultado con un mensaje predeterminado
    resultado = True

    # Verificar cada mes en unique_months
    for mes in unique_months:
        if mes not in correct_months:
            resultado = False
            break  # Salir del bucle si se encuentra un mes incorrecto

    return resultado


if(verificarMeses()):
    print("Todos los meses son correctos")



# - Time ---> Tiempo en el que se hizo la compra. El formato es hh:mm:ss

df_Retail_copy=df_Retail.copy()
df_Retail_copy['Time'].head(2)

time_pattern = re.compile(r'^\d{1,2}:\d{2}:\d{2}$')

# Función para verificar el formato de la hora
def verificar_formato_hora(time_str):
    return bool(time_pattern.match(time_str))

# Aplicar la función a la columna 'Time'
df_Retail_copy['Formato Correcto'] = df_Retail_copy['Time'].astype(str).apply(verificar_formato_hora)

# Verificar si todos los valores tienen el formato correcto
todos_correctos = df_Retail_copy['Formato Correcto'].all()
if(todos_correctos):
    print(f"Todos los valores tienen el formato correcto")
else:
    print("Hay valores incorrectos")

del df_Retail_copy
gc.collect()


# - Total_Purchases --> Cantidad de artículos comprados por el cliente

df_Retail['Total_Purchases'].dtype
print("Verificar normalidad de los datos")
grafico_Histograma(df_Retail,"Total_Purchases","Total_Purchases","Total comprado","Frecuencia")

print("La variable Total_Purchases es normal, el rango va entre 1 a 10 cantidades compradas")


# - Amount --> Total gastado en una compra. La elimino porque la columna Total_Amount es un producto entre 

df_Retail = df_Retail.drop(columns=['Amount'])


# - Total_Amount --> Total amount spent by the customer (calculated as Amount * Total_Purchases)

grafico_Histograma(df_Retail,"Total_Amount","Total_Amount","Total gastado","Frecuencia")

print("El histograma sugiere que los valores en la columna 'Total_Amount' están distribuidos de manera no uniforme, como se puede apreciar en el histograma la variable no presenta una distribución normal. Esto es un problema para realizar comparaciones estadísticas, por lo que es necesario normalizarla.")


#En el siguiente grafico se puede observar si la variable presenta o no una distribucion normal. 
# La linea roja es una linea teórica donde los datos siguen una distribución normal. 
# Si los puntos de la variable a estudiar se alinean aproximadamente a lo largo de la recta roja entonces se puede decir que es normal.

grafico_qqPlot(df_Retail,"Total_Amount")

print("Como se puede apreciar, los puntos se desvían significativamente de la línea roja, especialmente en los extremos, lo que sugiere que los datos de 'Total_Amount' no siguen una distribución normal.")

graficoDisplot(df_Retail,"Total_Amount")

print("La distribucion no sigue una funcion normal, por lo que es necesario la transformacion de la variable al logaritmo")

df_Retail['Total_Amount_log'] = np.log(df_Retail['Total_Amount'])
df_Retail_norm = df_Retail.drop(columns=['Total_Amount'])

#Verifico nuevamente el qqplot con la variable transformada

grafico_qqPlot(df_Retail,"Total_Amount_log")

print("Verificando la variable luego de la normalizacion, se observa que el problema persiste. Esto puede deberse a la presencia de valores atipicos. A continuacion se estudian estos.")

#Outliers

graficoBoxPlot(df_Retail, "Total_Amount_log", "Total_Amount_log", "Total_Amount_log")

print("Como se puede ver en el grafico, hay evidencia de valores atipicos. Sin embargo, es posible que estos tengan sentido para el analisis, por lo que optare por dejarlos y estudiar (en el EDA) en mayor profundidad si es conveniente sacarlos o dejarlos.")


# - Product_Category -->  Category of the purchased product.

cantidadUnicos=df_Retail['Product_Category'].nunique()

print("Hay solo", cantidadUnicos, "tipo de categorias.", "Estas son Electronics, Books, Home Decor, Grocery, Clothing")

#Verificar si existe y tiene sentido para un mismo producto tener distinta categoria

df_Retail_copy=df_Retail.copy()

grouped = df_Retail.groupby('products')['Product_Category'].nunique()
productos_con_categorias_distintas = grouped[grouped > 1]

productos_con_categorias_distintas = productos_con_categorias_distintas.reset_index()
productos_con_categorias_distintas.columns = ['products', 'Unique_Category_Count']

print("Productos con categorías distintas:")
productos_con_categorias_distintas.head()

del df_Retail_copy
gc.collect()



# - Product_Brand --> Brand of the purchased product.

unique_ProductBrand = df_Retail['Product_Brand'].cat.categories
num_marcas = len(unique_ProductBrand)
print("Hay solo", num_marcas, "marcas.", "Estas son: Adidas, Apple, Bed Bath & Beyond, BlueStar, Coca-Cola, Penguin Books, Pepsi, Random House, Samsung, Sony, Whirepool, Zara")


# - Product_Type --> Type of the purchased product.


unique_tipo_productos = df_Retail['Product_Type'].cat.categories
num_tipo_productos = len(unique_tipo_productos)
print("Hay solo", num_tipo_productos, "tipos de productos. Estos son: Bathroom, Bedding, BlueStar AC, Children's, Chocolate, Headphones, Jacket, Jeans, Juice, Kitchen, Laptop, Lighting, Literature, Mitsubishi 1.5 Ton 3 Star Split AC, Non-Fiction, Shirt, Shoes, Shorts, Smartphone, Snacks, Soft Drink, T-shirt, Tablet, Television, Thriller, Tools, Water")


# - Feedback --> Feedback provided by the customer on the purchase.

unique_Feedback = df_Retail['Feedback'].cat.categories
num_feedback = len(unique_Feedback)
print("Hay solo", num_feedback, "tipos de feedback posibles.", "Estos son: Average, Bad, Excellent, Good")



# - Shipping_Method --> Method used for shipping the product.

unique_Shipping_Method = df_Retail['Shipping_Method'].cat.categories
num_Shipping_Method = len(unique_Shipping_Method)
print("Hay solo", num_Shipping_Method, "metodos de Shipping disponibles.", "Estos son: Express, Same-Day, Standard")


# - Payment_Method--> Method used for payment.

unique_Payment_Method = df_Retail['Payment_Method'].cat.categories
num_Payment_Method = len(unique_Payment_Method)
print("Hay solo", num_Payment_Method, "metodos de pago posibles.", "Estos son: Cash, Credit Card, Debit Card, PayPal")


# - Order_Status --> Status of the order (e.g., Pending, Processing, Shipped, Delivered).

unique_Order_Status = df_Retail['Order_Status'].cat.categories
num_Order_Status = len(unique_Order_Status)
print("Hay solo", num_Order_Status, "estatus posibles en las que pueden estar las ordenes.", "Estos son: Delivered, Pending, Processing, Shipped")


# Ratings --> ratings given by customers on different products.

unique_Ratings = df_Retail['Ratings'].unique()
num_Ratings = len(unique_Ratings)
print("Hay solo", num_Ratings, "posibles valores para Ratings.", "Estos son: 1, 2, 3, 4, 5")


# --> Products


unique_Products = df_Retail['products'].cat.categories
num_Products = len(unique_Products)
print("Hay solo", num_Products, "productos distintos.")



def dataFrame_limpiado():
    return df_Retail

