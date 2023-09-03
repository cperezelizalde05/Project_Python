#Práctica Loop For 1
#Utilizando loops For, saluda a todos los miembros de una clase, imprimiendo "Hola" + su nombre.

#Por ejemplo: "Hola María"

#alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]

alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]
for nombre in alumnos_clase:
    print("Hola " + nombre)

#Práctica Loop For 2
#Dada la siguiente lista de números, realiza la suma de todos los números utilizando loops For y almacena el resultado de la suma en una variable llamada suma_numeros:

#lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0
for numero in lista_numeros:
    suma_numeros += numero
    print("la suma de los numeros es:", suma_numeros)


#Práctica Loop For 3
#Dada la siguiente lista de números, realiza la suma de todos los números pares e impares* por separado en las variables suma_pares y suma_impares respectivamente:

#lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]

#*Recordando de los días anteriores: el módulo (o resto) de un número dividido 2 es cero cuando dicho valor es par, y 1 cuando es impar

#num % 2 == 0 (valores pares)

#num % 2 == 1 (valores impares)

lista_numero = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0
for valores in lista_numero:
    if valores % 2 == 0:
        suma_pares += valores
    else:
        suma_impares += valores
print("La suma de los números pares en la lista es:", suma_pares)
print("La suma de los números impares en la lista es:", suma_impares)
