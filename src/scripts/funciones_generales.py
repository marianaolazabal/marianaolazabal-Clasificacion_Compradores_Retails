import os
from plots import estuadio_ingresos, genero_edad_ing, resultMensaje


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

#funcion agarra path del cvs data/
def pathToData():
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Sube dos niveles para llegar al directorio raíz del proyecto
    root_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))

    # Construye la ruta al archivo CSV en el directorio 'data'
    csv_path = os.path.join(root_dir, 'data', 'new_retail_data.zip')
    return csv_path



def analisisIngresos (df, genero, edad, pais):
    print(f"*******Grupo {genero} {edad} en {pais} con ingresos altos************")

    estuadio_ingresos(df, 'High', edad, pais)
    genero_edad_ing (df, genero, 'High', edad, pais)
    resultMensaje(genero, 'High', edad, pais)


    print(f"*******Grupo {genero} {edad} en {pais} con ingresos bajos************")

    estuadio_ingresos(df, 'Low', edad, pais)
    genero_edad_ing (df, genero, 'Low', edad, pais)
    resultMensaje(genero, 'Low', edad, pais)


    print(f"*******Grupo {genero} {edad} en {pais} con ingresos intermedios************")

    estuadio_ingresos(df, 'Indeterminate', edad, pais)
    genero_edad_ing (df, genero, 'Indeterminate', edad, pais)
    resultMensaje(genero, 'Indeterminate', edad, pais)


