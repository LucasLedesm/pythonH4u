#!/usr/bin/env python3


name = "lucas"
rol = "lammer"
edad = 28

print("mi nombre es " + name)
print("mi nombre es %s " % name)
print("mi nombre es %s y soy un %s" % (name, rol))
print("mi nombre es %s y soy un %s . tengo %d años" % (name, rol, edad))

print("mi nombre es {}".format(name))
print("mi nombre es {} y tengo {} años".format(name, edad))
print("mi nombre es {0} y tengo {1} años. mi nombre real tambien es {0}".format(name, edad))
print(f"mi nombre es {name} y tengo {edad} años. mi nombre real tambien es {name}")