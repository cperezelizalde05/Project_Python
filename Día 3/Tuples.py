mi_tuple = (1,2,3,4,(20,40))# con paréntesis
print(type(mi_tuple))
mi_tuple2 = 1,2,3,4# sin paréntesis
print(type(mi_tuple2))
t = (5,5.6, "ff")
print(t)
print(t[0])# ver que tengo en esa posición dentro del tuple
mi_tuple = list(mi_tuple)
print(type(mi_tuple))#lo convierto en lista

t1 = (1,2,3) #agrega claves al tuple. Tiene que tener la misma cantidad de elementos. sino da error.
x,y,z = t1
print(x,y,z)

t2=(1,2,4,1)#permite contar la cantidad de veces que aparece un elemento
print(t2.count(1))
t2=(1,2,4,1)#permite saber el lugar que ocupa en el tuple
print(t2.index(1))


