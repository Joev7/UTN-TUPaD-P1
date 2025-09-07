
"""
Práctico 1: Estructuras Secuenciales
Alumno: Joel Vitrano
Comisión: 12
"""

# ==============================
# Ejercicio 1
# ==============================
print("Hola Mundo!")

# ==============================
# Ejercicio 2
# ==============================
nombre = input("Por favor, ingrese su nombre: ")
print(f"Hola {nombre}!")
print("Hola " + nombre + "!")

# ==============================
# Ejercicio 3
# ==============================
nombre = input("Por favor, ingrese su nombre: ")
apellido = input("Por favor, ingrese su apellido: ")
edad = input("Por favor, ingrese su edad: ")
lugar_de_residencia = input("Por favor, ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_de_residencia}.")

# ==============================
# Ejercicio 4
# ==============================
import math

radio_circulo = float(input("Por favor, ingrese el radio del círculo: "))
area_circulo = round(math.pi * (radio_circulo)**2, 2)
perimetro_circulo = round(2 * math.pi * radio_circulo, 2)
print(f"El área del círculo es de {area_circulo} y el perímetro es de {perimetro_circulo}.")

# ==============================
# Ejercicio 5
# ==============================
cantidad_segundos = float(input("Por favor, ingrese la cantidad de segundos a convertir: "))
cantidad_horas = round(cantidad_segundos / 3600, 2)
print(f"El equivalente a {cantidad_segundos} segundos son {cantidad_horas} horas.")

# ==============================
# Ejercicio 6
# ==============================
numero_a_multiplicar = int(input("Por favor, ingrese un número entero: "))
print(f"""
  {numero_a_multiplicar} x 0 = {numero_a_multiplicar * 0}
  {numero_a_multiplicar} x 1 = {numero_a_multiplicar * 1}
  {numero_a_multiplicar} x 2 = {numero_a_multiplicar * 2}
  {numero_a_multiplicar} x 3 = {numero_a_multiplicar * 3}
  {numero_a_multiplicar} x 4 = {numero_a_multiplicar * 4}
  {numero_a_multiplicar} x 5 = {numero_a_multiplicar * 5}
  {numero_a_multiplicar} x 6 = {numero_a_multiplicar * 6}
  {numero_a_multiplicar} x 7 = {numero_a_multiplicar * 7}
  {numero_a_multiplicar} x 8 = {numero_a_multiplicar * 8}
  {numero_a_multiplicar} x 9 = {numero_a_multiplicar * 9}
      """)

# ==============================
# Ejercicio 7
# ==============================
numero_a = float(input("Por favor, ingrese un número distinto de 0: "))
numero_b = float(input("Por favor, ingrese otro número distinto de 0: "))
print(f"""
  Resultado de la suma: {numero_a + numero_b}
  Resultado de la división: {round(numero_a / numero_b, 2)}
  Resultado de la multiplicación: {numero_a * numero_b}
  Resultado de la resta: {numero_a - numero_b}
      """)

# ==============================
# Ejercicio 8
# ==============================
peso = float(input("Por favor, ingrese su peso en kilogramos: "))
altura = float(input("Por favor, ingrese su altura en metros: "))
imc = round(peso / altura**2, 2)
print(f"Su IMC es de: {imc}.")

# ==============================
# Ejercicio 9
# ==============================
temperatura_celsius = float(input("Por favor, ingrese una temperatura en °C: "))
temperatura_fahrenheit = round((9/5)*temperatura_celsius+32, 2)
print(f"{temperatura_celsius} °C equivalen a {temperatura_fahrenheit} °F.")

# ==============================
# Ejercicio 10
# ==============================
numero_a = float(input("Por favor, ingrese el primer número: "))
numero_b = float(input("Por favor, ingrese el segundo número: "))
numero_c = float(input("Por favor, ingrese el tercer número: "))
promedio_a_b_c = round((numero_a + numero_b + numero_c) / 3, 2)
print(f"El promedio de los números ingresados es {promedio_a_b_c}.")







