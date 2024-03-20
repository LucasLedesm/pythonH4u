#!/usr/bin/env python3

mi_conjunto = {1,2,3}
mi_tupla = (1,2,3)
mi_lista = [1,2,3]

mi_conjunto.add(6)
mi_conjunto.update({7,8,9})
mi_lista.append(6)
mi_lista.extend([7,8,9])
#### la tupla no se puede modificar.

print(type(mi_conjunto),mi_conjunto)
print(type(mi_tupla),mi_tupla)
print(type(mi_lista),mi_lista)
