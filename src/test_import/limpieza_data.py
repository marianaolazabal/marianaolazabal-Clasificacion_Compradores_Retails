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
#from test_import.funciones_generales import getTipoVariable
from funciones_generales import getTipoVariable
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

df_Retail_copy=df_Retail.copy()

df_Retail_copy.size


##Estudio univariable. Completitud, correctitud y consistencia

print(df_Retail.columns)

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
consistent_transaction_ids = set(df_Retail_copy['Transaction_ID'])  # Inicialmente todos los IDs son válidos
for column in columns_to_check:
    # Agrupar por Transaction_ID y verificar cuántos valores únicos hay
    consistency = df_Retail_copy.groupby('Transaction_ID')[column].nunique()
    
    # Identificar Transaction_ID donde el valor es consistente (solo un valor único de la columna)
    consistent_ids = consistency[consistency == 1].index
    
    # Intersección con IDs válidos actuales
    consistent_transaction_ids &= set(consistent_ids)


# Filtrar el DataFrame original para mantener solo los Transaction_IDs con valores consistentes en todas las columnas
df_Retail_copy = df_Retail_copy[df_Retail_copy['Transaction_ID'].isin(consistent_transaction_ids)]

df_Retail_copy.head()

df_Retail_unique_copy=df_Retail_copy.copy()
df_Retail_unique_copy = df_Retail_unique_copy[df_Retail_unique_copy['Transaction_ID'] == 4676558.0]
df_Retail_unique_copy.head(3)

# Cuntas veces se repite el cliente que compro mas veces

df_Retail_copy_unique=df_Retail_copy.copy()
max_compras = df_Retail_copy_unique['Customer_ID'].value_counts().max()
print("El cliente que compró más veces, lo hizo " + str(max_compras) + " veces")


# - City es la ciudad donde el cliente vive

# Paso a corroborar que la ciudad no tenga caracteres raros y que para una misma ciudad este escrito de forma diferente

df_Retail_copy_unique['City'].unique()
df_Retail_copy_unique['Country'].unique()

#Cambio USA y UK por su nombre completo
df_Retail_copy_unique['Country'] =df_Retail_copy_unique['Country'].replace('USA','United States')
df_Retail_copy_unique['Country'] =df_Retail_copy_unique['Country'].replace('UK','United Kingdom')

df_Retail_validate_country=df_Retail_copy_unique.copy()

df_Retail_validate_country = df_Retail_copy_unique[['City', 'Country']].drop_duplicates()
df_Retail_validate_country = df_Retail_validate_country.dropna()

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

df_Retail_validate_country['pais_valido'] = df_Retail_validate_country.apply(lambda row: validate_country(row['Country']), axis=1)


# Filtra las filas con resultados incorrectos en la validación
df_paises_incorrectos = df_Retail_validate_country[df_Retail_validate_country['pais_valido'] == False]
if(df_paises_incorrectos.empty):
    print("Todas los paises son correctos")
else:
    print(df_paises_incorrectos)



# - State es el estado donde el cliente vive


df_Retail_copy_unique['State'].unique()

df_Retail_copy_unique = df_Retail_copy_unique.dropna(subset=['State'])
df_Retail_copy_unique = df_Retail_copy_unique.dropna(subset=['City'])

df_Retail_validate_city_country=df_Retail_copy_unique.copy()

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
unique_city_country_pairs = df_Retail_validate_city_country[['City', 'Country']].drop_duplicates()
unique_city_country_pairs = unique_city_country_pairs.drop_duplicates()
# Apply the validation function to the unique city-country pairs
unique_city_country_pairs['Validation'] = unique_city_country_pairs.apply(
    lambda row: validate_city_country(row['City'], row['Country']), axis=1
)


print(f"Original dataframe shape: {df_Retail_validate_city_country.shape}")
print(f"Unique city-country pairs shape: {unique_city_country_pairs.shape}")

df_Retail_validate_city_country = df_Retail_validate_city_country.merge(unique_city_country_pairs, on=['City', 'Country'], how='left', suffixes=('', '_Validation'))

