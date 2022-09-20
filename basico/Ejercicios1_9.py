# EJERCICIO 1

"""
    Decribe una variable con nombre "notas" que tenga el valor -3
    muestra su valor
"""

notas = -3
print("El valor de las notas es" , notas)


"""
    Imprime los valores de "s" es igual 25, de "y" es igual a 10, poniendo la siguiente salida:
    El valor de "s" es "valor de s" y el valor de y es "valor de y"
"""

s= 25
y = 10
print('el valor de s es ' + str(s) + ' y el valor de y es ' + str(y))

# EJERCICIO 3

"""
    Declarar una variable con nombre "name",
    que tenga el valor de Juan "El profesor"
"""

name= "Juan"
name_2= " El profesor"
print(name + name_2)

# EJERCICIO 4

"""
    Concatena las siguientes palabras formando un sola:
    Juan "El profesor"
"""
name= "Juan"
nombre_profesion= name+ " El profesor"
nombre_profesion

# EJERCICIO 5

"""
    Teniendo la siguientes palabras: no cuentes los días, haz que los días cuenten
     · Pon las primeras letras de cada palabra en mayúsculas
     · Pon todas las letras en mayúsculas
     · Pon todas las letras en minúculas
"""

string="no cuentes los días, haz que los días cuenten"
string_primera_letra= string.title()
print("The capitalized string is:",string_primera_letra )


string="no cuentes los días, haz que los días cuenten"
string_primera_letra= string.upper()
print("The capitalized string is:",string_primera_letra )

string="no cuentes los días, haz que los días cuenten"
string_primera_letra= string.lower()
print("The capitalized string is:",string_primera_letra )


# EJERCICIO 6

"""
    Realiza la suma de 26 y 35
    Realiza la multiplicación de 26 y 35
    Realiza la operación de 2 + 32 por 10
    Saca el resultado de 3 elevado a 9
    Redondea el resultado anterior a dos decimales
    Muestra de que tipo se trata
"""
a= 26
b= 35
print(a + b)
print(a * b)
print((a + b) *  10 )
print( 3 ^ 9)
str(a)
str(b)
