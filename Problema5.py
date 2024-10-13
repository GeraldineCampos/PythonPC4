import os

def generar_tabla(n):
    nombre_archivo = f"tabla-{n}.txt"
    with open(nombre_archivo, "w") as archivo:
        for i in range(1, 11):
            archivo.write(f"{n} x {i} = {n * i}\n")
    print(f"Tabla de multiplicar del {n} guardada en {nombre_archivo}.")

# Función para leer la tabla completa de un archivo
def leer_tabla(n):
    nombre_archivo = f"tabla-{n}.txt"
    try:
        with open(nombre_archivo, "r") as archivo:
            contenido = archivo.read()
            print(f"Tabla de multiplicar del {n}:\n{contenido}")
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")

# Función para leer una línea específica de la tabla
def leer_linea_tabla(n, m):
    nombre_archivo = f"tabla-{n}.txt"
    try:
        with open(nombre_archivo, "r") as archivo:
            lineas = archivo.readlines()
            if 1 <= m <= 10:
                print(f"Línea {m} de la tabla del {n}: {lineas[m - 1].strip()}")
            else:
                print("El valor de m debe estar entre 1 y 10.")
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")

# Menú principal
def menu():
    while True:
        print("\nMenú de opciones:")
        print("1. Generar y guardar tabla de multiplicar")
        print("2. Leer y mostrar tabla de multiplicar")
        print("3. Leer y mostrar una línea específica de la tabla de multiplicar")
        print("4. Salir")
        
        opcion = input("Por favor, elija una opción: ")
        
        if opcion == "1":
            # Solicitar un número n entre 1 y 10
            try:
                n = int(input("Ingrese un número entero entre 1 y 10: "))
                if 1 <= n <= 10:
                    generar_tabla(n)
                else:
                    print("El número debe estar entre 1 y 10.")
            except ValueError:
                print("Por favor, ingrese un número entero válido.")
        
        elif opcion == "2":
            # Solicitar el número n para leer la tabla
            try:
                n = int(input("Ingrese un número entero entre 1 y 10: "))
                if 1 <= n <= 10:
                    leer_tabla(n)
                else:
                    print("El número debe estar entre 1 y 10.")
            except ValueError:
                print("Por favor, ingrese un número entero válido.")
        
        elif opcion == "3":
            # Solicitar el número n y m para leer una línea específica de la tabla
            try:
                n = int(input("Ingrese un número entero entre 1 y 10 (n): "))
                m = int(input("Ingrese un número entero entre 1 y 10 (m): "))
                if 1 <= n <= 10 and 1 <= m <= 10:
                    leer_linea_tabla(n, m)
                else:
                    print("Ambos números deben estar entre 1 y 10.")
            except ValueError:
                print("Por favor, ingrese números enteros válidos.")
        
        elif opcion == "4":
            # Salir del programa
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida. Por favor, elija una opción entre 1 y 4.")

if __name__ == "__main__":
    menu()