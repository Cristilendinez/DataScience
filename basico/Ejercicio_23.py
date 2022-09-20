# ejercicio 1

"""
    Desarrolla los siguientes ejercicios de POO:
   * Alumnos -> Es la clase.
   * __init__ -> Es el método init
   * nombre, edad, asignatura y nota son las propiedades
   * Instanciamos..
   * los posibles alumnos (alumno1, alumno2, alumno3..) --> son los "objetos"
   * y el.__init__ los inicializa
   A continuación se muestra la edad del alumno 2 y el alumno 3 y sus notas
"""


# Ejercicio 2

"""
    Escribir un programa que pregunte al usuario su edad
    y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

   
"""
from tarfile import PAX_NAME_FIELDS


edad = int(input("¿Cuántos años tienes? "))
for i in range(edad):
    print("Tienes " + str(i+1) + " años")
    


# Ejercicio 3

"""
    Escribir un programa que pida al usuario una palabra y
    luego muestre por pantalla una a una las letras de la palabra comenzando por la última.
"""

palabra = input("Introduce una palabra: ")
for i in range(len(palabra)-1, -1, -1):
    print(palabra[i])

# ejercicio 4

"""
    Escribir un programa que pregunte el nombre completo del usuario en la consola y
    después muestre por pantalla el nombre completo del usuario tres veces,
    una con todas las letras minúsculas,
    otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula.
    El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
"""
nombre = input("¿Cómo te llamas? ")
print(nombre.lower())
print(nombre.upper())
print(nombre.title())


# Ejercicio 5

"""
    Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extensión donde el prefijo es el código del país +34,
    y la extensión tiene dos dígitos (por ejemplo +34-913724710-56).
    Escribir un programa que pregunte por un número de teléfono con este formato
    y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
"""
telefono = input("Introduce un número de teléfono con el formato 34-913724710-56: ")
print('El número de teléfono es ', telefono[4:-3])# imprimo desde el numero 9 que tiene la posicion 4 y elimino los 3 ultimos con -3

# Ejercicio 6

"""
    Escribir un programa que pida al usuario que introduzca una frase en la consola y una voz,
    y después muestre por pantalla la misma frase pero con la vocal reemplazada en mayúsculas.
"""
string = input("Introduce una frase: ")
vocal = input("Introduce una vocal en minúscula:  ")
print(string.replace(vocal, vocal.upper()))

# ejercicio 7

"""
    Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales
    y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
"""
precio = input("Introduce el precio del producto con dos decimales:  ")
print(precio[:precio.find('.')], 'euros ', precio[precio.find('.')+1:], 'céntimos.')
# Ejercicio 8

"""
    Escribir programa que genere y muestre por pantalla un DataFrame con los datos de la tabla siguiente:
    Mes Ventas Gastos
    Enero 30500 22000
    Febrero 35600 23400
    Marzo 28300 18100
    Abril 33900 20700
"""

import pandas as pd
d = {"Mes": ["Enero", "Febrero", "Marzo", "Abril"],
     "Ventas": [30500, 35600, 28300, 33900],
     "Gastos": [22000, 23400, 18100, 20700]}

df = pd.DataFrame(d)
df

# ejercicio 9

"""
    Escribir una función que reciba un DataFrame con el formato del ejercicio anterior,
    una lista de meses, y devuelva el saldo (ventas - gastos) total en los meses indicados.
"""

# ejercicio 10

"""
    Escribir un programa que almacene las asignaturas de un curso
    (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista,
    pregunte al usuario la nota que ha sacado en cada asignatura,
    y después las muestre por pantalla con el mensaje "Has sacado ASIGNATURA la nota de NOTA"
    donde es cada una de las asignaturas de la lista y cada una de las correspondientes notas enviadas por el usuario.
"""