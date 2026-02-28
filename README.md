Catálogo de Películas POO 🎬

Este es un sistema de gestión de películas desarrollado en Python utilizando el paradigma de Programación Orientada a Objetos (POO). 
El programa permite crear múltiples catálogos, gestionar películas dentro de cada uno y persistir la información en archivos de texto plano (.txt).

  Características

- Persistencia de datos: Las películas se guardan en archivos físicos, por lo que no se pierden al cerrar el programa.
- Gestión Multi-Catálogo: Puedes crear diferentes categorías (ej. Terror, Comedia, Favoritas) y trabajar en cada una por separado.
- Validaciones robustas: Evita el registro de nombres vacíos.
- Control de duplicados (ignora mayúsculas y minúsculas).
- Interfaz de consola amigable: Incluye un escáner automático que detecta y muestra los catálogos existentes al iniciar.

  Estructura del Proyecto
  
El código está dividido en dos módulos para mantener la limpieza y escalabilidad:
 - pelicula.py: Contiene las definiciones de las clases Pelicula (modelo de datos) y CatalogoPelicula (lógica de archivos y métodos).
 - main.py: Punto de entrada del programa. Gestiona los menús y la interacción con el usuario.

  Manual de Operaciones
  
Al ejecutar el programa, podrás:
 - Ingresar el nombre de un catálogo: Si el nombre no existe, se creará al agregar la primera película. Si existe, se cargará automáticamente.
 - Agregar Película: Registra un nuevo título en el archivo actual.
 - Listar Películas: Muestra todas las películas guardadas en el catálogo seleccionado.
 - Eliminar Película: Borra un título específico buscando por su nombre.
 - Eliminar Catálogo: Borra permanentemente el archivo .txt correspondiente.

 Conceptos de Programación Aplicados
 
 - Clases y Objetos: Modelado de entidades del mundo real.
 - Encapsulamiento: Atributos privados (__nombre) para proteger la integridad de los datos.
 - Decoradores: Uso de @property para acceso controlado a atributos.
 - Manejo de Archivos: Lectura (r), escritura (w) y anexado (a) de datos.
 - Modularidad: División del código en múltiples archivos .py.
