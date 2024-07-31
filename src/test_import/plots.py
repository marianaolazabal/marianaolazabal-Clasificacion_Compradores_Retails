import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_Retail = pd.read_csv(r'C:\Users\mariana\Desktop\repos\Clasificacion_Compradores_Retails\data\new_retail_data.csv')


def grafico():
    sns.histplot(df_Retail['Total_Purchases'], kde=True)
    plt.title('Histograma de Total_Purchases')
    plt.xlabel('Total_Purchases')
    plt.ylabel('Frecuencia')
    plt.show()

