#!/usr/bin/env python3

import re  

text = "Mi gato esta en el jardin y mi otro gato esta en el tejado"
text2 = "Hoy es 17/01/2023 y mañana sera 18/01/2023"
text3 = "Nuestros usuarios de la academia se pueden contactar a soporte@hack4u.io o a support@hack4u.io"
matches = re.findall("gato", text)
matches2 = re.findall("\d{2}\/\d{2}\/\d{4}", text2)
matches3 = re.findall("(\w+)@(\w+\.\w{2,})", text3)
nuevoTexto = re.sub("gato" , "perro", text)
print(matches)
print(matches2)
print(matches3)
print(nuevoTexto)

def validar_correo(correo):
    
    patron = "[A-Za-z0-9._+-]@[A-Za-z0-9]+\.[A-Za-z]{2,}"
    
    if re.findall(patron, correo):
        return True
    else:
        return False
print(validar_correo("lucas_ledesma-92@gmail.com"))