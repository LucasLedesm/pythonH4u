#!/usr/bin/env python3

class calculadora:
    @staticmethod
    def suma(num1, num2):
    
        return num1 + num2
    @staticmethod
    def resta(num1, num2):
        return num1 - num2
    @staticmethod
    def multi(num1, num2):
    
        return num1 * num2
    @staticmethod
    def divi(num1, num2):
    
        return num1 / num2
print(calculadora.suma(4, 2))
print(calculadora.resta(4,2))
print(calculadora.multi(4, 2))
print(calculadora.divi(4, 2))


class automovil:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    @classmethod
    def deportivos(cls, marca):
        return cls(marca, "deportivo")
    @classmethod
    def sedan(cls, marca):
        return cls(marca, "sedan")
    def __str__(self):
        return f"la marca {self.marca} es un modelo {self.modelo}"
deportivo = print(automovil.deportivos("ferrari"))
sedan = print(automovil.sedan("toyota"))
