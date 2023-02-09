import tkinter as tk

def funcion():
    otra_ventana = tk.Toplevel(root)
    root.iconify()

root = tk.Tk()
boton = tk.Button(root, text="Abrir otra ventana", command=funcion)
boton.pack()
root.mainloop()