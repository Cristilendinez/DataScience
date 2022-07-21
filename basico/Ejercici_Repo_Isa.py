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
    elif num1 == num2 == num3:
        return (num1,num2, num3)
    else:
        return num3

print(max_de_tres(1,1,1)) 


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


# EJERCICIO 4

"""
    Escribir una función que tome un carácter y devuelva True si es una vocal,
    de lo contrario devuelve False.
"""

def es_vocal(caracter):
    vocales=['a','e', 'i','o','u']
    if caracter in vocales:
        return True
    else:
        return False
print(es_vocal('a'))

# EJERCICIO 5

"""
    Escribir una función suma() y una función multip() que sumen y multipliquen
    respectivamente todos los números de una lista.
    Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
"""
def suma(lista):
    resultado= 0
    for i in lista:
        resultado = resultado +(i)
    print(resultado)

suma ([1,2,3,4])
    
    
def multiplicacion(lista):
    resultado = lista[0]
    i = 1
    while i in range(1,len(lista)):
        resultado = resultado *lista[i]
        i +=1
        print(resultado)
    
multiplicacion([1,2,3,4])







