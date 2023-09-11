#Ejemplo 1
monedas = 5

while monedas > 0:
    print(f"Tengo {monedas} monedas")
    #monedas = monedas - 1
    monedas -=1 #forma compacta de hacer lo mismo que anteriormente hice
else:
    print("No tengo mas monedas")

#Ejemplo 2
respuesta = "s"
while respuesta == "s":
   respuesta = input("quieres seguir? (n/s) ")
else:
   print("Gracias")

#Ejemplo 3 - Pass
respuesta = "s"
while respuesta == "s":
   pass #me permite seguir codificando sin darle importancia a este loop

#print("Hola")

#Ejemplo 4 - Break
nombre = input("Cuál es tu nombre? ")
for letra in nombre:
    if letra == "r":
        #break
        continue
    print(letra)

