if 10>9:
    print("Es correcto")

if 5 == 2:
    print("OK")
else:
    print("no OK")

mascota = "perro"
if mascota == "gato": #los dos puntos se ponen al final
    print("Tienes un gato")
elif mascota == "perro": #al igual que en el if los dos puntos van al final
    print("Tienes un perro")
elif mascota == "pez":
    print("Tienes un pez")
else:
    print("No se que animal tienes")

#Anidar condiciones IF
edad = 16
calificacion = 6
if edad < 18:
    print("Eres menor de edad")
    if calificacion >=7:
        print("Aprobado. Felicitaciones!!")
    else:
        print("No has aprobado. Lo lamento.")
else:
    print("Eres mayor de edad")
