#!/usr/bin/env python3

def mi_decorador(funcion):
    def envoltura():
        print("esto es antes de la funcion")
        funcion()
        print("esto es despues de la funcion")
    return envoltura


@mi_decorador
def saludo():
    print("saludo desde funcion")
    
saludo()

class Circunferencia:
    def __init__(self, radio):
        self._radio = radio
        
    @property
    def radio(self):
        return self._radio
    @property     ###getter
    def diametro(self):
        return 2* self._radio
    @property     ###getter
    def area(self):
        return 3.1415 * (self._radio**2) 
    @radio.setter   ### setter
    def radio(self, valor):
        self._radio = valor


c = Circunferencia(5)
print(c.radio)
print(c.diametro)
print(c.area)
c.radio = 10    
print(c.radio)
print(c.diametro)
print(c.area)