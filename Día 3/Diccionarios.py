diccionario = {"c1":"valor1", "c2": "valor2"}
print(type(diccionario))
print(diccionario)
resultado = diccionario["c1"]
print(resultado)
cliente = {"nombre": "Carlos", "apellido": "Pérez Elizalde", "peso": 83, "talla": 1.71}
consulta = (cliente["apellido"])
print(consulta)

dic = {"c1":55, "c2": [10,20,30], "c3":{"s1":100, "s2":200}}#concatenación
print(dic["c2"][1])
print(dic["c3"]["s2"])

dic2 = {"c1":["a", "b", "c"], "c2":["d", "e", "f"]}
print(dic2["c2"][1].upper())

dic3 = {1:"a", 2:"b"}# Agregar una clave a este diccionario
print(dic3)
dic3[3]="c"
print(dic3)
dic3[2]="B"
print(dic3)
#Conocer todas las claves que están incluidas en un diccionario.
print(dic3.keys())#trae todas las claves
print(dic3.values())#trae todos los valores
print(dic3.items())#trae todos los elementos que tiene el diccionario



