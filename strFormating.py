cadena="       HOla mundo     "
print(cadena.strip()) ### .strip() elimina espacios, saltos de linea y tabulaciones
print(cadena.lower()) ### .lower() pasa todo a minuscula
print(cadena.upper()) ### .upper() pasa todo a mayuscula
print(cadena.replace("o", "x")) ### .replace() remplza digitos
nueva_cadena = cadena.split("m")    ###.split() es un delimitador, divide segun indiques
print(nueva_cadena)    
print(cadena.startswith("  ")) ###startwith comprueba si la cadena empieza con lo que le indiques
print(cadena.endswith("  ")) ### endswith comprueba si la cadena termina en lo que le indiques
print(cadena.index("la"))  ### .index indica en que posicion del index esta lo que le indiques
print(cadena.count("o")) ### cuenta las veces que se repite el caracter indicado
print(".".join(cadena))  ### unifica toda la cadena segun lo que indiques
print(cadena.isalpha())
print(cadena.isalnum())
print(cadena.isdigit())  ### con . "is..." son preguntas, cadena estacompuesta por espacios?
print(cadena.isspace())
tabla =str.maketrans("oau", "xyz")
nueva_cadena2= cadena.translate(tabla)   ###sustitucion avanzada de varios caracteres
print(nueva_cadena2)
      