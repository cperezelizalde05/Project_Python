#Ejemplo 1 sin numerador
lista = ["a", "b", "c"]
indice = 0
for item in lista:
    print(indice, item)
    indice +=1
#Ejemplo 2
lista2 = ["a", "b", "c"]
for item in enumerate(lista2):
    print(item)
#Ejemplo 3
lista = ["a", "b", "c"]
for indice1, item in enumerate(lista):
    print(indice1, item)
#Ejemplo 4
lista3 = ["a", "b", "c"]
mis_tuples = list(enumerate(lista3))
print(mis_tuples)

#Ejemplo 5
lista4 = ["a", "b", "c"]
mis_tuples2 = list(enumerate(lista4))
print(mis_tuples2[1])#esto es por si quiero acceder a mi tuple 1