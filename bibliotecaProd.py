#!/usr/bin/env python3
class Libro:
    
    def __init__(self, id_libro, autor, nombre_libro ):
        self.id_libro = id_libro
        self.autor = autor
        self.nombre_libro = nombre_libro
        self.esta_prestado = False
        
    def __str__(self):
        return f"Libro:({self.nombre_libro}) Autor({self.autor}) "
    
    def __repr__(self):
        return self.__str__()
class Biblioteca:
    def __init__(self):
        self.libros = {}
        
    def agregar_libro(self, libro):
        if libro.id_libro not in self.libros:
            self.libros[libro.id_libro]= libro
        else: 
            print(f"No es posible agregar el libro con ID {libro.id_libro}")
            
    def prestar_libro(self, id_libro):
        if id_libro in self.libros and not self.libros[id_libro].esta_prestado:
            self.libros[id_libro].esta_prestado = True
        else:
            print(f"[!] Este libro no se encuentra en tu biblioteca!")
    @property
    def mostrar_libros(self):
        return [libro for libro in self.libros.values() if not libro.esta_prestado]
    @property
    def mostrar_libros_prestados(self):
        return [libro for libro in self.libros.values() if  libro.esta_prestado]
if __name__ =='__main__':
    
    
    biblioteca=Biblioteca()  
    libro1 = Libro(1, "Lucas Ledesma", "como ser un hacker?")
    libro2 = Libro(2, "Nicolas Ledesma", "Como ser un programador desde cero?")
      
    print(libro1)
    print(libro2)
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    print(f"\n [+] Libros en la biblioteca : {biblioteca.mostrar_libros}")
    biblioteca.prestar_libro(1)
    print(f"\n [+] Libros en la biblioteca : {biblioteca.mostrar_libros}")
    print(f"\n [+] Libros prestados : {biblioteca.mostrar_libros_prestados}")