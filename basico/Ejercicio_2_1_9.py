# EJERCICIO 1

"""
   Dado el siguiente listado: ["Python", "Matlab", "R", "VBA", "Julia", "C++"].
    Modifique con un algoritmo este listado.
    Cuando encuentre Python debe poner un 1
    y cuando encuentre otro lenguaje de programacion, un 0
    es un simple ejemplo de modificación de valores en una lista.
"""
items = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def replaceiniter(it, predicate, replacement=None):
     for item in it: 
        if predicate(item):
            yield replacement 
        else: 
            yield item


