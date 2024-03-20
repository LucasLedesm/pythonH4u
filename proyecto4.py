#!/usr/bin/env python3

class Vehiculos:
    
    def __init__(self, matricula, modelo, marca):
        self.matricula = matricula
        self.modelo = modelo
        self.marca = marca
        self.disponible = True

    def __str__(self):
        return f"\n [+] Vehiculo {self.marca} {self.modelo} matricula: {self.matricula} {'esta disponible' if self.disponible else 'no esta disponible'}"
    
    def alquilar(self):
        if self.disponible:
            self.disponible = False
        else:
            print(f"El vehiculo ya fue alquilado!")
class Flota:
    
    def __init__(self):
        self.vehiculos = []
        
    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
        
    def __str__(self):
        return "\n".join(str(vehiculo) for vehiculo in self.vehiculos)
    
    def alquilar_vehiculo(self, matricula):
        for vehiculo in self.vehiculos:
            if vehiculo.matricula == matricula:
                vehiculo.alquilar()
if __name__ == '__main__':
    
    flota = Flota()
    flota.agregar_vehiculo(Vehiculos("WQY202", "Corolla", "Toyota"))
    flota.agregar_vehiculo(Vehiculos("VTR909", "Civic", "Honda"))
    print("\n [+] Flota inicial:")
    print(flota)
    flota.alquilar_vehiculo("WQY202")
    print("\n [+] Flota:")
    print(flota)
    flota.alquilar_vehiculo("WQY202")