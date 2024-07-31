import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

current_dir = os.path.dirname(os.path.abspath(__file__))

# Sube dos niveles para llegar al directorio raíz del proyecto
root_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))

# Construye la ruta al archivo CSV en el directorio 'data'
csv_path = os.path.join(root_dir, 'data', 'new_retail_data.csv')
#print(f"CSV path: {csv_path}")
df_Retail = pd.read_csv(csv_path)

#df_Retail = pd.read_csv(r'C:\Users\mariana\Desktop\repos\Clasificacion_Compradores_Retails\data\new_retail_data.csv')


def grafico():
    sns.histplot(df_Retail['Total_Purchases'], kde=True)
    plt.title('Histograma de Total_Purchases')
    plt.xlabel('Total_Purchases')
    plt.ylabel('Frecuencia')
    plt.show()

#grafico()