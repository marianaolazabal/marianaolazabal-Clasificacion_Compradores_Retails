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
import io
import zipfile
#from test_import.funciones_generales import getTipoVariable
from funciones_generales import transformarTipoVariable,getTipoVariable, revisarValores, pathToData
import funciones_generales as funciones_generales
from plots import grafico_Histograma, grafico_qqPlot, graficoDisplot, graficoBoxPlot

#from uszipcode import SearchEngine, SimpleZipcode, Zipcode

##Referencia de dataset##
#Retail Analysis on Large Dataset
#https://www.kaggle.com/datasets/sahilprajapati143/retail-analysis-large-dataset


#llama a la funcion desde funciones_generales
csv_path = pathToData()
#print(f"CSV path: {csv_path}")
df_Retail = pd.read_csv(csv_path)

df_Retail.head()

print("Tamaño inicial del dataFrame " + str(df_Retail.size))

##Estudio univariable. Completitud, correctitud y consistencia

print("Columnas del dataFrame:")
print(df_Retail.columns)


pd.reset_option('display.max_columns')
pd.set_option('display.max_colwidth', None)  # No recorta el contenido de las celdas
pd.set_option('display.max_rows', None)      # Muestra todas las filas sin resumen
pd.set_option('display.max_columns', None) 

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
       'Customer_Segment','Feedback', 'Shipping_Method', 'Payment_Method'
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
df_Retail.columns
df_Retail.info()


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


df_Retail.size

# Paso 1: Identificar el país más frecuente para cada Customer_ID
df_mode_country = df_Retail.groupby('Customer_ID')['Country'].agg(lambda x: x.mode()[0]).reset_index()

# Paso 2: Unir el DataFrame original con el DataFrame del país más frecuente
df_Retail = pd.merge(df_Retail, df_mode_country, on='Customer_ID', suffixes=('', '_Most_Frequent'))

# Paso 3: Filtrar para quedarte solo con las filas donde el país coincida con el más frecuente
df_Retail = df_Retail[df_Retail['Country'] == df_Retail['Country_Most_Frequent']]

# Paso 4: Eliminar la columna Country_Most_Frequent si ya no la necesitas
df_Retail = df_Retail.drop(columns=['Country_Most_Frequent'])
df_Retail.head()
df_Retail_10000=df_Retail[df_Retail['Customer_ID']==80175]
df_Retail_10000.head()

df_Retail.size



# - State es el estado donde el cliente vive


df_Retail['State'].unique()

df_Retail_copy=df_Retail.copy()

geolocator = Photon(user_agent="geoapiExercises")

def validate_city_country(city, country):
    # Diccionario de equivalencias de nombres de países
    country_aliases = {
        "germany": "germany",
        "deutschland": "germany",
        # Agrega más equivalencias si es necesario
    }

    try:
        query = f"{city}, {country}"
        location = geolocator.geocode(query, timeout=10)

        if location:
            address_parts = location.address.split(', ')
            found_city = address_parts[0].strip() if len(address_parts) >= 2 else ""
            found_country = address_parts[-1].strip().lower()

            # Normalizar el país devuelto
            normalized_country = country_aliases.get(found_country, found_country)
            normalized_input_country = country_aliases.get(country.lower(), country.lower())

            # Guardar la dirección devuelta por la API
            api_response = location.address

            # Verificar coincidencia exacta
            if found_city.lower() == city.lower() and normalized_country == normalized_input_country:
                return api_response, api_response  # Coincidencia exacta
            else:
                return None, api_response  # No coinciden, pero guarda la respuesta de la API
        return None, None  # Si no se encuentra ninguna ubicación
    except GeocoderTimedOut:
        time.sleep(1)  # Espera un poco antes de reintentar
        return validate_city_country(city, country)


#print(validate_city_country('Montevideo','Uruguay'))

