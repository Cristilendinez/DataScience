"""
    Basándote en la teoría explicada en clase sobre Python
    realiza los siguientes ejercicios
"""

# EJERCICIO 1

"""
    Definir una función generar_n_caracteres() que tome un entero n
    y devuelva el caracter multiplicado por n.
    Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".
"""

def generar_n_caracteres(n, caracter):
    return n * caracter


# EJERCICIO 2

"""
    Definir un diagrama procedimiento() que tome una lista de números enteros
    e imprima un diagrama en la pantalla. Ejemplo: procedimiento([4, 9, 7])
    debería imprimir lo siguiente:
"""

def procedimiento(lista):
    for i in lista:
        print(i * "x")

procedimiento([4, 9, 7])

# EJERCICIO 3

"""
    Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga.
"""

def mas_larga(lista):
    mas_larga = ""
    for i in lista:
        if len(i) > len(mas_larga):
            mas_larga = i
    return mas_larga

print(mas_larga(["coche", "tortuga", "bici"]))

# EJERCICIO 4

"""
    Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n,
    y devuelva las palabras que tengan mas de n caracteres.
"""

def filtrar_palabras(lista, n):
    for i in lista:
        if len(i) > n:
            print(i)

filtrar_palabras(["coche", "tortuga", "bici"], 4)

# EJERCICIO 5

"""
    Escribir un programa que ingrese una cadena de texto.
    El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.
"""

def contador_minusculas_mayusculas(cadena):
    contador= {'minusculas':0, 'mayusculas':0}
    
    for i in cadena:
        if i.isupper():
            contador['mayusculas']+=1
        elif i.islower():
            contador['minusculas']+=1
        
    return contador
frase= 'Que bonitas son las Flores en Primavera'
print(contador_minusculas_mayusculas(frase))

# EJERCICIO 6

"""
    Definir una tupla con 10 edades de personas.
        * Imprimir la cantidad de personas con edades superiores a 20.
"""

tupla = (23,23,46,3,2,54,23,34,24,64)
cantidad=0
for elemento in tupla:
    if elemento >20:
        cantidad = cantidad + 1
print("Cantidad de personas con edades superiores a 20")
print(cantidad)s

# EJERCICIO 7

"""
    Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a.
    También se puede hacer elegir al usuario la letra a buscar.  (Un poco mas emocionante)
"""

def main():
    # TODO: definir cuantos nombres quieres ingresar
    # TODO: definir una lista con el numero de elementos
    # TODO: pedir los nombres que pertenecen a la lista
    # TODO: definir por que letra comienza el nombre
    # TODO: imprimir la cantidad de nombres que empiezan por la letra
    pass

# EJERCICIO 8

"""
    Crear una función contar_vocales(),
    que reciba una palabra y cuente cuantas letras "a" tiene,
    cuantas letras "e" tiene y así hasta completar todas las vocales.
    Se puede hacer que el usuario sea quien elija la palabra.
"""

def contar_vocales(palabra):
    palabra_minuscula = palabra.lower()
    cant_a = 0
    cant_e = 0
    cant_i = 0
    cant_o = 0
    cant_u = 0

    for letra in palabra_minuscula:
        if letra == "a":
            cant_a = cant_a + 1
        elif letra == "e":
            cant_e = cant_e + 1
        elif letra == "i":
            cant_i = cant_i + 1
        elif letra == "o":
            cant_o = cant_o + 1
        elif letra == "u":
            cant_u = cant_u + 1

    print("Hay "+ str(cant_a)+ " a")
    print("Hay "+ str(cant_e)+ " e")
    print("Hay "+ str(cant_i)+ " i")
    print("Hay "+ str(cant_o)+ " o")
    print("Hay "+ str(cant_u)+ " u")



palabra = input("Escribe una palabra: ")
contar_vocales(palabra)




