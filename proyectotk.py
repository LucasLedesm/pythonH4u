import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.geometry('800x600')
root.title("Mi primera aplicacion")


def accion_de_boton():
    print(f"Se ha presionado el boton")

def get_data():
    data = entry_widget.get()  ## si se usa tk.text hay que agregar .get("1.0, tk.end") para que agarre todo el texto
    print(f"lo que ha introducido es {data}")
def accion_menu():
    messagebox.showwarning("texto1", "texto2")
barra_menu = tk.Menu(root)
entry_widget = tk.Entry(root)    ## podmos usar tk.text para que el campo sea mas grande

label1 = tk.Label(root, text="Hola mundo!", bg="blue")
#label2 = tk.Label(root, text="Hola mundo!", bg="red")
#label3 = tk.Label(root, text="Hola mundo!", bg="green")


button = tk.Button(root, text="Presioname!", command=accion_de_boton)
button2 = tk.Button(root, text="Enter", command=get_data)

frame = tk.Frame(root, bg="black", bd=2 )

label_frame = tk.Label(frame, text="Hola mundo frame!", bg="red")
label1.pack(fill=tk.X) #side=tk.LEFT, fill=tk.y  para que el label este a la izquierda
#label2.grid(row=0,column=0, columnspan=2)
#label3.place(relx=0.8, rely=0.2, anchor=tk.center)   

root.config(menu=barra_menu)

menu1 = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Menu", menu=menu1)

menu1.add_command(label="opcion1")
menu1.add_command(label="opcion2")

menu2 = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Opciones", menu=menu2)

menu2.add_command(label="opcion1", command=accion_menu)

button.pack(side=tk.BOTTOM)
entry_widget.pack(pady=10, fill=tk.X, padx=20)
button2.pack(side=tk.TOP)
frame.pack(fill=tk.X, padx=10)
label_frame.pack(fill=tk.X, padx=20, pady=10)
root.mainloop()
