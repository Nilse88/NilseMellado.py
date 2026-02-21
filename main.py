import glob
import os
from pelicula import Pelicula, CatalogoPelicula

def mostrar_catalogos_existentes():
    archivos = glob.glob("*.txt")
    if archivos:
        print("\n📂 Catálogos detectados:")
        for archivo in archivos:
            print(f" - {archivo[:-4]}")

def ejecutar_menu():
    while True:
        print("\n" + "="*40)
        print("      SISTEMA DE GESTIÓN DE CINE")
        print("="*40)
        
        mostrar_catalogos_existentes()
        nombre_cat = input("\nNombre del catálogo (o 'salir'): ").strip()
        
        if nombre_cat.lower() == 'salir':
            break
        if not nombre_cat: continue

        catalogo = CatalogoPelicula(nombre_cat)
        
        while True:
            print(f"\n--- TRABAJANDO EN: {catalogo.nombre.upper()} ---")
            print("1. Agregar Película")
            print("2. Listar Películas")
            print("3. Eliminar una Película") # Nueva opción
            print("4. Eliminar catálogo completo")
            print("5. Volver / Cambiar catálogo")
            print("6. Salir")
            
            opcion = input("Seleccione: ")

            if opcion == "1":
                n = input("Nombre de la película: ")
                catalogo.agregar(Pelicula(n))
            elif opcion == "2":
                catalogo.listar()
            elif opcion == "3":
                peli_a_borrar = input("Nombre exacto de la película a eliminar: ")
                catalogo.eliminar_pelicula(peli_a_borrar)
            elif opcion == "4":
                catalogo.eliminar()
                break 
            elif opcion == "5":
                break 
            elif opcion == "6":
                return 
            else:
                print("🚫 Opción no válida.")

if __name__ == "__main__":
    ejecutar_menu()