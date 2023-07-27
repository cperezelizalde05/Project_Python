mi_set= set([1,2,3,(1,2,3),4,5]) #con la palabra set. Admite tuples
print(type(mi_set))
print(mi_set)
print(len(mi_set)) #ver la longitud de mi set
print(2 in mi_set)# buscar en mi set

otro_set = {1,2,3} #sin la palabra set
print(type(otro_set))
print(otro_set)

s1 = {1,2,3,4}
s2 = {4,5,6}
s3 = s1.union(s2)#unir dos sets
print(s3)

s1.add(5)#agregar elemento a un set
print(s1)

s2.remove(6)#eliminar elemento en un set. Un elemento similar es discard (descartar)
print(s2)

s1.pop()#elimina aleatoriamente un elemento
#ejemplo
sorteo = s1.pop()
print(sorteo)

s1.clear()#borrar lo que está en el set
print(s1)