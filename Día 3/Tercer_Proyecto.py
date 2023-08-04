#Consignas:
#Pedir al usuario que ingrese un texto
#Pedir al usuario que ingrese tres letras
#Le va a devolver al usuario la siguiente información
#Cuantas veces aparece la letra que eligió. Almacenar esas letras en una lista, pasar texto original a minúsculas
#Cuantas palabras hay a lo largo del texto
#Indicar la primera y la última letra del texto
#Mostrar el texto si invirtiéramos el texto de las palabras
#Consultar si la palabra python está dentro del texto, booleanos y diccionarios

#La casa de mi madre es hermosa y cálida
# a, b, c

#Ejercicio
frase = input("Escribí un texto o frase\n")
letras = []
frase = frase.lower()
letras.append(input("Ingresa la primera letra\n").lower())
letras.append(input("Ingresa la segunda letra\n").lower())
letras.append(input("Ingresa la tercera letra\n").lower())
print("\n")

print("La cantidad de letras es")
cantidad_letras1 = frase.count(letras[0])
cantidad_letras2 = frase.count(letras[1])
cantidad_letras3 = frase.count(letras[2])


print(f"Hemos encontrado la letra '{letras[0]}' repetida {cantidad_letras1} veces" )
print(f"Hemos encontrado la letra '{letras[1]}' repetida {cantidad_letras2} veces" )
print(f"Hemos encontrado la letra '{letras[2]}' repetida {cantidad_letras3} veces" )

print("\n")
print("Cantidad de palabras")
palabras = frase.split()
print(f"Hemos encontrado {len(palabras)}")

print("\n")
print("Letras de inicio y final\n")
letra_inicio = frase [0]
letra_final = frase [-1]
print(f"La letra inicial es {letra_inicio} y la letra final es {letra_final}")

print("\n")
print("Texto Invertido")
palabras.reverse()
frase_invertida = ' '.join(palabras)
print(f"Si ordenamos el texto al revés va a decir: '{frase_invertida}'")

print("\n")
print("Buscando palabra Python")
buscar_python = "Python" in frase
dic = {True: "si", False: "no"}
print(f"La palabra 'Python' {dic[buscar_python]} se encuentra en el texto")