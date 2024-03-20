#!/usr/bin/env python3

class rectangulo:
    def __init__(self, alto, ancho):
        self.alto = alto
        self.ancho = ancho
    @property                              ###con esta decoracion combierte el objeto en propiedad
    def area(self):
        return self.ancho * self.alto
    def __str__(self):      ###con esta decoracion se puede modificar lo que printea el objeto
        return f"\n las propiedades del objeto son: alto:{self.alto} y el ancho {self.ancho}"

rect1= rectangulo(20, 40)
print(f"el area es de : {rect1.area}")
print(rect1)


class libro:
    IVA = 0.21
    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio
    @staticmethod    ### decoracion para dejar de usar el objeto como tal y usar la clase
    def es_bestseller(total_ventas):
        return total_ventas > 5000
    @classmethod
    def precio_con_iva(cls, precio):
        return precio + precio * cls.IVA   
        
mi_libro = libro("como ser un hacker", "lucas", 2.99)
print(libro.es_bestseller(7000))
print(f"el precio del libro con IVA incluido es de: {libro.precio_con_iva(mi_libro.precio)}")