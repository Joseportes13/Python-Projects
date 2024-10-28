from pathlib import Path
import os
from os import system

def limpiar_pantalla():
    # Limpia la pantalla según el sistema operativo
    system('cls' if os.name == 'nt' else 'clear')

def bienvenida():
    limpiar_pantalla()
    print('Bienvenido a tu recetario.')
    carpeta_recetas = os.path.abspath("Recetas")
    print(f'La ruta de acceso a la carpeta de recetas es: {carpeta_recetas}')
    total_recetas = contar_recetas(carpeta_recetas)
    print(f'\nHay un total de {total_recetas} recetas en la carpeta de Recetas')

def contar_recetas(carpeta_recetas):
    # Contar el número de recetas en la carpeta
    contador = 0
    for carpeta, subcarpetas, archivos in os.walk(carpeta_recetas):
        for archivo in archivos:
            if archivo.endswith(".txt"):
                contador += 1
    return contador

def elegir_categoria(carpeta_recetas):
    categorias = []
    for c in os.listdir(carpeta_recetas):
        if os.path.isdir(os.path.join(carpeta_recetas, c)):
            categorias.append(c)

    print('Categorías disponibles:')
    for i, categoria in enumerate(categorias, 1):
        print(f'{i}. {categoria}')

    seleccion = int(input('Elige una categoría: '))
    return os.path.join(carpeta_recetas, categorias[seleccion - 1])

def mostrar_recetas(carpeta_categoria):
    recetas = [f for f in os.listdir(carpeta_categoria) if f.endswith(".txt")]

    print('Recetas disponibles:')
    for i, receta in enumerate(recetas, 1):
        print(f'{i}. {receta[:-4]}')  # Muestra el nombre sin la extensión .txt

    seleccion = int(input('Elige una receta: '))
    return os.path.join(carpeta_categoria, recetas[seleccion - 1])

def leer_receta(ruta_receta):
    with open(ruta_receta, 'r') as archivo:
        return archivo.read()

def crear_receta(carpeta_categoria):
    nombre_receta = input("Escribe el nombre de la nueva receta: ")
    contenido_receta = input("Escribe el contenido de la receta:\n")
    
    # Crear la ruta completa del archivo de la receta
    ruta_receta = os.path.join(carpeta_categoria, nombre_receta + ".txt")
    
    # Guardar el contenido en el archivo
    with open(ruta_receta, 'w') as archivo:
        archivo.write(contenido_receta)
    
    print(f"\nLa receta '{nombre_receta}' ha sido creada en la categoría seleccionada.\n")

def crear_categoria(carpeta_recetas):
    nombre_categoria = input("Escribe el nombre de la nueva categoría: ")
    ruta_categoria = os.path.join(carpeta_recetas, nombre_categoria)
    
    # Crear la nueva carpeta si no existe ya
    if not os.path.exists(ruta_categoria):
        os.mkdir(ruta_categoria)
        print(f"\nLa categoría '{nombre_categoria}' ha sido creada exitosamente.\n")
    else:
        print(f"\nLa categoría '{nombre_categoria}' ya existe.\n")

def eliminar_receta(carpeta_recetas):
    carpeta_categoria = elegir_categoria(carpeta_recetas)
    ruta_receta = mostrar_recetas(carpeta_categoria)
    
    # Confirmar eliminación
    confirmacion = input(f"¿Estás seguro de que deseas eliminar la receta '{Path(ruta_receta).stem}'? (s/n): ")
    if confirmacion.lower() == 's':
        os.remove(ruta_receta)
        print(f"\nLa receta '{Path(ruta_receta).stem}' ha sido eliminada.\n")
    else:
        print("\nOperación cancelada.\n")

def eliminar_categoria(carpeta_recetas):
    carpeta_categoria = elegir_categoria(carpeta_recetas)
    
    # Confirmar eliminación
    confirmacion = input(f"¿Estás seguro de que deseas eliminar la categoría '{Path(carpeta_categoria).name}' y todas sus recetas? (s/n): ")
    if confirmacion.lower() == 's':
        # Eliminar todos los archivos y luego la carpeta
        for archivo in os.listdir(carpeta_categoria):
            os.remove(os.path.join(carpeta_categoria, archivo))
        os.rmdir(carpeta_categoria)
        print(f"\nLa categoría '{Path(carpeta_categoria).name}' ha sido eliminada.\n")
    else:
        print("\nOperación cancelada.\n")

def menu(carpeta_recetas):
    opcion = 0
    while opcion != 6:
        limpiar_pantalla()
        opcion = int(input('''\nElija la opción que desee realizar:
            [1] - Leer receta
            [2] - Crear receta
            [3] - Crear categoría
            [4] - Eliminar receta
            [5] - Eliminar categoría
            [6] - Finalizar programa
        '''))

        if opcion == 1:
            carpeta_categoria = elegir_categoria(carpeta_recetas)
            ruta_receta = mostrar_recetas(carpeta_categoria)
            contenido = leer_receta(ruta_receta)
            print(f"\nContenido de la receta:\n{contenido}\n")
            input("Presiona Enter para regresar al menú...")

        elif opcion == 2:
            carpeta_categoria = elegir_categoria(carpeta_recetas)
            crear_receta(carpeta_categoria)
            input("Presiona Enter para regresar al menú...")

        elif opcion == 3:
            crear_categoria(carpeta_recetas)
            input("Presiona Enter para regresar al menú...")

        elif opcion == 4:
            eliminar_receta(carpeta_recetas)
            input("Presiona Enter para regresar al menú...")

        elif opcion == 5:
            eliminar_categoria(carpeta_recetas)
            input("Presiona Enter para regresar al menú...")

        elif opcion == 6:
            print("\nPrograma finalizado. ¡Hasta pronto!\n")

bienvenida()
carpeta_recetas = os.path.abspath("Recetas")
menu(carpeta_recetas)
