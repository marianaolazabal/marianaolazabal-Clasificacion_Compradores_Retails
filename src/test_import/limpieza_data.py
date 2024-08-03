import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
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

df_Retail.size

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
    'Customer_ID', 'Address', 'City', 'State', 'Zipcode', 'Country', 'Age', 'Gender',
    'Income', 'Customer_Segment', 'Date', 'Month', 'Time',
    'Total_Amount', 'Shipping_Method', 'Payment_Method', 'Order_Status', 'Feedback'
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