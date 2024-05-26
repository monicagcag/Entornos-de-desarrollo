import unittest
import json
import os
from libreria import Libreria


class TestLibreria(unittest.TestCase):

    def setUp(self):
        """Configurar el entorno de prueba antes de cada prueba."""
        self.libreria = Libreria()
        self.libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
        self.libreria.anadir_libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Novela", 1605)
        self.test_file = 'test_libreria.json'

    def tearDown(self):
        """Limpia el entorno de prueba después de cada prueba."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_anadir_libro(self):
        # Caso típico
        resultado = self.libreria.anadir_libro("1984", "George Orwell", "Distopía", 1949)
        self.assertEqual(resultado, "Libro añadido")
        self.assertEqual(len(self.libreria.libros), 3)
        # Caso extremo: año negativo
        resultado = self.libreria.anadir_libro("Libro Antiguo", "Autor Desconocido", "Historia", -500)
        self.assertEqual(resultado, "Libro añadido")
        self.assertEqual(len(self.libreria.libros), 4)
        # Error de entrada: año no numérico
        with self.assertRaises(TypeError):
            self.libreria.anadir_libro("Libro Erróneo", "Autor Erróneo", "Error", "año")

    def test_buscar_libro(self):
        # Caso típico
        resultado = self.libreria.buscar_libro("Cien años de soledad")
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0]['autor'], "Gabriel García Márquez")
        # Caso no encontrado
        resultado = self.libreria.buscar_libro("El señor de los anillos")
        self.assertEqual(len(resultado), 0)
        # Caso insensible a mayúsculas/minúsculas
        resultado = self.libreria.buscar_libro("cien años de soledad")
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0]['autor'], "Gabriel García Márquez")

    def test_buscar_por_autor(self):
        # Caso típico
        resultado = self.libreria.buscar_por_autor("Gabriel García Márquez")
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0]['titulo'], "Cien años de soledad")
        # Caso no encontrado
        resultado = self.libreria.buscar_por_autor("J.R.R. Tolkien")
        self.assertEqual(len(resultado), 0)
        # Caso insensible a mayúsculas/minúsculas
        resultado = self.libreria.buscar_por_autor("miguel de cervantes")
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0]['titulo'], "Don Quijote de la Mancha")

    def test_eliminar_libro(self):
        # Caso típico
        resultado = self.libreria.eliminar_libro("Cien años de soledad")
        self.assertEqual(resultado, "Libro eliminado")
        self.assertEqual(len(self.libreria.libros), 1)
        # Caso no encontrado
        resultado = self.libreria.eliminar_libro("El señor de los anillos")
        self.assertEqual(resultado, "Libro no encontrado")
        self.assertEqual(len(self.libreria.libros), 1)

    def test_guardar_libros(self):
        # Caso típico
        resultado = self.libreria.guardar_libros(self.test_file)
        self.assertEqual(resultado, "Libros guardados")
        with open(self.test_file, 'r') as f:
            datos = json.load(f)
        self.assertEqual(len(datos), 2)
        self.assertEqual(datos[0]['titulo'], "Cien años de soledad")

    def test_cargar_libros(self):
        # Caso típico
        self.libreria.guardar_libros(self.test_file)
        nueva_libreria = Libreria()
        resultado = nueva_libreria.cargar_libros(self.test_file)
        self.assertEqual(resultado, "Libros cargados")
        self.assertEqual(len(nueva_libreria.libros), 2)
        self.assertEqual(nueva_libreria.libros[0]['titulo'], "Cien años de soledad")
        # Caso archivo no encontrado
        resultado = nueva_libreria.cargar_libros('archivo_inexistente.json')
        self.assertEqual(resultado, "Archivo no encontrado")

    def test_integracion(self):
        # Prueba de integración que combina varias funcionalidades
        self.libreria.anadir_libro("1984", "George Orwell", "Distopía", 1949)
        self.libreria.guardar_libros(self.test_file)
        nueva_libreria = Libreria()
        nueva_libreria.cargar_libros(self.test_file)
        resultado = nueva_libreria.buscar_libro("1984")
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0]['autor'], "George Orwell")
        resultado = nueva_libreria.eliminar_libro("1984")
        self.assertEqual(resultado, "Libro eliminado")
        self.assertEqual(len(nueva_libreria.libros), 2)
        
    def test_contar_libros(self):
        # Caso típico
        self.assertEqual(self.libreria.contar_libros(), 2)
         # Añadir un libro y contar de nuevo.
        self.libreria.anadir_libro("1984", "George Orwell", "Distopía", 1949)
        self.assertEqual(self.libreria.contar_libros(), 3)
        # Eliminar un libro y contar de nuevo.
        self.libreria.eliminar_libro("1984")
        self.assertEqual(self.libreria.contar_libros(), 2)
        # Caso extremo: Contar libros cuando la librería está vacía.
        self.libreria.eliminar_libro("Cien años de soledad")
        self.libreria.eliminar_libro("Don Quijote de la Mancha")
        self.assertEqual(self.libreria.contar_libros(), 0)


if __name__ == '__main__':
    unittest.main()

