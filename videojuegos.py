#!/usr/bin/env python3

#Juegos
juegos = ["Mu online", "Diablo4", "DeadSpace2", "Left4Dead"]

#Generos
generos = {
    "Mu online" : "MMORPG",
    "Diablo4" : "MMORPG",
    "DeadSpace2" : "Accion",
    "Left4Dead" : "accion",
}
#Ventas y stock
ventas_y_stock = {
    "Mu online" : (200, 400),
    "Diablo4" : (500,200),
    "DeadSpace2" : (100,50),
    "Left4Dead" : (1000,30)
    
}
#CLientes
clientes = {
    "Mu online" : {"lucas", "nico", "facu", "marcelo", "alberto", "roberto"},
    "Diablo4" : {"diego", "luis"},
    "DeadSpace2" : {"Gabi", "marcos","macarena"},
    "Left4Dead" : {"micaela", "natalia", "lourdes"}
    
}


def sumario(juego):
    
    #sumario
    print(f"[i] -Resumen del juego {juego}\n")
    print(f"\t[+] -Genero del juego: {generos[juego]}")
    print(f"\t[+] -Quedan {ventas_y_stock[juego][1]} en stock, y se vendieron {ventas_y_stock[juego][0]}")
    print(f"\t[+] -los clientes que compraron {juego} son : {', '.join(clientes[juego])}")

for juego in juegos:
    sumario(juego)
    
ventas_totales = lambda: sum(ventas for ventas, _ in ventas_y_stock.values())
print(f"\t -El total de ventas es: {ventas_totales()} unidades")