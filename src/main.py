from test_import import limpieza_data


df=limpieza_data.dataFrame_limpiado()
df.head()

df_Retail_unique_copy=df.copy()
df_Retail_unique_copy = df_Retail_unique_copy[df_Retail_unique_copy['Transaction_ID'] == 4676558.0]
df_Retail_unique_copy.head(3)

print("Tamaño inicial del dataFrame " + str(df.size))