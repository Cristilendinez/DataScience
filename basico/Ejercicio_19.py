# Ejercicio 1

"""
    Definir una función inversa() que calcule la inversion de una cadena. 
    Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse".
"""

def inversa(cadena):
    if len(cadena)== 0:
        return cadena
    else: 
        return inversa(cadena[1:])+ cadena[0]

cadena= "estoy probando" 
print("La cadena original es : ", end="")
print(cadena)

print("La cadena reversa es : ", end="")
print(inversa(cadena))

# Ejercicio 2

"""
    Definir una funcion es_palindromo() que reconoce palindromo 
    palabras  que tiene el mismo aspecto escritas invertidas), ejemplo: es_palindromo("radar")
    tendría que devolver True.
"""
cadena= "radar"
def palindromo(cadena):
    inicio = 0
    fin = len(cadena) - 1
    while cadena[inicio] == cadena[fin]:
        if inicio >= fin:
            return True
        inicio += 1
        fin -= 1
    return False
print(palindromo(cadena))


# Ejercicio 3

"""
    Definir una funcion superposicion() que tome dos listas y devuelva True si tiene al
    menos 1 elemento en común o devuelva False en caso contrario. Escribe la función usando el bucle for 
    aninado.
"""

def superposicion(lista1,lista2):
    for elemento1 in lista1:
        for elemento2 in lista2:
            if elemento1 == elemento2:
                return True
    return False
print(superposicion([96,88,105],[99,91,4]))


def superposicion(lista1,lista2):
    for elemento1 in lista1:
        for elemento2 in lista2:
            if elemento1 == elemento2:
                return True
    return False
print(superposicion([96,88,105],[99,91,105]))