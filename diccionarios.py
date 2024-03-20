#!/usr/bin/env python3

mi_diccionario = {"nombre": "lucas", "edad": 28, "nacionalidad": "argentino" }
del mi_diccionario["edad"]
mi_diccionario["nombre"] = "damian"
mi_diccionario["profesion"] = "pobre"
print(mi_diccionario)

if "nacionalidad" in mi_diccionario:
    print("esta clave existe")
else:
    print("no existe")
    
    
for key,values in mi_diccionario.items():
    print(f"para la clave {key} tendriamos el valor {values}")

cuadrados ={x: x**2 for x in range(23)}
print(cuadrados.keys())
print(cuadrados.values())