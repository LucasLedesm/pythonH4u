#!/usr/bin/env python3

class Player:
    ####CLASES###
    Guerrero = {"Fuerza":40, "Agilidad":25, "Vitalidad":25, "Energia":10}
    Mago = {"Fuerza":10, "Agilidad":25, "Vitalidad":25, "Energia":40}
    ####ITEMS###
    ##Shields
    Shield_Crymson = {"Vitalidad":60, "Agilidad" :-10, "Clase" : "Guerrero"  }
    Shield_Barrier = {"Vitalidad":60, "Agilidad" :-10, "Clase" : "Mago"  }
    ###Swords&Staffs
    Bone_Sword = {"Fuerza":30, "Agilidad" :15, "Clase" : "Guerrero"  }
    Imperial_Sword = {"Fuerza":20, "Agilidad" :25, "Clase" : "Guerrero"  }
    Elemental_Sword = {"Fuerza":10, "Agilidad" :35, "Clase" : "Guerrero"  }
    Bone_Staff = {"Energia":30, "Agilidad" :15, "Clase" : "Mago"  }
    Imperial_Staff = {"Energia":20, "Agilidad" :25, "Clase" : "Mago"  }
    Elemental_Staff = {"Energia":10, "Agilidad" :35, "Clase" : "Mago"  }
    ####Sets
    Classic_set={"Fuerza":20, "Agilidad":-20, "Vitalidad":30, "Energia":0,"Clase" : "Guerrero"}
    Emperor_set={"Fuerza":30, "Agilidad":-10, "Vitalidad":50, "Energia":5,"Clase" : "Guerrero"}
    King_set={"Fuerza":40, "Agilidad":0, "Vitalidad":60, "Energia":10,"Clase" : "Guerrero"}
    
    Magic_set={"Fuerza":20, "Agilidad":-20, "Vitalidad":30, "Energia":0,"Clase" : "Mago"}
    Elemental_set={"Fuerza":30, "Agilidad":-10, "Vitalidad":50, "Energia":10,"Clase" : "Mago"}
    Wizard_set={"Fuerza":40, "Agilidad":0, "Vitalidad":60, "Energia":20,"Clase" : "Mago"}
    

    @classmethod    
    def play(cls):
        clase1 = "Guerrero"
        clase2 = "Mago"
        eleccion_clase = 0
        
        while eleccion_clase not in [1, 2]:
            eleccion_clase = int(input("Elija su clase:\n1-Guerrero\n2-Mago\n"))
            if eleccion_clase == 1:
                return f"Has elegido la clase: {clase1}\nStats: {cls.Guerrero}"
            elif eleccion_clase == 2:
                return f"Has elegido la clase: {clase2}\nStats: {cls.Mago}"

print(Player.play())

