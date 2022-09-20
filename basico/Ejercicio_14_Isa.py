import  pandas  as  pd

# EJERCICIO 1

"""
    Cada número es la suma de los 2 anteriores:
    0-1-1-2-3-5-8-13-21-34...
    Se pide programar esa secuencia con Python.
    No un:
    Apendiza elementos hasta tener 10 primeros resultados.
    (los 10 números indicados desde 0 hasta 34)
    Si sabes hazlo de varias formas diferentes
"""

def fibonacci():
    L = [0, 1]
    while (len(L) < 10):
        L.append(L[-1] + L[-2])
    return L

# imprimir(fibonacci())



# EJERCICIO 2

# Cada número es la suma de los 2 anteriores:

#0-1-1-2-3-5-8-13-21-34...

# Se pide programar para los numeros de fibonacci mayores de 1000

# Primero muestra los valores de 0 hasta 1000000, crea una lista
# con ese listado crea una segunda lista con los mayores de 1000



# EJERCICIO 3

# Se pide crear un NUEVO dataframe para cada uno de los siguientes casos

# planteados y que están relacionados con el Titanic DataSet

# (antes debéis de cargar el archivo como df)

# 1) Leer el archivo train.csv del conjunto de datos titanic

df  =  pd . read_csv ("train.csv")
print(df)

# Descomentar para ejecutar:
# imprimir (df)

# 2) Crear un dataframe de nombre df_sobreviven refiriéndose a un dataframe en el que todos los pasajeros sobreviven
df.Survived.value_counts()
print(df.Survived.value_counts())


df_Survived = df[df["Survived"]== 1]
print(df_Survived.head(10))


    # NOTA: si al principio no estás seguro del resultado, puedes usar value_counts() para comprobar tu resultado
##Primero voy a ver las observaciones que tengo de vivos y muertos

# 3) Crear un dataframe de nombre df__no_sobreviven refiriéndose a un dataframe en el que NINGUNO de los pasajeros sobreviven
##Primero voy a ver las observaciones que tengo de vivos y muertos

df_No_Survived = df[df["Survived"]== 0]
print(df_No_Survived.head(10))

# 4) DataFrame de hombres que no sobrevivieron en el titanic
df_hombres_no_sobreviven = df[(df["Survived"]== 0) & (df["Sex"]=="male")]
print(df_hombres_no_sobreviven.shape)

# 5) DataFrame de hombres que si sobrevivieron en el titanic

# 6) DataFrame de mujeres que no sobrevivieron en el titanic

# 7) DataFrame de muj  