print(f"Dataframe shape after merge: {df_Retail_validate_city_country.shape}")


# Filtra las filas con resultados incorrectos en la validación
df_incorrectas = df_Retail_validate_city_country[df_Retail_validate_city_country['Validation'].isna()]
if(df_incorrectas.empty):
    print("Todas las ciudades son correctas")
else:
    print(df_incorrectas)



# - Zipcode es el codigo de la direccion del cliente


nan_count = df_Retail_copy_unique['Zipcode'].isna().sum()
print("Hay " + str(nan_count) + " valores nulos para la variable Zipcode")

df_Retail_copy_unique = df_Retail_copy_unique.dropna(subset=['Zipcode'])

df_Retail_copy_unique['Zipcode'] = df_Retail_copy_unique['Zipcode'].round(0)
df_Retail_copy_unique['Zipcode'] = df_Retail_copy_unique['Zipcode'].astype(int)

#Columnas con valores faltantes
df_Retail_copy_unique.isna().sum().sum() # number of missing cells
print("El " + str(round(df_Retail_copy_unique.isna().sum().sum() / df_Retail_copy_unique.size * 100, 1)) + " % de los datos son faltantes") # percentage of missing cells

# Por mayor comodidad, transformo todas las variables a category menos las numericas

columns_not_to_convert = ['Age', 'Zipcode','Total_Purchases', 'Amount', 'Total_Amount', 'Ratings', 'Customer_ID', 'Transaction_ID']
all_columns = set(df_Retail_copy_unique.columns)

columns_not_to_convert_set = set(columns_not_to_convert)
columns_to_skip = list(all_columns - columns_not_to_convert_set)

# Convertir las columnas restantes a tipo 'category'
for col in columns_to_skip:
    df_Retail_copy_unique[col] = df_Retail_copy_unique[col].astype('category')



# - Age

print("Unique values of Age")
df_Retail_copy_unique['Age'].unique()

print(getTipoVariable(df_Retail_copy_unique, 'Age'))

df_Retail_copy_unique = df_Retail_copy_unique.dropna(subset=['Age'])
#Transformo Age a un int
df_Retail_copy_unique['Age'] = df_Retail_copy_unique['Age'].astype('int')
print(getTipoVariable(df_Retail_copy_unique, 'Age'))

df_Retail_verificarAge=df_Retail_copy_unique.copy()
# Verificar si hay clientes con edad menor a 18
underage_clients = (df_Retail_verificarAge['Age'] < 18).any()

# Mostrar resultado
if underage_clients:
    print("Hay clientes cuya edad es menor a 18.")
else:
    print("No hay clientes cuya edad sea menor a 18.")


# - Year

df_Retail_copy_unique = df_Retail_copy_unique.dropna(subset=['Year'])
print(getTipoVariable(df_Retail_copy_unique, 'Year'))
df_Retail_copy_unique['Year'] = df_Retail_copy_unique['Year'].astype('int')
print(getTipoVariable(df_Retail_copy_unique, 'Year'))


#Quiero borrar todos los valores nulos o nan pero quiero estudiar primero si me conviene borrar las filas o una columna entera,
# porque si los datos faltantes estan en su mayoria en una columna puede ser mejor deshacerme de esa columna en lugar de borrar registros.
#A continuacion estudio cual es la variable que tiene la mayor cantidad de nulos o valores nan

# Calcular el número de valores NaN por columna
nan_counts = df_Retail_copy_unique.isna().sum()
max_nan_count = nan_counts.max()

print("La columna con la mayor cantidad de números NaN tiene un total de", max_nan_count, "valores. Esta cantidad es pocos datos por lo que no voy a borrar columnas por el momento")



# - Name --> Mail del cliente

# Elimino la columna porque no es estadisticamente necesaria
df_Retail_copy_unique = df_Retail_copy_unique.drop(columns=['Name'])

# - Email --> Mail del cliente

