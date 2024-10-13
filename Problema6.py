def contar_lineas_codigo(ruta_archivo):
    try:
        # Verificar si el archivo tiene la extensión .py
        if not ruta_archivo.endswith(".py"):
            print("El archivo no tiene la extensión .py")
            return

        # Abrir el archivo y leer todas las líneas
        with open(ruta_archivo, "r") as archivo:
            lineas = archivo.readlines()

        lineas_codigo = 0

        # Iterar sobre las líneas y contar solo aquellas que no son comentarios o líneas en blanco
        for linea in lineas:
            # Quitar espacios en blanco al inicio y al final de la línea
            linea = linea.strip()

            # Ignorar líneas vacías o comentarios 
            if linea == "" or linea.startswith("#"):
                continue

            # Si la línea es código válido, incrementa el contador
            lineas_codigo += 1

        print(f"Número de líneas de código: {lineas_codigo}")

    except FileNotFoundError:
        # Si el archivo no se encuentra, mostrar un mensaje de error
        print("El archivo no fue encontrado. Verifica la ruta proporcionada.")

def main():
    # Solicitar al usuario la ruta del archivo
    ruta_archivo = input("Introduce la ruta del archivo .py: ")
    
    # Llamar a la función para contar líneas de código
    contar_lineas_codigo(ruta_archivo)

if __name__ == "__main__":
    main()