# Extract unique city-country pairs
unique_city_country_pairs = df_Retail[['City', 'Country']].drop_duplicates()
unique_city_country_pairs = unique_city_country_pairs.drop_duplicates()
# Apply the validation function to the unique city-country pairs
unique_city_country_pairs[['Validation', 'API_Response']] = unique_city_country_pairs.apply(
    lambda row: validate_city_country(row['City'], row['Country']), axis=1,
    result_type='expand'
)

print(f"Original dataframe shape: {df_Retail_copy.shape}")
print(f"Unique city-country pairs shape: {unique_city_country_pairs.shape}")

df_Retail_copy = df_Retail_copy.merge(unique_city_country_pairs, on=['City', 'Country'], how='left', suffixes=('', '_Validation'))
df_Retail_copy.head()
print(f"Dataframe shape after merge: {df_Retail_copy.shape}")
df_Retail_copy_Berlin=df_Retail_copy[df_Retail_copy['Country']=='Germany']
df_Retail_copy_Berlin.head()

# Rellenar los valores None en la columna 'Validation' con una cadena vacía
df_Retail_copy['Validation'] = df_Retail_copy['Validation'].fillna('')


def dividirColumna(row):

    if(row['Validation']==''):
        split_parts = row['API_Response'].split(',')
    
        # Asegúrate de que siempre se devuelvan 6 columnas
        return pd.Series({
            'Column1': split_parts[0].strip() if len(split_parts) > 0 else np.nan,
            'Column2': split_parts[1].strip() if len(split_parts) > 1 else np.nan,
            'Column3': split_parts[2].strip() if len(split_parts) > 2 else np.nan,
            'Column4': split_parts[3].strip() if len(split_parts) > 3 else np.nan,
            'Column5': split_parts[4].strip() if len(split_parts) > 4 else np.nan,
            'Column6': split_parts[5].strip() if len(split_parts) > 5 else np.nan
        })
    else:
        split_parts = row['Validation'].split(',')
    
        # Asegúrate de que siempre se devuelvan 6 columnas
        return pd.Series({
            'Column1': split_parts[0].strip() if len(split_parts) > 0 else np.nan,
            'Column2': split_parts[1].strip() if len(split_parts) > 1 else np.nan,
            'Column3': split_parts[2].strip() if len(split_parts) > 2 else np.nan,
            'Column4': split_parts[3].strip() if len(split_parts) > 3 else np.nan,
            'Column5': split_parts[4].strip() if len(split_parts) > 4 else np.nan,
            'Column6': split_parts[5].strip() if len(split_parts) > 5 else np.nan
        })


# Aplicar la función al DataFrame
result = df_Retail_copy.apply(dividirColumna, axis=1)

# Asegúrate de que el DataFrame original tiene las mismas columnas
df_Retail_copy[['Column1', 'Column2', 'Column3', 'Column4', 'Column5', 'Column6']] = result

df_Retail_copy.head()
df_Retail_copy['Column2'].unique()
df_Retail_copy['Column1'] = df_Retail_copy['Column1'].replace('Clarke City', 'Quebec City')
df_Retail_copy['Column1'] = df_Retail_copy['Column1'].replace('Albury Botanical Gardens', 'Albury')
df_Retail_copy['Column1'] = df_Retail_copy['Column1'].replace('United States Senate', 'Washington')
df_Retail_copy['Column1'] = df_Retail_copy['Column1'].replace('München', 'Munich')
df_Retail_copy['Column1'] = df_Retail_copy['Column1'].replace('Köln', 'Cologne')
df_Retail_copy['Column1'] = df_Retail_copy['Column1'].replace('Frankfurt am Main', 'Frankfurt')

