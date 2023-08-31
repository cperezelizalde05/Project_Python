#Ejemplo 1
lista = ["a", "b", "c"]
for letra in lista:
    numero_letra = lista.index(letra) + 1
    print("letra: " + letra)
    print(f"Letra {numero_letra}: {letra}")

#Ejemplo 2
lista2 = ["Pablo", "Laura", "Fede", "Luis", "Julia"]
for nombre in lista2:
    if nombre.startswith("L"):
        print(nombre)

#Ejemplo 3
numeros = [1, 2, 3, 4, 5]
mi_valor = 0
for numero in numeros:
    mi_valor = mi_valor + numero

print(mi_valor)# el print al estar en la misma posición del "for" me ejecuta al finalizar el loop

#Ejemplo 4
palabra = "Python" #los strings al igual que las listas son iterables
for letra in palabra:
    print(letra)

#Ejemplo 5
for letras in "python":
    print(letras)

for x in [[1,2],[3,4],[5,6]]:
    print(x)

for a,b in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)

#Ejemplo 6
dic = {"clave1": "a", "clave2": "b", "clave3": "c"}
for item in dic:
    print(item)

ene = {"clave1": "a", "clave2": "b", "clave3": "c"}
for item in ene.items():
    print(item)

feb = {"clave1": "a", "clave2": "b", "clave3": "c"}
for item in feb.values():
    print(item)

mar = {"clave1": "a", "clave2": "b", "clave3": "c"}
for d,f  in mar.items():
    print(d,f)



