# Transformar variables
def transformarTipoVariable(columns_to_convert,dataFrame, tipo):
    for column in columns_to_convert:
        if column in dataFrame.columns:
            dataFrame[column] = dataFrame[column].astype(tipo)
        else:
            print(f"La columna '{column}' no existe en el DataFrame.")

# Obtener el tipo de un variable
def getTipoVariable(dataFrame, variable):
    tipo_dato = dataFrame[variable].dtype
    mensaje = "El tipo de dato de la columna '{}' es: {}".format(variable, tipo_dato)
    return mensaje


def revisarValores(dataFrame):
    resultado = {
        'columnas_con_nulos': {},
        'columnas_con_ceros': {}
    }

    for column in dataFrame.columns:
        num_nulos = dataFrame[column].isnull().sum()
        num_ceros = (dataFrame[column] == 0).sum()

        if num_nulos > 0:
            resultado['columnas_con_nulos'][column] = num_nulos
        if num_ceros > 0:
            resultado['columnas_con_ceros'][column] = num_ceros

    return resultado