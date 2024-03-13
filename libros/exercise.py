#!/usr/bin/env python3

# Ejercicio de biblioteca para practicar POO, herencia, etc.

class Libro:

    def __init__(self, id_libro, autor, nombre):
        self.id_libro = id_libro
        self.autor = autor
        self.nombre = nombre
        self.esta_prestado = False

    def __str__(self):
        return f"Libro ({self.id_libro}, {self.autor}, {self.nombre})"

    def __repr__(self):     # Esto es para mostrarlo en mostrar_libros
        return self.__str__()

class Biblioteca:

    def __init__(self):
        self.libros = {} # La clave el id y el valor el objeto libro

    def agregar_libro(self, libro):
        
        if libro.id_libro not in self.libros:
            self.libros[libro.id_libro] = libro  # Agregamos el libro
        else:
            print("No es posible agregar el libro con ID: {libro.id_libro}")
    
    def prestar_libro(self, id_libro):
        
        if id_libro in self.libros and not self.libros[id_libro].esta_prestado:
            self.libros[id_libro].esta_prestado = True

        else:
            print("\n[!] El libro cuyo ID es {id_libro} ya ha sido prestado")



    @property
    def mostrar_libros(self):
        return [libro for libro in self.libros.values() if not libro.esta_prestado]

    @property
    def mostrar_libros_prestados(self):
        return [libro for libro in self.libros.values() if libro.esta_prestado]

class BibliotecaInfantil(Biblioteca):

    def __init__(self):
        super().__init__()
        self.libros_infantiles = {}

    def agregar_libro(self, libro, es_infantil):
        super().agregar_libro(libro)
        self.libros_infantiles[libro.id_libro] = es_infantil

    def prestar_libro(self, id_libro, es_infantil):
        if id_libro in self.libros and self.libros_infantiles[id_libro] == es_infantil and not self.libros[id_libro].esta_prestado:
            self.libros[id_libro].esta_prestado = True

        else:
            print("\n[!] El libro cuyo ID es {id_libro} ya ha sido prestado")

    @property
    def mostrar_libros_estado_infantiles(self):
        return self.libros_infantiles

if __name__ == "__main__":

    biblioteca = BibliotecaInfantil()

    libro1 = Libro(1, "Marcelo Vázquez", "¿Cómo tensarla fuerte?")
    libro2 = Libro(2, "Pepe Romero", "Aprende a colorear desde cero")

    biblioteca.agregar_libro(libro1, es_infantil=False)
    biblioteca.agregar_libro(libro2, es_infantil=True)

    print(f"\n[+] Libros en la biblioteca: {biblioteca.mostrar_libros}")

    biblioteca.prestar_libro(1, es_infantil=False)

    print(f"\n[+] Libros en la biblioteca: {biblioteca.mostrar_libros}")
    print(f"\n[+] Libros prestados: {biblioteca.mostrar_libros_prestados}")
    print(f"\n[+] Libros para niños: {biblioteca.mostrar_libros_estado_infantiles}")