df_Retail_copy['Column2'] = df_Retail_copy['Column2'].replace('2500', 'New South Wales')
df_Retail_copy['Column2'] = df_Retail_copy['Column2'].replace('4870', 'New South Wales')
df_Retail_copy['Column2'] = df_Retail_copy['Column2'].replace('6000', 'New South Wales')
df_Retail_copy['Column2'] = df_Retail_copy['Column2'].replace('N9A 1B2', 'Ontario')
df_Retail_copy['Column2'] = df_Retail_copy['Column2'].replace('4350', 'Queensland')
df_Retail_copy['Column2'] = df_Retail_copy['Column2'].replace('HU1 3DX', 'England')
df_Retail_copy.loc[(df_Retail_copy['Country'] == 'Canada') & (df_Retail_copy['Column2'] == 'N6A 3N7'), 'Column2'] = 'Ontario'
df_Retail_copy.loc[(df_Retail_copy['Country'] == 'United Kingdom') & (df_Retail_copy['Column2'] == 'N6A 3N7'), 'Column2'] = 'England'
df_Retail_copy['Column2'] = df_Retail_copy['Column2'].replace('2600', 'New South Wales')
df_Retail_copy['Column2'] = df_Retail_copy['Column2'].replace('3218', 'Victoria')
df_Retail_copy['Column2'] = df_Retail_copy['Column2'].replace('4740', 'Queensland')
df_Retail_copy['Column2'] = df_Retail_copy['Column2'].replace('BN1 1HH', 'England')
df_Retail_copy['Column2'] = df_Retail_copy['Column2'].replace('0800', 'Northern Territory')
df_Retail_copy['Column2'] = df_Retail_copy['Column2'].replace('2300', 'New South Wales')
df_Retail_copy['Column2'] = df_Retail_copy['Column2'].replace('3350', 'Victoria')
df_Retail_copy['Column2'] = df_Retail_copy['Column2'].replace('CF10 2AF', 'Wales')
df_Retail_copy['Column2'] = df_Retail_copy['Column2'].replace('G2 1DY', 'Scotland')
df_Retail_copy['Column2'] = df_Retail_copy['Column2'].replace('Sept-Îles', 'Quebec')
df_Retail_copy['Column2'] = df_Retail_copy['Column2'].replace('Wodonga Place', 'New South Wales')
df_Retail_copy['Column2'] = df_Retail_copy['Column2'].replace('Alba / Scotland', 'Scotland')
df_Retail_copy['Column2'] = df_Retail_copy['Column2'].replace('West Terraces and Steps', 'District of Columbia')
df_Retail_copy.loc[(df_Retail_copy['City'] == 'Hamburg') & (df_Retail_copy['Column2'] == 'Deutschland'), 'Column2'] = 'Schleswig-Holstein'
df_Retail_copy.loc[(df_Retail_copy['City'] == 'Berlin') & (df_Retail_copy['Column2'] == 'Deutschland'), 'Column2'] = 'Brandenburg'
df_Retail_copy['Column2'] = df_Retail_copy['Column2'].replace('United Kingdom', 'England')


df_Retail_copy = df_Retail_copy.drop(['Column3', 'Column4', 'Column5', 'Column6', 'City', 'State', 'Validation', 'API_Response'], axis=1)
df_Retail_copy = df_Retail_copy.rename(columns={'Column1': 'City', 'Column2': 'State'})
df_Retail_copy.head()

df_comb = df_Retail_copy[['City', 'Country', 'State']].drop_duplicates()
print(df_comb)

