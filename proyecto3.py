#!/usr/bin/env python3

class Animal:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie
        self.alimentado = False
        
    def alimentar(self):
        self.alimentado = True

    def __str__(self):
        return f"{self.nombre} es un : {self.especie}, {'alimentado' if self.alimentado else 'Hambriento'}"
class TiendaAnimales:
    def __init__(self, nombre):
        self.nombre = nombre
        self.animales = []
        
    def agregar_animal(self, animal):
        self.animales.append(animal)
        
    def mostrar_animales(self):
        for animal in self.animales:
            print(animal)
            
        
    def alimentar_animales(self):
        for animal in self.animales:
            animal.alimentar()
   
        
if __name__ == '__main__':
    
    tienda = TiendaAnimales("Mi tienda de animales")
    
    gato=Animal("michi", "gato")
    perro=Animal("thor", "perro")
    
    tienda.agregar_animal(gato)
    tienda.agregar_animal(perro)
    
    
    tienda.mostrar_animales()
    tienda.alimentar_animales()
    
    print("[+] alimentando animales....")
    
    tienda.mostrar_animales()