#Elimino la columna porque no es estadisticamente necesaria
df_Retail_copy_unique = df_Retail_copy_unique.drop(columns=['Email'])


# - Phone --> Phone del cliente
#Elimino la columna porque no es estadisticamente necesaria
df_Retail_copy_unique = df_Retail_copy_unique.drop(columns=['Phone'])


# - Gender

df_Retail_verificarGender=df_Retail_copy_unique.copy()
cantidadUnicos=df_Retail_verificarGender['Gender'].nunique()
print("Hay solo", cantidadUnicos, "valores unicos de la variable genero y son Female and Male")


# - Income

df_Retail_verificarIncome=df_Retail_copy_unique.copy()
cantidadUnicos=df_Retail_verificarIncome['Income'].nunique()
print("Hay solo", cantidadUnicos, "valores unicos de la variable Income y son Low, High and Medium")


# - Customer_Segment

df_Retail_verificarCustomer_Segment=df_Retail_copy_unique.copy()
cantidadUnicos=df_Retail_verificarCustomer_Segment['Customer_Segment'].nunique()
print("Hay solo", cantidadUnicos, "valores unicos de la variable Customer_Segment y son Premium, Regular and New")


# - Date --> Figura como mm/dd/yyyy

df_Retail_verificarDate=df_Retail_copy_unique.copy()
num_rows_df_Retail_copy_unique = df_Retail_copy_unique.shape[0]
print(f"Number of rows: {num_rows_df_Retail_copy_unique}")

#Verfico que solo hay datos para el 2023 y 2024
df_Retail_verificarDate['Date'] = pd.to_datetime(df_Retail_verificarDate['Date'], errors='coerce')
df_Retail_verificarDate['Extracted_Year'] = df_Retail_verificarDate['Date'].dt.year
df_Retail_verificarDate['Year_Match'] = df_Retail_verificarDate['Extracted_Year'] == df_Retail_verificarDate['Year']

num_rows = df_Retail_verificarDate.shape[0]
print(f"Number of rows: {num_rows}")

print("Hay" , df_Retail_verificarDate['Date'].isna().sum() , "valores na")

df_2023 = df_Retail_verificarDate[df_Retail_verificarDate['Year'] == 2023]
df_2024 = df_Retail_verificarDate[df_Retail_verificarDate['Year'] == 2024]


# Extrae el mes de la columna 'Year'
df_2023.loc[:, 'Month'] = df_2023['Date'].dt.month
valores_unicos_mes_2023 = sorted(df_2023['Month'].unique())
nombres_meses_2023 = [calendar.month_name[mes] for mes in valores_unicos_mes_2023]
print("Los meses para el año 2023 son", nombres_meses_2023)

df_2024.loc[:, 'Month'] = df_2024['Date'].dt.month
valores_unicos_mes_2024 = sorted(df_2024['Month'].unique())
nombres_meses_2024 = [calendar.month_name[mes] for mes in valores_unicos_mes_2024]
print("Los meses para el año 2024 son", nombres_meses_2024)


# Controles generales


total_rows_before = df_Retail_copy_unique.shape[0]

# Eliminar todas las filas que contienen al menos un NaN en alguna columna
df_Retail_copy_unique = df_Retail_copy_unique.dropna()

# Contar las filas después de eliminar NaN
total_rows_after = df_Retail_copy_unique.shape[0]

# Calcular cuántas filas se eliminaron
rows_deleted = total_rows_before - total_rows_after

# Mostrar resultados
print("Número total de filas antes de eliminar NaN:", total_rows_before)
print("Número total de filas después de eliminar NaN:", total_rows_after)
print("Número de filas eliminadas:", rows_deleted)




df_Retail_copy_unique['Total_Amount'] = df_Retail_copy_unique['Total_Amount'].round(2)
df_Retail_copy_unique['Amount'] = df_Retail_copy_unique['Amount'].round(2)
df_Retail_copy_unique['Total_Purchases'] = df_Retail_copy_unique['Total_Purchases'].round(2)






def dataFrame_limpiado():
    return df_Retail_copy_unique

