from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry("400x250")
root.title("Chương trình in ra Họ và Tên")

#======= BẮT ĐẦU PHẦN THÂN CHƯƠNG TRÌNH
# Khai báo hàm xử lý
def addName():
    First_Name = str(ho.get())
    Last_Name = str(ten.get())
    result = "Xin chào" + " " + First_Name + " " + Last_Name
    ket_qua.config(text="Kết quả: " + str(result))

Label(root, text = "Nhập họ").grid(row = 0, column = 0)
ho = Entry(root)
ho.grid(row = 0, column = 1)

Label(root, text = "Nhập tên").grid(row = 1, column = 0)
ten = Entry(root)
ten.grid(row = 1, column = 1)

Button(root, text = "Xử lý",command=addName).grid(row = 2, column = 0)
ket_qua = Label(root,text="Kết quả")
ket_qua.grid(row = 3, column = 1)

root.mainloop()