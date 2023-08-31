##Práctica Control de Flujo 1
#Utilizando las variables num1 y num2, que se alimentan con el input del usuario (tal como en el código ya proporcionado):

#Crea una estructura de control de flujo que compare los valores de las variables, y arroje un resultado de acuerdo al caso:

#"num1 es mayor que num2"

#"num2 es mayor que num1"

#"num1 y num2 son iguales"

#Debes mostrar en pantalla el valor de las variables ingresadas en lugar de num1 y num2.

num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))
if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales4")

##Práctica Control de Flujo 2
#Las leyes de un país establecen que un adulto puede conducir si tiene licencia para hacerlo, y para optar por una licencia para conducir, debe de tener 18 años o más.

#Crea una estructura condicional para verificar si una persona de 16 años sin licencia puede conducir, y muestra el resultado que corresponda en pantalla:

#"Puedes conducir"

#"No puedes conducir aún. Debes tener 18 años y contar con una licencia"

#"No puedes conducir. Necesitas contar con una licencia"

#Utiliza la base de código ya proporcionada para plantear la estructura de control de flujo apropiada y verificar dichas condiciones.

edad = 16
tiene_licencia = False

"Puedes conducir"

"No puedes conducir aún. Debes tener 18 años y contar con una licencia"

"No puedes conducir. Necesitas contar con una licencia"
if edad >= 18 and tiene_licencia == True:
    print("Puedes conducir")
elif edad<18:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
elif edad >=18 and tiene_licencia == False:
    print("No puedes conducir. Necesitas contar con una licencia")

##Práctica Control de Flujo 3
#Para acceder a un determinado puesto de trabajo, el candidato debe ser capaz de programar en Python y tener conocimientos de inglés.

#Crea una estructura condicional para evaluar a un candidato dadas estas condiciones, y muestra el mensaje correspondiente en pantalla:
habla_ingles = True
sabe_python = False
"Cumples con los requisitos para postularte"
"Para postularte, necesitas saber programar en Python y tener conocimientos de inglés"
"Para postularte, necesitas tener conocimientos de inglés"
"Para postularte, necesitas saber programar en Python"
if sabe_python == True and habla_ingles == True:
    print("Cumples con los requisitos para postularte")
elif sabe_python == True and not habla_ingles == False:
    print("Para postularte, necesitas tener conocimientos de inglés")
elif sabe_python == False and habla_ingles == True:
    print("Para postularte, necesitas saber programar en Python")
else:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
#Utiliza la base de código ya proporcionada para plantear la estructura de control de flujo apropiada y verificar dichas condiciones. Evalúa a un candidato que sabe inglés, pero no programa en Python.