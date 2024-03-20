#!/usr/bin/env python3

my_ports = []
my_ports.append(22)
my_ports.append(21)
my_ports.append(21)
my_ports.append(80)
my_ports.append(443)
my_ports.extend([45,43])
my_ports += [8080,21]

my_ports = sorted(my_ports)

print (str (my_ports[3:]) +"sin los 3 primeros puertos")
print (str (my_ports[:3]) +"solo los 3 primeros puertos")

my_ports.insert(2, 99)  # cambia el valor que esta en la posicion 2 a "99"
my_ports.pop() # borra el ultimo valor
print("el valor de indice del 443 es: " + str (my_ports.index(443))) # muestra el valor de indice
print("El puerto 21 se repite : "+ str (my_ports.count(21)) + " veces")
for x, y in enumerate(my_ports):
    print("[+]el indice es: " + str (x) + " y el puerto es: " + str(y))

for port in my_ports:
    print("Puerto: " + str (port))
print(f"\n[+] la lista tiene un total de {len(my_ports)} elementos")


print("total de puertos excluyendo los repetidos :"+ str (sorted(set(my_ports))))
print("el puerto mas alto es :" + str(max(my_ports)))
print("el puerto mas bajo es :" + str(min(my_ports)))