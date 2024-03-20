#!/usr/bin/env python3

names = ["lucas", "pepe", "s4vitar", "augusto"]

for i in range(5):
    print(i)

for name in names:
    print(f"el nombre para esta vuelta es {name}")

for indice, name in enumerate(names):
    print(f"Nombre : [{indice +1}] : [{name}]")

a = 0   
while a < 5:
    print(a)
    a += 1     


frutas = {"manzanas" : 1, "peras": 4, "kiwis": 2}
for fruta, cantidad in frutas.items():
    print(f"hay {cantidad} unidad de {fruta}")
    
    
my_list = [[1,2,3], [4,5,6], [7,8,9]]
for element in my_list:
    print(f"ahora vamos a desglosar la lista : {element}")
    for element_in_list in element:
      print(element_in_list)