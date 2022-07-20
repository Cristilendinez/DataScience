# EJERCICIO 1

"""
    Definir una función max()
    que tome como argumento dos numeros y devuelva el mayor de ellos.
    (Es cierto que python tiene una función incorporada max(),
    pero hacerla nosotros mismos es un muy buen ejercicio).
"""

def  funcion_max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
print(funcion_max(10,18))


# EJERCICIO 2

"""
    Definir una función max_de_tres(), 
    que tome tres números como argumentos y 
    devuelva el mayor de ellos.
"""

def max_de_tres(num1, num2,num3):
    if num1>num2 and num1 > num3:
        return num1
    elif num2>num1 and num2 >num3:
        return num2
    else:
        return num3

print(max_de_tres(89,56,980)) 

# EJERCICIO 3

"""
    Definir una función que calcule la longitud de una lista
    o una cadena dada.
    (Es cierto que python tiene la función len() incorporada,
    pero escribirla por nosotros mismos resulta un muy buen ejercicio.
"""

texto = "Que bonitas son las flores en primavera"
print(len(texto))#para comprobar su longitud

def calcular_longitud_cadena(cadena):
    contador = 0

    for i in cadena:
        contador +=1
    return contador
print(calcular_longitud_cadena(texto))




