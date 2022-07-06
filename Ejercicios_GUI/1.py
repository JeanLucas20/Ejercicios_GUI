from cProfile import label
from cgitb import text
from tkinter import Tk, Label


# Crea una ventana llamada root de la clase TK.


root = Tk() 
root.geometry("500x500")


root.resizable(True, False)

root.minsize(50 ,50)
root.maxsize(500, 500)

etiqueta= Label(text= "\nUIS Socorro\n")
etiqueta.pack()

root.mainloop()


