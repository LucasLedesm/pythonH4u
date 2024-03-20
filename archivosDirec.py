import os   
import shutil

if os.path.exists("mi_archivo.txt"):
    print("el archivo existe")
else:
    print("el archivo no existe")
    
if not os.path.exists("mi_directorio"):
    os.mkdir("mi_directorio")  ## con makedirs se puede crear subdirectorios mi_directorio/subdirectorio
    print("se creo mi_directorio")
if os.path.exists("mi_directorio"):
    os.rmdir("mi_directorio")     ## os.remove para borrar archivos
    print("se borro mi_directorio")
    
if not os.path.exists("mi_subdirectorio2/subdirec"):
    os.makedirs("mi_subdirectorio2/subdirec")
    print("se crearon directorios")
    
if os.path.exists("mi_subdirectorio2/subdirec"):
    shutil.rmtree("mi_subdirectorio2")    ### borra todo el arbol
    print("se borro todo el tree")
    
if os.path.exists("rename.txt"):
    os.rename("rename.txt", "renamed.txt")
    print("se renombro el archivo")