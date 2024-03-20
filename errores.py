#!/usr/bin/env python3

try:
    num = 5/0
except ZeroDivisionError:    #zerodivisionerror es el error que da la operacion
    print("error no se puede")
    
x = -5
if x < 0:
    raise Exception("no se puede utilizar numeros negativos")   #stack trace