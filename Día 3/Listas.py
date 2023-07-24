mi_lista = ["a", "b", "c"]
mi_lista2 = ["d", "e", "f"]
mi_lista3 = mi_lista + mi_lista2
mi_lista4 = ["g", "l", "a", "c"]
otra_lista = ["hola", 55, 66.1]
resultado1 = len(mi_lista) #indicar el largo
print(resultado1)
resultado2 = mi_lista[0] #extraer la posición 0
print(resultado2)
print(type(mi_lista), type(otra_lista))
resultado3 = mi_lista[0:2] #extraer la posición 0 a 2
print(resultado3)
print(type(mi_lista))
resultado1 = mi_lista [0:] #concatenación de strings
print(mi_lista+mi_lista2)

mi_lista3[0] = "alfa" #modifica el valor de cero
print(mi_lista3)

mi_lista3.append("g")#agregar elemento
print(mi_lista3)

mi_lista3.pop(0)#si le dejo vacío () elimina el último item.
print(mi_lista3)

mi_lista4.sort()# ordena los elementos
print(mi_lista4)

frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
eliminado = frutas.pop(2)
print(frutas)
