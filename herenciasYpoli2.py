#!/usr/bin/env python3

class A:
    def __init__(self):
        print("Inicializando A")
class B(A):
    def __init__(self):
        print("Inicializando B")
        super().__init__()     #### se utiliza esto para llamar a los 2 constructores a la vez
b = B()



class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def saludo(self):
        return f"Hola soy {self.nombre} y tengo {self.edad} años"
        
class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)      
        self.salario = salario
    def saludo(self):
        print(f"{super().saludo()}, y cobro {self.salario}")  
persona = Empleado("lucas", 29, 4239123)    
persona.saludo()