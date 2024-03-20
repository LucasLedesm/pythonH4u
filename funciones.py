#!/usr/bin/env python3

def saludo(nombre):
    print(f"hola {nombre}")

saludo("lucas")

def suma(numero1, numero2):
    return numero1 + numero2
resultado = suma(2,8)
print(f"el resultado de la suma es {resultado}")

def mi_funcion():
    variable_local = "soy local"
    print(variable_local)
mi_funcion()

#######funciones lambda anonimas#########

mi_funcion2 = lambda: "hola soy lambda"
print(mi_funcion2())

mi_funcion3 = lambda x : x * 2
print(mi_funcion3(4))

numeros = [1,2,3,4,5]
cuadrados =list(map(lambda x: x**2, numeros))
print(cuadrados)

numeros2 = [1,2,3,4,5]
pares =list(filter(lambda x: x % 2 == 0, numeros2))
print(pares)

numeros3 = [1,2,3,4,5]
impares =list(filter(lambda x: x % 2 == 1, numeros3))
print(impares)