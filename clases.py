#!/usr/bin/env python3

class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def saludo(self):
        return f"hola, soy {self.nombre} y tengo {self.edad} años"    
marcelo = persona("marcelo", 28)
juan = persona("juan", 21)
print(juan.saludo())


class animal:
    def __init__(self, nombre, patas, tipo):
        self.nombre = nombre
        self.patas = patas
        self.tipo = tipo
    def definicion(self):
        return  f"el es {self.nombre}, es de tipo {self.tipo} y tiene {self.patas} patas"
        
gato = animal("michi", 4, "gato")
perro = animal("thor", 4, "perro")
pez = animal("qwerty", 0, "pez")

print(perro.definicion())


class cuenta_bancaria:
    def __init__(self, cvu, dinero, titular):
        self.cvu = cvu
        self.dinero = dinero
        self. titular = titular
        
        
        
    def depositar_dinero(self, dineroNuevo):
        self.dinero += dineroNuevo
        return f"se han depositado {dineroNuevo},el monto total ahora es de {self.dinero}"
    
    
    def retirar_dinero(self, dineroNuevoR):
        if dineroNuevoR > self.dinero :
            
            return("no tenes suficiente dinero para retirar")
        self.dinero -= dineroNuevoR
        return f"se ha retirado {dineroNuevoR}, el monto total ahora es de {self.dinero}"
    
    
    
    def informacion(self):
        return   f"la cuenta con el cvu : {self.cvu} tiene un monto de ${self.dinero} y esta a nombre de {self.titular}"

lucas = cuenta_bancaria("123534123123", 9123, "Lucas Ledesma")
nicolas = cuenta_bancaria("128934719812", 43534, "Nicolas Ledesma")
facundo = cuenta_bancaria("3459823423412", 123135, "Facundo Ledesma")

print(lucas.informacion())
print(lucas.depositar_dinero(2342))
print(lucas.retirar_dinero(11465))