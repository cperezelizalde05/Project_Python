#Upper
texto = "Este es el texto de Carlos"
resultado = texto.upper()
print(resultado)

resultado = texto[2].upper()
print(resultado)

#Lower
texto = "Este es el texto de Carlos"
resultado = texto.lower()
print(resultado)

#Split
texto = "Este es el texto de Carlos"
resultado = texto.split()
print(resultado)

texto = "Este es el texto de Carlos"
resultado = texto.split("e")#e va a ser el criterio de separación
print(resultado)

#Join
a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a,b,c,d])
print(e)

#Find
texto = "Este es el texto de Carlos"
resultado = texto.find("e")# busca este caracter dentro del string
print(resultado)
texto = "Este es el texto de Carlos"
resultado = texto.find("texto")# busca este caracter dentro del string
print(resultado)

#Replace
texto = "Este es el texto de Carlos"
resultado = texto.replace("Carlos", "Federico")# busca un valor y lo reemplaza por otro.
print(resultado)


lista_palabras = ["La","legibilidad","cuenta."]
a = " ".join(["La","legibilidad","cuenta."])
print(a)

#texto1 = "Si la implementación es difícil de explicar, puede que sea una mala idea."
#resultado1 = texto1.replace("dificil","fácil","mala","buena")
#print(resultado1)

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
print(frase.replace("difícil", "fácil").replace("mala","buena"))