df_Retail_copy.loc[(df_Retail_copy['City'] == 'Cairns') & (df_Retail_copy['State'] == 'New South Wales'), 'State'] = 'Queensland'
df_Retail_copy.loc[(df_Retail_copy['City'] == 'Perth') & (df_Retail_copy['State'] == 'New South Wales'), 'State'] = 'Western Australia'
df_Retail_copy.loc[(df_Retail_copy['City'] == 'Toronto') & (df_Retail_copy['State'] == 'Toronto'), 'State'] = 'Ontario'
df_Retail_copy.loc[(df_Retail_copy['City'] == 'Wichita') & (df_Retail_copy['State'] == 'Texas'), 'State'] = 'Kansas'
df_Retail_copy.loc[(df_Retail_copy['City'] == 'Hamburg') & (df_Retail_copy['State'] == 'Schleswig-Holstein'), 'State'] = 'Hamburg'
df_Retail_copy.loc[(df_Retail_copy['City'] == 'Townsville') & (df_Retail_copy['State'] == '4810'), 'State'] = 'Queensland'
df_Retail_copy.loc[(df_Retail_copy['City'] == 'Charlotte') & (df_Retail_copy['State'] == 'Florida'), 'State'] = 'North Carolina'
df_Retail_copy.loc[(df_Retail_copy['City'] == 'Leicester') & (df_Retail_copy['State'] == 'LE1 5YA'), 'State'] = 'England'
df_Retail_copy.loc[(df_Retail_copy['City'] == 'Canberra') & (df_Retail_copy['State'] == 'New South Wales'), 'State'] = 'Australian Capital Territory'
df_Retail_copy.loc[(df_Retail_copy['City'] == 'Bendigo') & (df_Retail_copy['State'] == '3550'), 'State'] = 'Victoria'
df_Retail_copy.loc[(df_Retail_copy['City'] == 'Mesa') & (df_Retail_copy['State'] == 'Colorado'), 'State'] = 'Arizona'
df_Retail_copy.loc[(df_Retail_copy['City'] == 'Dresden') & (df_Retail_copy['State'] == 'Sachsen'), 'State'] = 'Saxony'
df_Retail_copy['City'] = df_Retail_copy['City'].replace('Québec', 'Quebec')


df_Retail_copy['City'].unique()
df_Retail_copy['State'].unique()
df_Retail_copy['Country'].unique()


# Eliminar espacios en blanco al principio y al final de cada nueva columna (opcional)
df_Retail_copy['City'] = df_Retail_copy['City'].str.strip()
df_Retail_copy['State'] = df_Retail_copy['State'].str.strip()
df_Retail_copy['Country'] = df_Retail_copy['Country'].str.strip()

df_Retail_copy.head()

#del df_Retail_copy
#gc.collect()


# - Zipcode es el codigo de la direccion del cliente

df_Retail_copy['Zipcode'].unique()


# - Age

print(getTipoVariable(df_Retail_copy, 'Age'))

# Verificar si hay clientes con edad menor a 18
underage_clients = (df_Retail_copy['Age'] < 18).any()

# Mostrar resultado
if underage_clients:
    print("Hay clientes cuya edad es menor a 18.")
else:
    print("No hay clientes cuya edad sea menor a 18.")

pd.set_option('display.max_columns', None) 


df_Retail_10000 = df_Retail_copy[df_Retail_copy['Customer_ID'] == 10000]
df_Retail_10000.head()

df_age_counts = df_Retail_copy.groupby('Customer_ID')['Age'].nunique().reset_index()
df_multiple_ages = df_age_counts[df_age_counts['Age'] > 1]

# Paso 2: Filtrar las filas con más de una edad distinta
df_filtered_multiple_ages = pd.merge(df_multiple_ages[['Customer_ID']], df_Retail_copy, on='Customer_ID', how='inner')

# Paso 3: Determinar la edad más frecuente para cada Customer_ID
df_mode_age = df_filtered_multiple_ages.groupby('Customer_ID')['Age'].agg(lambda x: x.mode()[0]).reset_index()

# Paso 4: Actualizar el DataFrame original con la edad más frecuente
df_Retail_updated = pd.merge(df_filtered_multiple_ages, df_mode_age, on='Customer_ID', suffixes=('', '_Most_Frequent'))

# Paso 5: Reemplazar la columna Age con el valor más frecuente
df_Retail_updated['Age'] = df_Retail_updated['Age_Most_Frequent']

# Paso 6: Eliminar la columna Age_Most_Frequent si ya no la necesitas
df_Retail_updated = df_Retail_updated.drop(columns=['Age_Most_Frequent'])

# Paso 7: Eliminar de df_Retail_cleaned las filas con Customer_ID que tienen múltiples edades
df_Retail_copy = df_Retail_copy[~df_Retail_copy['Customer_ID'].isin(df_multiple_ages['Customer_ID'])]

# Paso 8: Concatenar los DataFrames
df_Retail_final_customer = pd.concat([df_Retail_copy, df_Retail_updated], ignore_index=True)
 
