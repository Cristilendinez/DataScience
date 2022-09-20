## #Calcular la suma de los cuadrados de los n primeros numero naturales,
# teniendo en cuenta que los n numeros deben de ser positivios

n= int(input("Ingrese la cantidad de numeros naturales: "))

while n<=0:
    print("REl numero debe de ser positivos")
    n= int(input("Ingrese la cantidad de numeros naturales: "))

suma= 0
for i in range(1,n+1):
    elevar_cuadrados = i * i
    suma= suma + elevar_cuadrados
print("La suma de los n numeros naturales es: ", suma)

1.## Escribe un programa en Python para encontrar aquellos números que son divisibles por 7 
## y múltiplos de 5, entre 1500 y 2700 (ambos incluidos)

nl=[]
for x in range(1500, 2701):
    if (x%7==0) and (x%5==0):
        nl.append(str(x))
print (','.join(nl))


