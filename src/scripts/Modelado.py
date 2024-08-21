import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
#from limpieza_data import dataFrame_limpiado 
from funciones_generales import pathToData
from datetime import datetime
from plots import plot_bar_graphs, grafico_Histograma
import gc
import plotly.express as px
import requests
import io
import zipfile

#TIENE QUE QUEDARME UNA TABLA CON UNA LINEA POR CLIENTEEEEEE

# Leo el dataset que obtuve de limpiar los datos en el archivo limpieza_data.py
csv_path = pathToData()
df =pd.read_csv(csv_path + 'Data_Modelar.zip')

#Informacion generica del dataframe
df.info()

#K-Means

#Nos quedamos unicamente con las variables cuantitativas.

