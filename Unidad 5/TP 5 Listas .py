"""
Práctico 3: Estructuras secuenciales
Alumno: Joel Vitrano
Comisión: 12

"""

1) Crear una lista con las notas de 10 estudiantes.
• Mostrar la lista completa.
• Calcular y mostrar el promedio.
• Indicar la nota más alta y la más baja.

notas = [6,7,6,9,7,9,6,7,2,5]
print("las notas de los estudiantes son : ", notas )

promedio = sum(notas) / len(notas)
print("el promedio de las notas ", promedio)

nota_max = max(notas)
nota_min = min(notas)

print("Nota más alta:", nota_max)
print("Nota más baja:", nota_min)

2) Pedir al usuario que cargue 5 productos en una lista.
• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
• Preguntar al usuario qué producto desea eliminar y actualizar la lista.

products =[]
for i in range(5):
     products.append(product)

 print("La lista ordenada alfabeticamente es: ")
 print(sorted(products))

 productDelet = input("Ingrese el producto que quiera eliminar: ")

 if (productDelet in products):
     products.remove(productDelet)
     print("Producto eliminado")
 else:
     print("El producto no esta en la lista")

 print("La lista actualizada : ", products)

 3) Generar una lista con 15 números enteros al azar entre 1 y 100.
 • Crear una lista con los pares y otra con los impares.
 • Mostrar cuántos números tiene cada lista.

 import random

 numbers = [random.randint(1, 100) for _ in range(15)]
 print("Lista completa:", numbers)

 par = [i for i in numbers if i % 2 == 0]
 impar = [j for j in numbers if j % 2 != 0]

 print("Lista de pares:", par)
 print("Cantidad de pares:", len(impar))

 print("Lista de impares:", par)
 print("Cantidad de impares:", len(impar))

 4) Dada una lista con valores repetidos:
 • Crear una nueva lista sin elementos repetidos.
 • Mostrar el resultado.

 datos = [1,3,5,3,7,1,9,5,3]
 datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

 noRepetidos = list(set(datos))

 print("Lista original:", datos)
 print("Lista sin repetidos:", noRepetidos)

 5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
 • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
 • Mostrar la lista final actualizada.

 estudiantes = ["Ana", "Luis", "Maria", "Carlos", "Sofia", "Pedro", "Lucia", "Jorge"]

 print("Lista inicial de estudiantes:", estudiantes)

 accion = input("\n¿Querés 'agregar' un estudiante o 'eliminar' uno? (escriba agregar/eliminar): ").lower()

 if accion == "agregar":
     nuevo = input("Ingrese el nombre del nuevo estudiante: ").title()
     estudiantes.append(nuevo)
     print(f"{nuevo} fue agregado a la lista.")
 elif accion == "eliminar":
     borrar = input("Ingrese el nombre del estudiante a eliminar: ").title()
     if borrar in estudiantes:
         estudiantes.remove(borrar)
         print(f"{borrar} fue eliminado de la lista.")
     else:
         print("Ese estudiante no está en la lista.")
 else:
     print("Opción no válida.")

 print("\nLista final de estudiantes:", estudiantes)

 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
 último pasa a ser el primero).

 numeros = [10, 20, 30, 40, 50, 60, 70]

 numeros = [numeros[-1]] + numeros[:-1]

 print("Lista rotada:", numeros)

 7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
 semana.
 • Calcular el promedio de las mínimas y el de las máximas.
 • Mostrar en qué día se registró la mayor amplitud térmica.

 temperaturas = [
     [12, 22],  
     [14, 25],  
     [10, 21],  
     [13, 24],  
     [15, 27],  
     [11, 20],  
     [9, 18]    
 ]

 days = ["lunes", "martes", "miercoles", "jeves", "viernes", "sabado", "domingo"]

 minimas = [fila[0] for fila in temperaturas]
 maximas = [fila[1] for fila in temperaturas]

 promedioMin = sum(minimas) / len(minimas)
 promedioMax = sum(maximas) / len(maximas)

 amplitudes = [fila[1] - fila[0] for fila in temperaturas]
 maxAmplitud = max(amplitudes)
 diaMaxAmplitud = days[amplitudes.index(maxAmplitud)]

 print("Promedio de minimas:", promedioMin)
 print("Promedio de maximas:", promedioMax)
 print("Mayor amplitud termica:", maxAmplitud, "grados en", diaMaxAmplitud)

 Crear una matriz con las notas de 5 estudiantes en 3 materias.
 • Mostrar el promedio de cada estudiante.
 • Mostrar el promedio de cada materia.

 notas = [
     [7, 8, 6],   
     [5, 9, 7],   
     [8, 6, 9],   
     [4, 7, 5],   
     [9, 8, 10]   
 ]

 print("Promedio de cada estudiante:")
 for i, fila in enumerate(notas):
     promedio = sum(fila) / len(fila)
     print(f"Estudiante {i+1}: {round(promedio,2)}")

 print("Promedio de cada materia :")
 materias = len(notas[0]) 

 for j in range(materias):
     suma = sum(fila[j] for fila in notas)
     promedio = suma / len(notas)
     print(f"Materia {j+1}: {round(promedio,2)}")

 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
 • Inicializarlo con guiones "-" representando casillas vacías.
 • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
 • Mostrar el tablero después de cada jugada

 tablero = [["-"] * 3 for _ in range(3)]

 for fila in tablero:
     print(" ".join(fila))
 print()

 for turno in range(9):

     jugador = "X" if turno % 2 == 0 else "O"
     print(f"Turno del jugador {jugador}")
    
     fila = int(input("Ingrese la fila (0-2): "))
     columna = int(input("Ingrese la columna (0-2): "))
    
     if tablero[fila][columna] == "-":
         tablero[fila][columna] = jugador     else:
         print("Casilla ocupada")

     for fila_mostrar in tablero:
         print(" ".join(fila_mostrar))
     print()

 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
 • Mostrar el total vendido por cada producto.
 • Mostrar el día con mayores ventas totales.
 • Indicar cuál fue el producto más vendido en la semana.

ventas = [
    [10, 20, 15, 30, 25, 40, 35],  
    [5, 10, 20, 15, 25, 30, 20],   
    [12, 18, 22, 28, 26, 30, 24],  
    [8, 15, 10, 20, 18, 25, 30]    
]

print("Total vendido por cada producto:")
for i, fila in enumerate(ventas):
    total = sum(fila)
    print(f"Producto {i+1}: {total}")


totalesDias = [sum(ventas[i][j] for i in range(len(ventas))) for j in range(7)]

maxDia = max(totalesDias)
indiceDia = totalesDias.index(maxDia)
print(f"\nEl dia con mayores ventas fue el día {indiceDia+1} con {maxDia} ventas")


productosTotales = [sum(fila) for fila in ventas]
maxProducto = max(productosTotales)
indiceProducto = productosTotales.index(maxProducto)
print(f"El producto mas vendido fue el Producto {indiceProducto+1} con {maxProducto} ventas")