# Paso 9: Visualizar los datos del Customer_ID 10000 (opcional)
df_Retail_10000 = df_Retail_final_customer[df_Retail_final_customer['Customer_ID'] == 10000]
df_Retail_10000.head()





# - Year

print(getTipoVariable(df_Retail_final_customer, 'Year'))
df_Retail_final_customer['Year'] = df_Retail_final_customer['Year'].astype('int')
print(getTipoVariable(df_Retail_final_customer, 'Year'))



# - Name --> Mail del cliente

# Elimino la columna porque no es estadisticamente necesaria
df_Retail_final_customer = df_Retail_final_customer.drop(columns=['Name'])

# - Email --> Mail del cliente

#Elimino la columna porque no es estadisticamente necesaria
df_Retail_final_customer = df_Retail_final_customer.drop(columns=['Email'])


# - Phone --> Phone del cliente
#Elimino la columna porque no es estadisticamente necesaria
df_Retail_final_customer = df_Retail_final_customer.drop(columns=['Phone'])


# - Gender

cantidadUnicos=df_Retail_final_customer['Gender'].nunique()
print("Hay solo", cantidadUnicos, "valores unicos de la variable genero y son Female and Male")

#Para un mismo cliente no puede haber amas de un genero

df_Retail_final_customer.size
df_Retail_10000=df_Retail_final_customer[df_Retail_final_customer['Customer_ID']==10000]
df_Retail_10000['Gender'].unique()
df_Retail_10000.head()

df_customer_counts = df_Retail_final_customer.groupby(['Customer_ID']).size().reset_index(name='counts')
df_multiple_genders_correct = df_customer_counts[df_customer_counts['counts'] > 2]
df_filtered = pd.merge(df_multiple_genders_correct[['Customer_ID']], df_Retail_final_customer, on='Customer_ID', how='inner')
df_Retail_cleaned = df_Retail_final_customer[~df_Retail_final_customer['Customer_ID'].isin(df_filtered['Customer_ID'])]

# Paso 1: Identificar los Customer_ID que tienen más de un Gender
df_gender_counts = df_filtered.groupby('Customer_ID')['Gender'].nunique().reset_index()
df_multiple_genders = df_gender_counts[df_gender_counts['Gender'] > 1]
df_filtered_multiple_gender = pd.merge(df_multiple_genders[['Customer_ID']], df_Retail_final_customer, on='Customer_ID', how='inner')

df_mode_gender = df_filtered_multiple_gender.groupby('Customer_ID')['Gender'].agg(lambda x: x.mode()[0]).reset_index()

# Paso 4: Actualizar el DataFrame original con el género más frecuente
df_Retail_updated = pd.merge(df_filtered_multiple_gender, df_mode_gender, on='Customer_ID', suffixes=('', '_Most_Frequent'))

# Reemplazar la columna Gender con el valor más frecuente
df_Retail_updated['Gender'] = df_Retail_updated['Gender_Most_Frequent']

# Eliminar la columna Gender_Most_Frequent si ya no la necesitas
df_Retail_updated = df_Retail_updated.drop(columns=['Gender_Most_Frequent'])
df_Retail_updated.size


df_final = pd.concat([df_Retail_cleaned, df_Retail_updated], ignore_index=True)
df_final.head()
df_Retail_10000=df_final[df_final['Customer_ID']==10000]
df_Retail_10000.head()


conteo_gender = df_final.groupby('Customer_ID')['Gender'].nunique().reset_index()
customer_ids_dos_gender = conteo_gender[conteo_gender['Gender'] == 2]['Customer_ID']
df_filtrado = df_final[~df_final['Customer_ID'].isin(customer_ids_dos_gender)]
df_final=df_filtrado.copy()

# - Income

cantidadUnicos=df_final['Income'].nunique()
print("Hay solo", cantidadUnicos, "valores unicos de la variable Income y son Low, High and Medium")



