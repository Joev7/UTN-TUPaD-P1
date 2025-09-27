"""
TP 3 - Estructuras condicionales (UTN a distancia)
Autor: (completar con tu nombre)
Descripción: Script con resoluciones de los 10 ejercicios del práctico.
Cada ejercicio está implementado en una función independiente.
Al ejecutar el archivo, aparece un menú para probar cada ejercicio.
"""

from statistics import mean, median, mode
import random
import sys

# -------------------------------
# Utilidades comunes
# -------------------------------

def leer_entero(mensaje, minimo=None, maximo=None):
    """Lee un entero desde input con validación opcional de rango."""
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"Por favor, ingrese un número entero >= {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"Por favor, ingrese un número entero <= {maximo}.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")

def leer_str_no_vacio(mensaje):
    """Lee un string no vacío desde input."""
    while True:
        s = input(mensaje).strip()
        if s:
            return s
        print("La entrada no puede estar vacía.")

# -------------------------------
# Ejercicios
# -------------------------------

def ejercicio_1():
    """1) Mayor de edad"""
    edad = leer_entero("Ingrese su edad: ", minimo=0)
    if edad > 18:
        print("Es mayor de edad")
    else:
        print("No es mayor de edad")


def ejercicio_2():
    """2) Nota Aprobado/Desaprobado"""
    nota = leer_entero("Ingrese su nota (0-10): ", minimo=0, maximo=10)
    if nota >= 6:
        print("Aprobado")
    else:
        print("Desaprobado")


def ejercicio_3():
    """3) Permitir ingresar solo números pares (mensaje según corresponda)"""
    n = leer_entero("Ingrese un número: ")
    if n % 2 == 0:
        print("Ha ingresado un número par")
    else:
        print("Por favor, ingrese un número par")


def ejercicio_4():
    """4) Categoría según edad"""
    edad = leer_entero("Ingrese su edad: ", minimo=0)
    if edad < 12:
        categoria = "Niño/a"
    elif 12 <= edad < 18:
        categoria = "Adolescente"
    elif 18 <= edad < 30:
        categoria = "Adulto/a joven"
    else:
        categoria = "Adulto/a"
    print(f"Categoría: {categoria}")


def ejercicio_5():
    """5) Validación de longitud de contraseña (8 a 14 caracteres)"""
    pwd = leer_str_no_vacio("Ingrese una contraseña: ")
    if 8 <= len(pwd) <= 14:
        print("Ha ingresado una contraseña correcta")
    else:
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


def ejercicio_6():
    """6) Sesgo (media, mediana, moda) con lista aleatoria de 50 números entre 1 y 100"""
    numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]
    mu = mean(numeros_aleatorios)
    med = median(numeros_aleatorios)
    try:
        mod = mode(numeros_aleatorios)
        tiene_moda = True
    except Exception:
        # En caso de que no haya una moda única, lo indicamos.
        mod = None
        tiene_moda = False

    print("Lista generada:", numeros_aleatorios)
    print(f"Media: {mu:.2f}")
    print(f"Mediana: {med:.2f}")
    if tiene_moda:
        print(f"Moda: {mod}")
    else:
        print("Moda: no definida de manera única")

    # Criterio de sesgo
    if tiene_moda and (mu > med > mod):
        print("Sesgo positivo (a la derecha)")
    elif tiene_moda and (mu < med < mod):
        print("Sesgo negativo (a la izquierda)")
    else:
        # Si no hay moda única o no se cumple la cadena estricta, evaluamos igualdad aproximada
        # Consideramos sin sesgo si media y mediana casi coinciden y (si hay) moda es cercana.
        eps = 1e-9
        if abs(mu - med) < eps and (not tiene_moda or abs(mu - mod) < eps):
            print("Sin sesgo")
        else:
            print("No se puede determinar un sesgo claro con el criterio dado")


def ejercicio_7():
    """7) Agregar '!' si termina con vocal (considerando acentos)"""
    texto = leer_str_no_vacio("Ingrese una palabra o frase: ")
    ultima = texto.strip()[-1:]  # último carácter no-espacio si existe
    vocales = set("aeiouáéíóúAEIOUÁÉÍÓÚ")
    if ultima in vocales:
        print(texto + "!")
    else:
        print(texto)


