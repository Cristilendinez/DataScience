## Ejercicio 8
## Escriba un programa en Python que imprima todos los números del 0 al 6,
#  excepto el 3 y el 6. Nota: use la declaración 'continuar'.

for i in range(6):
    if (i== 3 or i == 6) :
        continue
    print(i, end= " ")
print("\n")