df_customer_counts = df_final.groupby(['Customer_ID']).size().reset_index(name='counts')
df_multiple_Income_correct = df_customer_counts[df_customer_counts['counts'] > 2]
df_filtered = pd.merge(df_multiple_Income_correct[['Customer_ID']], df_final, on='Customer_ID', how='inner')
df_Retail_cleaned = df_final[~df_final['Customer_ID'].isin(df_filtered['Customer_ID'])]

# Paso 1: Identificar los Customer_ID que tienen más de un Gender
df_Income_counts = df_filtered.groupby('Customer_ID')['Income'].nunique().reset_index()
df_multiple_genders = df_Income_counts[df_Income_counts['Income'] > 1]
df_filtered_multiple_Income = pd.merge(df_multiple_genders[['Customer_ID']], df_final, on='Customer_ID', how='inner')

df_mode_Income = df_filtered_multiple_Income.groupby('Customer_ID')['Income'].agg(lambda x: x.mode()[0]).reset_index()

# Paso 4: Actualizar el DataFrame original con el género más frecuente
df_Retail_updated = pd.merge(df_filtered_multiple_Income, df_mode_Income, on='Customer_ID', suffixes=('', '_Most_Frequent'))

# Reemplazar la columna Gender con el valor más frecuente
df_Retail_updated['Income'] = df_Retail_updated['Income_Most_Frequent']

# Eliminar la columna Gender_Most_Frequent si ya no la necesitas
df_Retail_updated = df_Retail_updated.drop(columns=['Income_Most_Frequent'])
df_Retail_updated.size


df_final = pd.concat([df_Retail_cleaned, df_Retail_updated], ignore_index=True)

df_final.head()
df_Retail_10000=df_final[df_final['Customer_ID']==10000]
df_Retail_10000.head()


conteo_income = df_final.groupby('Customer_ID')['Income'].nunique().reset_index()
customer_ids_dos_incomes = conteo_income[conteo_income['Income'] == 2]['Customer_ID']
df_filtrado_final = df_final[~df_final['Customer_ID'].isin(customer_ids_dos_incomes)]
df_final=df_filtrado_final.copy()
df_final.head()

# - Customer_Segment

cantidadUnicos=df_final['Customer_Segment'].nunique()
print("Hay solo", cantidadUnicos, "valores unicos de la variable Customer_Segment y son Premium, Regular and New")


# - Date --> Figura como mm/dd/yyyy

df_Retail_copy=df_final.copy()
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

unique_months = df_final['Month'].cat.categories

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

df_Retail_copy=df_final.copy()
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

df_final['Total_Purchases'].dtype
print("Verificar normalidad de los datos")
grafico_Histograma(df_Retail,"Total_Purchases","Total_Purchases","Total comprado","Frecuencia")

print("La variable Total_Purchases es normal, el rango va entre 1 a 10 cantidades compradas")


# - Total_Amount --> Total amount spent by the customer (calculated as Amount * Total_Purchases)

grafico_Histograma(df_final,"Total_Amount","Total_Amount","Total gastado","Frecuencia")

print("El histograma sugiere que los valores en la columna 'Total_Amount' están distribuidos de manera no uniforme, como se puede apreciar en el histograma la variable no presenta una distribución normal. Esto es un problema para realizar comparaciones estadísticas, por lo que es necesario normalizarla.")


#En el siguiente grafico se puede observar si la variable presenta o no una distribucion normal. 
# La linea roja es una linea teórica donde los datos siguen una distribución normal. 
# Si los puntos de la variable a estudiar se alinean aproximadamente a lo largo de la recta roja entonces se puede decir que es normal.

grafico_qqPlot(df_final,"Total_Amount")

print("Como se puede apreciar, los puntos se desvían significativamente de la línea roja, especialmente en los extremos, lo que sugiere que los datos de 'Total_Amount' no siguen una distribución normal.")

graficoDisplot(df_final,"Total_Amount")

print("La distribucion no sigue una funcion normal, por lo que es necesario la transformacion de la variable al logaritmo")

df_final['Total_Amount_log'] = np.log(df_final['Total_Amount'])
df_Retail_norm = df_final.drop(columns=['Total_Amount'])

