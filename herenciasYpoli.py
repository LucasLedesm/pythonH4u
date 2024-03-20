#!/usr/bin/env python3

class animal:
    def __init__(self, nombre):
        self.nombre = nombre
    def hablar(self):
        pass
    
class gato(animal):
    def hablar(self):
        return f"dice miau!"
class perro(animal):
    def hablar(self):
        return f"dice guau!"
    
def hacer_hablar(objeto):
    print(f"{objeto.nombre} dice {objeto.hablar()} ")
    
animal1 = gato("firulais")
animal2 = perro("toto")
hacer_hablar(animal1)
hacer_hablar(animal2)


class automovil:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo  
        
    def describir(self):
        pass
    
class auto(automovil):
    def describir(self):
        
        return f"vehiculo: {self.marca} {self.modelo}"

class moto(automovil):
    def describir(self):
        
        return f"moto: {self.marca} {self.modelo}"
    
auto1 = auto("ferrari", "testarosa")
moto1= moto("honda", "cbr")
print(auto1.describir())      
print(moto1.describir())