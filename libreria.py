import json


class Libreria:
    """
    Una clase utilizada para representar una Librería.

    Atributos:
        libros (list): Una lista de diccionarios que almacenan la información de los libros.
    """
    
    def __init__(self):
        """Inicializa una nueva instancia de Libreria con una lista vacía de libros."""
        self.libros = []

    def anadir_libro(self, titulo, autor, genero, anio):
        """
        Añade un nuevo libro a la lista de libros.
        
        Args:
            titulo (str): El título del libro.
            autor (str): El autor del libro.
            genero (str): El género del libro.
            anio (int): El año de publicación del libro.
        
        Returns:
            str: Mensaje confirmando que el libro ha sido añadido.
        """
        if not isinstance(anio, int):
            raise TypeError("El año debe ser un número entero.")
        self.libros.append({'titulo': titulo, 'autor': autor, 'genero': genero, 'anio': anio})
        return "Libro añadido"

    def buscar_libro(self, titulo):
        """
        Busca un libro por su título.
        
        Args:
            titulo (str): El título del libro a buscar.
        
        Returns:
            list: Lista de libros que coinciden con el título buscado.
        """
        return [libro for libro in self.libros if libro['titulo'].lower() == titulo.lower()]

    def buscar_por_autor(self, autor):
        """
        Busca libros por autor.
        
        Args:
            autor (str): El autor de los libros a buscar.
        
        Returns:
            list: Lista de libros que coinciden con el autor buscado.
        """
        return [libro for libro in self.libros if autor.lower() in libro['autor'].lower()]

    def eliminar_libro(self, titulo):
        """
        Elimina un libro por su título.
        
        Args:
            titulo (str): El título del libro a eliminar.
        
        Returns:
            str: Mensaje confirmando si el libro ha sido eliminado o no encontrado.
        """
        original_count = len(self.libros)
        self.libros = [libro for libro in self.libros if libro['titulo'].lower() != titulo.lower()]
        return "Libro eliminado" if len(self.libros) < original_count else "Libro no encontrado"

    def guardar_libros(self, archivo):
        """
        Guarda la lista de libros en un archivo JSON.
        
        Args:
            archivo (str): El nombre del archivo donde se guardarán los libros.
        
        Returns:
            str: Mensaje confirmando que los libros han sido guardados.
        """
        with open(archivo, 'w') as f:
            json.dump(self.libros, f)
        return "Libros guardados"

    def cargar_libros(self, archivo):
        """
        Carga la lista de libros desde un archivo JSON.
        
        Args:
            archivo (str): El nombre del archivo desde donde se cargarán los libros.
        
        Returns:
            str: Mensaje confirmando que los libros han sido cargados o que el archivo no fue encontrado.
        """
        try:
            with open(archivo, 'r') as f:
                self.libros = json.load(f)
            return "Libros cargados"
        except FileNotFoundError:
            return "Archivo no encontrado"
        
    def contar_libros(self):
        """
        Cuenta el número de libros en la librería.

        Returns:
            int: El número de libros en la librería.
        """
        return len(self.libros)


# Ejemplo de uso de la clase Libreria
mi_libreria = Libreria()
mi_libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
mi_libreria.guardar_libros('libreria.json')
print(mi_libreria.cargar_libros('libreria.json'))
print(mi_libreria.buscar_por_autor("Gabriel García Márquez"))