#Verifico nuevamente el qqplot con la variable transformada

grafico_qqPlot(df_final,"Total_Amount_log")

print("Verificando la variable luego de la normalizacion, se observa que el problema persiste. Esto puede deberse a la presencia de valores atipicos. A continuacion se estudian estos.")

#Outliers

graficoBoxPlot(df_final, "Total_Amount_log", "Total_Amount_log", "Total_Amount_log")

print("Como se puede ver en el grafico, hay evidencia de valores atipicos. Sin embargo, es posible que estos tengan sentido para el analisis, por lo que optare por dejarlos y estudiar (en el EDA) en mayor profundidad si es conveniente sacarlos o dejarlos.")


# - Product_Category -->  Category of the purchased product.

cantidadUnicos=df_final['Product_Category'].nunique()

print("Hay solo", cantidadUnicos, "tipo de categorias.", "Estas son Electronics, Books, Home Decor, Grocery, Clothing")

#Verificar si existe y tiene sentido para un mismo producto tener distinta categoria

df_Retail_copy=df_final.copy()

grouped = df_Retail_copy.groupby('products')['Product_Category'].nunique()
productos_con_categorias_distintas = grouped[grouped > 1]

productos_con_categorias_distintas = productos_con_categorias_distintas.reset_index()
productos_con_categorias_distintas.columns = ['products', 'Unique_Category_Count']

print("Productos con categorías distintas:")
productos_con_categorias_distintas.head()

del df_Retail_copy
gc.collect()



# - Product_Brand --> Brand of the purchased product.

unique_ProductBrand = df_final['Product_Brand'].cat.categories
num_marcas = len(unique_ProductBrand)
print("Hay solo", num_marcas, "marcas.", "Estas son: Adidas, Apple, Bed Bath & Beyond, BlueStar, Coca-Cola, Penguin Books, Pepsi, Random House, Samsung, Sony, Whirepool, Zara")

# Algunos productos cuyo nombre contienen el nombre de la marca, tienen otro nombre en la columna marca, por lo tanto sustituyo
# la marca por la que existe en el nombre


# Mostrar los primeros registros para verificar
df_final.head()

pd.set_option('display.max_rows', None)  # Mostrar todas las filas

marca_producto = df_final.groupby('Product_Brand')['products'].unique()

# Mostrar las marcas y los productos únicos asociados
for marca, productos in marca_producto.items():
    print(f"Marca: {marca}")
    print(f"Productos: {', '.join(productos)}")
    print()


def cambioMarca(producto, marca):
    df_Retail_Electronics.loc[df_Retail_Electronics['products'].str.contains(producto, case=False, na=False), 'Product_Brand'] = marca

# Define los productos y marcas
productos = ['Samsung Galaxy','Samsung Galaxy Tab','Lenovo Tab','Lenovo ThinkPad','Razer Blade', 'Samsung Notebook', 'Acer Swift', 'Asus ZenBook', 'HP Spectre', 'Dell XPS', 
              'Huawei P', 'Amazon Fire Tablet', 'Google Pixel', 'LG Gram', 'Microsoft Surface Laptop', 
              'iPhone', 'LG G', 'Xiaomi Mi', 'Microsoft Surface', 'iPad', 'Asus ZenPad', 'Nokia', 
              'Huawei MediaPad', 'Acer Iconia Tab', 'Motorola Moto', 'Sony Xperia Tablet', 
              'Google Pixel Slate', 'OnePlus', 'Sony Xperia']
marcas = ['Samsung','Samsung','Lenovo','Lenovo','Razer', 'Samsung', 'Acer', 'Asus', 'HP', 'Dell', 'Huawei', 'Amazon', 'Google', 'LG', 
          'Microsoft', 'Apple', 'LG', 'Xiaomi', 'Microsoft', 'Apple', 'Asus', 'Nokia', 
          'Huawei', 'Acer', 'Motorola', 'Sony', 'Google', 'OnePlus', 'Sony']

# Crear el DataFrame de mapeo
df_mapping = pd.DataFrame({
    'products': productos,
    'Product_Brand': marcas
})

