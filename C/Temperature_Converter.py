from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry("400x250")
root.title("Temperature Converter")

def F_to_C():
    TempF = int(F.get())
    resultC = 5/9 * (TempF - 32)
    ket_quaC.config(text=resultC)

def C_to_F():
    TempC = int(C.get())
    resultF = 9/5 * TempC  + 32
    ket_quaF.config(text=resultF)

F = Entry(root)
F.grid(row=0, column=0)
Label(root, text = "\N{DEGREE FAHRENHEIT}").grid(row = 0, column = 1)
Button(root, text = "\N{RIGHTWARDS BLACK ARROW}",command= F_to_C).grid(row = 0, column = 2)

C = Entry(root)
C.grid(row=1, column=0)
Label(root, text = "\N{DEGREE CELSIUS}").grid(row = 1, column = 1)
Button(root, text = "\N{RIGHTWARDS BLACK ARROW}",command= C_to_F).grid(row = 1, column = 2)

ket_quaC = Label(root)
ket_quaC.grid(row = 0, column = 3)

ket_quaF = Label(root)
ket_quaF.grid(row = 1, column = 3)

root.mainloop()