def ejercicio_8():
    """8) Transformar nombre según opción 1/2/3"""
    nombre = leer_str_no_vacio("Ingrese su nombre: ")
    print("Opciones:")
    print("1) Mayúsculas")
    print("2) Minúsculas")
    print("3) Primera letra mayúscula")
    opcion = leer_entero("Elija opción (1-3): ", minimo=1, maximo=3)
    if opcion == 1:
        print(nombre.upper())
    elif opcion == 2:
        print(nombre.lower())
    else:
        print(nombre.title())


def ejercicio_9():
    """9) Clasificación de la magnitud de un terremoto (escala de Richter)"""
    while True:
        try:
            magnitud = float(input("Ingrese magnitud del terremoto (número real): "))
            break
        except ValueError:
            print("Entrada inválida. Ingrese un número (use punto como separador decimal).")

    if magnitud < 3:
        print("Muy leve (imperceptible)")
    elif 3 <= magnitud < 4:
        print("Leve (ligeramente perceptible)")
    elif 4 <= magnitud < 5:
        print("Moderado (sentido por personas, pero generalmente no causa daños)")
    elif 5 <= magnitud < 6:
        print("Fuerte (puede causar daños en estructuras débiles)")
    elif 6 <= magnitud < 7:
        print("Muy Fuerte (puede causar daños significativos)")
    else:
        print("Extremo (puede causar graves daños a gran escala)")


def ejercicio_10():
    """10) Estación del año según hemisferio, mes y día"""
    # Hemisferio
    while True:
        hemisferio = input("Indique hemisferio (N/S): ").strip().upper()
        if hemisferio in ("N", "S"):
            break
        print("Entrada inválida. Ingrese 'N' para norte o 'S' para sur.")

    # Mes y día
    mes = leer_entero("Ingrese número de mes (1-12): ", minimo=1, maximo=12)
    dia = leer_entero("Ingrese día del mes (1-31): ", minimo=1, maximo=31)

    # Validaciones mínimas de día por mes (simplificadas, no considera años bisiestos)
    dias_por_mes = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    if dia > dias_por_mes.get(mes, 31):
        print("Fecha inválida para el mes indicado.")
        return

    # Rangos según tabla (fechas INCLUSIVAS)
    # 21/12 - 20/03 ; 21/03 - 20/06 ; 21/06 - 20/09 ; 21/09 - 20/12
    # Construimos una tupla (mes, día) para comparar lexicográficamente.
    md = (mes, dia)

    def en_rango(md, ini, fin):
        """Devuelve True si md está en [ini, fin] considerando que ini puede estar a fin de año (21/12 a 20/03)."""
        # Si el rango no cruza fin de año:
        if ini <= fin:
            return ini <= md <= fin
        # Si el rango cruza de diciembre a marzo:
        return md >= ini or md <= fin

    inv_norte = en_rango(md, (12, 21), (3, 20))
    prim_norte = en_rango(md, (3, 21), (6, 20))
    ver_norte = en_rango(md, (6, 21), (9, 20))
    oto_norte = en_rango(md, (9, 21), (12, 20))

    if hemisferio == "N":
        if inv_norte:
            estacion = "Invierno"
        elif prim_norte:
            estacion = "Primavera"
        elif ver_norte:
            estacion = "Verano"
        elif oto_norte:
            estacion = "Otoño"
        else:
            estacion = "Fecha fuera de los rangos considerados"
    else:  # Sur
        if inv_norte:      # En norte es Invierno, en sur es Verano
            estacion = "Verano"
        elif prim_norte:   # En norte es Primavera, en sur es Otoño
            estacion = "Otoño"
        elif ver_norte:    # En norte es Verano, en sur es Invierno
            estacion = "Invierno"
        elif oto_norte:    # En norte es Otoño, en sur es Primavera
            estacion = "Primavera"
        else:
            estacion = "Fecha fuera de los rangos considerados"

    print(f"Estación: {estacion}")

# -------------------------------
# Menú principal
# -------------------------------

def mostrar_menu():
    print("\nTP 3 - Estructuras condicionales")
    print("Seleccione un ejercicio a ejecutar:")
    for i in range(1, 11):
        print(f"{i}) Ejercicio {i}")
    print("0) Salir")

def main():
    while True:
        mostrar_menu()
        opcion = leer_entero("Opción: ", minimo=0, maximo=10)
        if opcion == 0:
            print("¡Hasta luego!")
            return
        try:
            globals()[f"ejercicio_{opcion}"]()
        except KeyError:
            print("Opción inválida.")
        except Exception as e:
            print(f"Ocurrió un error durante la ejecución: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