df_Retail_final = df_final.merge(df_mapping, on='products', how='left', suffixes=('', '_new'))

# Reemplazar 'Product_Brand' en df_Retail con los valores de 'Product_Brand_new'
df_Retail_final['Product_Brand'] = df_Retail_final['Product_Brand_new'].combine_first(df_Retail_final['Product_Brand'])

# Eliminar la columna temporal 'Product_Brand_new'
df_Retail_final = df_Retail_final.drop(columns='Product_Brand_new')

df_Retail_Electronics=df_Retail_final[df_Retail_final['Product_Category']=='Electronics']
df_Retail_Electronics.head(20)



# - Product_Type --> Type of the purchased product.


unique_tipo_productos = df_Retail_final['Product_Type'].cat.categories
num_tipo_productos = len(unique_tipo_productos)
print("Hay solo", num_tipo_productos, "tipos de productos. Estos son: Bathroom, Bedding, BlueStar AC, Children's, Chocolate, Headphones, Jacket, Jeans, Juice, Kitchen, Laptop, Lighting, Literature, Mitsubishi 1.5 Ton 3 Star Split AC, Non-Fiction, Shirt, Shoes, Shorts, Smartphone, Snacks, Soft Drink, T-shirt, Tablet, Television, Thriller, Tools, Water")


# - Feedback --> Feedback provided by the customer on the purchase.

unique_Feedback = df_Retail_final['Feedback'].cat.categories
num_feedback = len(unique_Feedback)
print("Hay solo", num_feedback, "tipos de feedback posibles.", "Estos son: Average, Bad, Excellent, Good")



# - Shipping_Method --> Method used for shipping the product.

unique_Shipping_Method = df_Retail_final['Shipping_Method'].cat.categories
num_Shipping_Method = len(unique_Shipping_Method)
print("Hay solo", num_Shipping_Method, "metodos de Shipping disponibles.", "Estos son: Express, Same-Day, Standard")


# - Payment_Method--> Method used for payment.

unique_Payment_Method = df_Retail_final['Payment_Method'].cat.categories
num_Payment_Method = len(unique_Payment_Method)
print("Hay solo", num_Payment_Method, "metodos de pago posibles.", "Estos son: Cash, Credit Card, Debit Card, PayPal")


# - Order_Status --> Status of the order (e.g., Pending, Processing, Shipped, Delivered).

unique_Order_Status = df_Retail_final['Order_Status'].cat.categories
num_Order_Status = len(unique_Order_Status)
print("Hay solo", num_Order_Status, "estatus posibles en las que pueden estar las ordenes.", "Estos son: Delivered, Pending, Processing, Shipped")


# Ratings --> ratings given by customers on different products.

unique_Ratings = df_Retail_final['Ratings'].unique()
num_Ratings = len(unique_Ratings)
print("Hay solo", num_Ratings, "posibles valores para Ratings.", "Estos son: 1, 2, 3, 4, 5")


# --> Products
df_Retail_final['products'] = df_Retail_final['products'].astype('category')

unique_Products = df_Retail_final['products'].cat.categories
num_Products = len(unique_Products)
print("Hay solo", num_Products, "productos distintos.")



def dataFrame_limpiado():
    return df_Retail_final

#guarda el csv en la carpeta data y lo zipea
csv_file_name = 'Limpiado.csv'
zip_file_path = csv_path + 'Limpiado.zip'
csv_buffer = io.StringIO()
df_Retail_final.to_csv(csv_buffer, index=False)

with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    # Move the pointer to the start of the buffer
    csv_buffer.seek(0)
    # Write the CSV buffer to the ZIP file
    zipf.writestr(csv_file_name, csv_buffer.getvalue())

# Optional: Close the buffer
csv_buffer.close()
print("Tamaño inicial del dataFrame " + str(df_Retail_final.size))


df_Retail_final.head()
df_Retail_final_10000=df_Retail_final[df_Retail_final['Customer_ID']==10000]
df_Retail_final_10000.head()
