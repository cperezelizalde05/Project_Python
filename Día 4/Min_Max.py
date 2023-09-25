#Ejemplo 1
menor = min(58,96,72,64,35)
print(menor)

#Ejemplo 2
min_palabras = min("Carlos","Juan", "Alberto")
print(min_palabras)

#Ejemplo 3
nombre = "Carlos"
print(min(nombre.lower()))

#Ejemplo 4 - Diccionarios
dic = {"c1":45, "c2":11}
print(min(dic)) #Se fija en la clave que alfabéticamente tenga el mínimo valor de letra
print(min(dic.values())) #me devuelve el menor valor en número

