# Obtener el tipo de un variable
def getTipoVariable(dataFrame, variable):
    tipo_dato = dataFrame[variable].dtype
    mensaje = "El tipo de dato de la columna '{}' es: {}".format(variable, tipo_dato)
    return mensaje
