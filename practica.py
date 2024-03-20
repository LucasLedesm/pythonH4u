#!/usr/bin/env python3

class player:
    
    def __init__(self, raza, fuerza=0, energia=0, agilidad=0, vitalidad=0 ):
        self.raza = raza
        self.fuerza = fuerza
        self.energia = energia
        self.agilidad = agilidad
        self.vitalidad = vitalidad
       
       
    
    def daño(self):
        if self.raza == "guerrero":
            return   self.fuerza * self.agilidad
        if self.raza == "mago":
            return   self.energia * self.agilidad
        if self.raza == "asesino":
            return   self.fuerza + self.agilidad + self.energia
        if self.raza == "elfo":
            return   self.vitalidad * self.agilidad
    def informacion(self):
        return f"Hola veo que elegiste ser un {self.raza} tus stats son: \n [+]fuerza:{self.fuerza}\n [+]agilidad:{self.agilidad}\n [+]vitalidad:{self.vitalidad}\n [+]energia:{self.energia}\n [+]daño:{self.daño()}"
             
            

player1 = player("guerrero",10,90,50,40)
player2 = player("mago",40,30,60,10)
print(player1.informacion())
print(player2.informacion())


 