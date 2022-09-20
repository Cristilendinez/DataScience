import pandas as pd

# EJERCICIO 1

"""
    Describa una variable con nombre "notas" que tenga el valor -3
    muestra su valor
"""


def note(notas):
    print(notas)
notas= - 3

note(notas)

# EJERCICIO 2

"""
    Imprime los valores de "s" es igual 25, de "y" es igual a 10, poniendo la siguiente salida:
    El valor de "s" es "valor de s" y el valor de y es "valor de y"
"""
s= 25
y= 10


def imprimir(s, y):
    print(f'el valor de s es {s} y el valor de y es {y}')
    print('el valor de s es ' + str(s) + ' y el valor de y es ' + str(y))
    print('el valor de s es ', s, ' y el valor de y es ', y)
    print(f'el valor de s es %s y el valor de y es %s' %(s, y))

imprimir(s,y)

# EJERCICIO 3

"""
    Declarar una variable con nombre "name",
    que tenga el valor de Juan "El profesor"
"""

def name(nombre):
    print(nombre)
nombre= "Juan,  El Profesor"

name(nombre)

# EJERCICIO 4

"""
    Concatena las siguientes palabras formando un sola:
    Juan "El profesor"
"""

s1= "Juan"
s2= "El Profesor"

def concatenar(s1, s2):
    print(s1,s2)
concatenar(s1, s2)

# EJERCICIO 5

"""
    Teniendo la siguientes palabras: no cuentes los días, haz que los días cuenten
     · Pon las primeras letras de cada palabra en mayúsculas
     · Pon todas las letras en mayúsculas
     · Pon todas las letras en minúculas
"""

frase = "no cuentes los días, haz que los días cuenten"

def titulo(frase):
    print(frase.title())

def mayuscula(frase):
    print(frase.upper())

def minuscula(frase):
    print(frase.lower())

titulo(frase)
mayuscula(frase)
minuscula(frase)

# EJERCICIO 6

"""
    Realiza la suma de 26 y 35
    Realiza la multiplicación de 26 y 35
    Realiza la operación de 2 + 32 por 10
    Saca el resultado de 3 elevado a 9
    Redondea el resultado anterior a dos decimales
    Muestra de que tipo se trata
"""

num1= 26
num2= 35
num3= 2
num4= 32
num5= 10

def suma(num1,num2):
    print(num1 + num2)

def multiplicacion(num1,num2):
    print(num1 * num2)

def operacion(num3, num4, num5):
    print(2+(num4* num5 ))

suma(num1, num2)
multiplicacion(num1,num2)
operacion(num3, num4, num5)


