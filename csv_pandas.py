import pandas as pd

def read_pandas(filepath,names):
    #Leer archivo csv con pandas, regresa un dataframe
    #Se agregan los valores dentro de la variable names para establecer encabezados
    df = pd.read_csv(filepath,names=names,)
    return df

if __name__ == "__main__":
    #Establecer el filepath del archivo
    filepath = './data/iris.data'
    #Encabezados
    names = ['sepal_length','sepal_width','petal_length','petal_width','class']
    #Obtener el dataframe
    df = read_pandas(filepath,names)
    #Utilizar función head para leer primeras cinco líneas
    print(df.head(5))

    # sepal_length = df['sepal_length'].to_list()
    # print(sepal_length)

    #Obtener primera combinación de columnas
    df['sl+pl'] = df['sepal_length']+df['petal_length']
    #Obtener seguna combinación de columnas
    df['sw*sl'] = df['sepal_width']*df['sepal_length']
    #Imprimir dataframe con combinaciones
    print(df.head())


    # df_filtered = df[df['sepal_length']>=5]
    # print(df_filtered)

    #La función describe nos ayuda a conocer muchos datos sobre las columnas del
    #dataframe, como la cantidad de filas, el promedio de las columnas el mínimo,
    #máximo, percentiles y los tipos de datos.
    
    print(df.describe())
