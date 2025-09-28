"""
Práctico 3: Estructuras Condicionales
Alumno: Joel Vitrano
Comisión: 12

"""



print("---------------------EJERCICIO 1---------------------")

print("Bienvenido ingrese su edad")
age = int(input("Edad :"))
if (age >= 18):
    print("Es mayor de edad")
else:
    print("es menor") 

print("---------------------EJERCICIO 2---------------------")

print("Bienvenido, ingrese la nota que se saco")
nota = int(input("Nota :"))
if (nota >= 6):
    print("Aprobado")
else:
    print("Desaprobado") 

print("---------------------EJERCICIO 3---------------------")

print("Bienvenido, ingrese un numero par")
number = int(input("Numero :"))

if (number%2==0):
    print("es par")
else:
    print("no es par") 

import random
import statistics


print("---------------------EJERCICIO 4---------------------")

print("Bienvenido, ingrese su edad para ver en que categoria entra")
age = int(input("Edad :"))

if (age < 12):
    print("Ninio/a")
elif(age >= 12 or age < 18):
    print("Adolescente")
elif(age >= 18 or age < 30):
    print("Adulto/a joven")
elif(age >= 30 ):
    print("Adulto/a")
else:
    ("Ingrese una edad > 0")

print("---------------------EJERCICIO 5---------------------")

password = input("Ingrese una contraseña: ")


if 8 <= len(password) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

print("---------------------EJERCICIO 6---------------------")

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular moda, mediana y media
moda = statistics.mode(numeros_aleatorios)
mediana = statistics.median(numeros_aleatorios)
media = statistics.mean(numeros_aleatorios)

print("Lista de numeros:", numeros_aleatorios)
print("Moda:", moda)
print("Mediana:", mediana)
print("Media:", media)

if media > mediana > moda:
    print("Sesgo positivo (a la derecha)")
elif media < mediana < moda:
    print("Sesgo negativo (a la izquierda)")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("No cumple exactamente con los criterios de sesgo")

print("---------------------EJERCICIO 7---------------------")

text = input("Ingrese palabra: ")

if text[-1] in "aeiou":
    text = text + "!"

print(text)

print("---------------------EJERCICIO 8---------------------")

name = str(input("Ingrese su nombre: "))
print("Ingrese un numero dependiendo la forma en la que quiere su nombre")
print("1 -> Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.")
print("2 -> Si quiere su nombre en minúsculas. Por ejemplo: pedro")
print("3 -> Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.")
number = int(input("Numero : "))
if (number == 1):
    print(name.upper())
elif (number == 2):
    print(name.lower())
elif (number == 3):
    print(name.title())
else:
    print("Error el numero tiene que ser 1, 2 o 3")    

print("---------------------EJERCICIO 8---------------------")

magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa danios)")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar danios en estructuras débiles)")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar danios significativos)")
else:  
    print("Extremo (puede causar graves danios a gran escala)")

print("---------------------EJERCICIO 9---------------------")

hemisferio = str(input("Ingrese en que hemisferio se encuentra NORTE O SUR: ")).lower()
mes = int(input("Ingrese en que mes (NUMERO) se encuentra: "))
dia = int(input("Ingrese que dia es (NUMERO) :"))

if (mes == 12 and dia >= 21) or (mes in[1,2]) or (mes == 3 and dia <=20):
    hemisferioNorte = "Invierno"
    hemisferioSur = "Verano"
if (mes == 3 and dia >= 21) or (mes in[4,5]) or (mes == 6 and dia <=20):
    hemisferioNorte = "Primavera"
    hemisferioSur = "Otonio"
if (mes == 6 and dia >= 21) or (mes in[7,8]) or (mes == 9 and dia <=20):
    hemisferioNorte = "Verano"
    hemisferioSur = "Invierno"    
if (mes == 9 and dia >= 21) or (mes in[10,11]) or (mes == 12 and dia <=20):
    hemisferioNorte = "Otonio"
    hemisferioSur = "Primavera" 
else:
    print("Ingrese los datos correctamente")

if (hemisferio == "norte"):
    print(f"En el hemisferio norte la estacion del anio es {hemisferioNorte}")
elif (hemisferio == "sur"):
    print(f"En el hemisferio sur la estacion del anio es {hemisferioSur}")
else:
    print("Ingrese la opcion validad NORTE O SUR")
