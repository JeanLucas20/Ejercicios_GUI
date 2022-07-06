from tkinter import Tk, Label, TOP, BOTTOM, LEFT, RIGHT 
#Crea una ventana llamada root, de la clase TK. Se crea un objeto de la clase Tk 
root = Tk()

#Definimos el tamaño de la ventana
root.geometry("500x500")

root.resizable(True, False)

root.minsize(50,50)
root.maxsize(500,500)

# Agregamos etiqueta a la ventana
etiqueta1 = Label(text="UIS SOCORRO 1")
etiqueta2 = Label(text="UIS SOCORRO 2")
etiqueta3 = Label(text="UIS SOCORRO 3")
etiqueta4 = Label(text="UIS SOCORRO 4")

etiqueta1.pack(side = LEFT, padx=10,pady=20)
etiqueta2.pack(padx=10,pady=20)
etiqueta3.pack(padx=10,pady=50)
etiqueta4.pack(padx=10,pady=20)
