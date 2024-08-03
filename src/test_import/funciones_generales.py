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
