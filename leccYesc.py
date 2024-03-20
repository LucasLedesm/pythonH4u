####de esta manera hay que cerrar manualmente si o si el archivo
#f=open("example.txt", "w")
#f.write("Hola mundo!")
#f.close

### de esta manera se cierra solo
with open("example.txt", "w") as f:
    f.write("Hola mundo!")
##  f.writelines(mi_lista)       pasa varias lineas que tengas en una lista

#with open("/etc/hosts" , "r") as f:
#    file_content=f.read()
#print(file_content)

with open("/etc/hosts", "r") as f: ##el"rb" es para leer binarios
    for line in f:
        print(line.strip())