#Práctica Zip 1
#Muestra en pantalla frases como la del siguiente ejemplo:

#La capital de Alemania es Berlín

#Utiliza la función zip, loops, y las siguientes listas de países y capitales para resolverlo rápida y eficientemente.

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]


for pais, capital in zip(paises, capitales):
   if pais=="Alemania" and capital == "Berlín":
    frase = f"La capital de {pais} es {capital}"
    print(frase)
for pais, capital in zip(paises, capitales):
    frase = f"La capital de {pais} es {capital}"
    print(frase)
#Práctica Zip 2
#Crea un objeto zip formado a partir de listas, de un conjunto de marcas y productos que tú prefieras, dentro de la variable mi_zip.
marcas = ["Wrangler", "Levis", "Gap"]
productos = ["pantalón", "camisa", "buzo"]
mi_zip = list(zip(marcas, productos))
print(mi_zip)

#Práctica Zip 3
#Crea el zip con las traducciones los números del 1 al 5 en español, portugués e inglés (en el mismo orden), y convierte el objeto generado en una lista almacenada en la variable numeros:

#uno / um / one

#dos / dois / two

#tres / três / three

#cuatro / quatro / four

#cinco / cinco / five

#El resultado deberá seguir la estructura:

#[('uno', 'um', 'one'), ('dos', 'dois', 'two'), ... ]

espaniol= ["uno", "dos", "tres", "cuatro", "cinco"]
portuques= ["um", "dois", "três", "quatro", "cinco"]
ingles= ["one", "two", "three", "four", "five"]

numeros = list(zip(espaniol, portuques, ingles))
print(numeros)
