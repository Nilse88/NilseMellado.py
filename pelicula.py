import os
    # Se crea la clase Pelicula cuyo constructor recibe el nombre de la película y lo almacena como un atributo privado para evitar modificaciones directas. 
     # Se aplica el principio de encapsulamiento para controlar el acceso al nombre de la película.
class Pelicula:
    def __init__(self, nombre):
        self.__nombre = nombre.strip()  
        
    @property 
    def nombre(self): 
        return self.__nombre 
    
    # También se crea la clase CatalogoPelicula que permite agregar, listar y eliminar películas, así como eliminar el catálogo completo.
    # A través de su constructor, recibe el nombre del catálogo y define la ruta del archivo donde se almacenarán las películas.
class CatalogoPelicula: 
    def __init__(self, nombre): 
        self.nombre = nombre 
        self.ruta_archivo = f"{self.nombre}.txt" 

    def agregar(self, pelicula): 
        if not pelicula.nombre:
            print(" Error: Nombre vacío.") 
            return 
        
        if os.path.exists(self.ruta_archivo): 
            with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
                existentes = [linea.strip().lower() for linea in archivo.readlines()] 
                if pelicula.nombre.lower() in existentes: 
                    print(f"⚠️ '{pelicula.nombre}' ya existe.")
                    return 
                
        with open(self.ruta_archivo, "a", encoding="utf-8") as archivo: 
            archivo.write(f"{pelicula.nombre}\n") 
        print(f"✅ Guardada en '{self.ruta_archivo}'") 

    def listar(self):
        if not os.path.exists(self.ruta_archivo):
            print(f"⚠️ El catálogo '{self.nombre}' no tiene películas.")
            return []
        with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
            lineas = [linea.strip() for linea in archivo.readlines()]
            if lineas:
                print(f"\n--- Películas en: {self.nombre.upper()} ---")
                for i, nombre in enumerate(lineas, 1):
                    print(f"{i}. {nombre}")
            return lineas

    def eliminar_pelicula(self, nombre_peli):
        """Elimina una película específica del archivo."""
        if not os.path.exists(self.ruta_archivo):
            return

        with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
        
        # Filtramos las líneas: mantenemos solo las que NO coinciden con el nombre buscado
        nuevas_lineas = [l for l in lineas if l.strip().lower() != nombre_peli.lower()]

        if len(lineas) == len(nuevas_lineas):
            print(f"❌ No se encontró la película '{nombre_peli}'.")
        else:
            with open(self.ruta_archivo, "w", encoding="utf-8") as archivo:
                archivo.writelines(nuevas_lineas)
            print(f"🗑️ Película '{nombre_peli}' eliminada.") 

    def eliminar(self):
        if os.path.exists(self.ruta_archivo):
            os.remove(self.ruta_archivo)
            print(f"🗑️ Catálogo '{self.nombre}' borrado por completo.")
        
